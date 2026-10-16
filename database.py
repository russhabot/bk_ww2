"""SQLite persistence layer for Burnt Kingdoms WW2.

The database file is selected by DB_PATH, or by RAILWAY_VOLUME_MOUNT_PATH when
Railway has attached a persistent volume. Legacy kv/players databases are migrated
on startup; season reset only clears country assignments and keeps player profiles.
"""
from __future__ import annotations

import json
import os
import sqlite3
import time
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
VOLUME_PATH = os.environ.get("RAILWAY_VOLUME_MOUNT_PATH", "").strip()
DEFAULT_PATH = Path(VOLUME_PATH) / "bk_ww2.db" if VOLUME_PATH else BASE_DIR / "bk_ww2.db"
DB_PATH = Path(os.environ.get("DB_PATH", str(DEFAULT_PATH))).expanduser()
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

db = sqlite3.connect(str(DB_PATH), check_same_thread=False, timeout=30)
db.row_factory = sqlite3.Row
db.execute("PRAGMA journal_mode=WAL")
db.execute("PRAGMA foreign_keys=ON")
db.execute("PRAGMA busy_timeout=30000")


def _table_exists(name: str) -> bool:
    return db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)).fetchone() is not None


def _columns(name: str) -> set[str]:
    return {row["name"] for row in db.execute(f"PRAGMA table_info({name})").fetchall()}


def init_db() -> None:
    # Preserve legacy player rows before creating the normalized schema.
    if _table_exists("players") and not {"uid", "data", "country_code"}.issubset(_columns("players")):
        if not _table_exists("players_legacy"):
            db.execute("ALTER TABLE players RENAME TO players_legacy")
        else:
            db.execute("DROP TABLE players")
    db.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL,
            updated_at INTEGER NOT NULL
        )
    """)
    db.execute("""
        CREATE TABLE IF NOT EXISTS players (
            uid INTEGER PRIMARY KEY,
            country_code TEXT UNIQUE,
            data TEXT NOT NULL,
            created_at INTEGER NOT NULL,
            updated_at INTEGER NOT NULL
        )
    """)
    db.execute("""
        CREATE TABLE IF NOT EXISTS season_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            season_number INTEGER NOT NULL,
            action TEXT NOT NULL,
            actor_id INTEGER,
            details TEXT NOT NULL DEFAULT '{}',
            created_at INTEGER NOT NULL
        )
    """)
    db.execute("""
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            actor_id INTEGER,
            action TEXT NOT NULL,
            target TEXT,
            details TEXT NOT NULL DEFAULT '{}',
            created_at INTEGER NOT NULL
        )
    """)
    db.execute("CREATE INDEX IF NOT EXISTS idx_players_country ON players(country_code)")
    db.execute("CREATE INDEX IF NOT EXISTS idx_season_history_number ON season_history(season_number)")

    # Migrate settings from the previous key/value table.
    if _table_exists("kv"):
        for row in db.execute("SELECT k, v FROM kv").fetchall():
            db.execute(
                "INSERT OR IGNORE INTO settings(key, value, updated_at) VALUES(?, ?, ?)",
                (str(row["k"]), str(row["v"]), int(time.time())),
            )

    # Migrate player JSON rows from the old schema; keep the first owner if legacy data
    # accidentally contains duplicate country claims.
    if _table_exists("players_legacy"):
        rows = db.execute("SELECT uid, data FROM players_legacy").fetchall()
        for row in rows:
            try:
                data = json.loads(row["data"])
                if not isinstance(data, dict):
                    continue
                code = str(data.get("c") or "").strip().upper() or None
                if code and db.execute("SELECT 1 FROM players WHERE country_code=?", (code,)).fetchone():
                    code = None
                    data["c"] = ""
                now = int(time.time())
                db.execute(
                    "INSERT OR IGNORE INTO players(uid, country_code, data, created_at, updated_at) VALUES(?, ?, ?, ?, ?)",
                    (int(row["uid"]), code, json.dumps(data, ensure_ascii=False), int(data.get("created_at") or now), now),
                )
            except (ValueError, TypeError, json.JSONDecodeError):
                continue

    now = int(time.time())
    db.execute("INSERT OR IGNORE INTO settings(key, value, updated_at) VALUES('season', 'wait', ?)", (now,))
    db.execute("INSERT OR IGNORE INTO settings(key, value, updated_at) VALUES('season_number', '1', ?)", (now,))
    db.execute("INSERT OR IGNORE INTO settings(key, value, updated_at) VALUES('schema_version', '2', ?)", (now,))
    db.commit()


def kget(key: str, default: Any = None) -> Any:
    row = db.execute("SELECT value FROM settings WHERE key=?", (key,)).fetchone()
    return row["value"] if row else default


def kset(key: str, value: Any) -> None:
    db.execute(
        "INSERT INTO settings(key, value, updated_at) VALUES(?, ?, ?) "
        "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
        (str(key), str(value), int(time.time())),
    )
    db.commit()


def pget(uid: int) -> dict[str, Any] | None:
    row = db.execute("SELECT data FROM players WHERE uid=?", (int(uid),)).fetchone()
    if not row:
        return None
    try:
        value = json.loads(row["data"])
        return value if isinstance(value, dict) else None
    except (ValueError, TypeError):
        return None


def pset(uid: int, data: dict[str, Any]) -> None:
    now = int(time.time())
    code = str(data.get("c") or "").strip().upper() or None
    payload = json.dumps(data, ensure_ascii=False)
    db.execute(
        "INSERT INTO players(uid, country_code, data, created_at, updated_at) VALUES(?, ?, ?, ?, ?) "
        "ON CONFLICT(uid) DO UPDATE SET country_code=excluded.country_code, data=excluded.data, updated_at=excluded.updated_at",
        (int(uid), code, payload, int(data.get("created_at") or now), now),
    )
    db.commit()


def pdel(uid: int) -> None:
    db.execute("DELETE FROM players WHERE uid=?", (int(uid),))
    db.commit()


def all_players() -> list[tuple[int, dict[str, Any]]]:
    result: list[tuple[int, dict[str, Any]]] = []
    for row in db.execute("SELECT uid, data FROM players ORDER BY uid").fetchall():
        try:
            data = json.loads(row["data"])
            if isinstance(data, dict) and str(data.get("c") or "").strip():
                result.append((int(row["uid"]), data))
        except (ValueError, TypeError):
            continue
    return result


def find_player_by_country(code: str) -> tuple[int | None, dict[str, Any] | None]:
    normalized = str(code or "").strip().upper()
    if not normalized:
        return None, None
    row = db.execute(
        "SELECT uid, data FROM players WHERE country_code=?",
        (normalized,),
    ).fetchone()
    if not row:
        return None, None
    try:
        value = json.loads(row["data"])
        return int(row["uid"]), value if isinstance(value, dict) else None
    except (ValueError, TypeError):
        return None, None


def reset_season(actor_id: int | None = None) -> tuple[int, int]:
    """Return (new season number, released country count). Profiles are retained."""
    now = int(time.time())
    current = int(kget("season_number", "1") or "1")
    new_number = current + 1
    released = len(all_players())
    rows = db.execute("SELECT uid, data FROM players").fetchall()
    with db:
        for row in rows:
            try:
                data = json.loads(row["data"])
                if not isinstance(data, dict):
                    continue
                data["c"] = ""
                data["alive"] = True
                data.pop("last_country", None)
                db.execute(
                    "UPDATE players SET country_code=NULL, data=?, updated_at=? WHERE uid=?",
                    (json.dumps(data, ensure_ascii=False), now, int(row["uid"])),
                )
            except (ValueError, TypeError):
                continue
        db.execute(
            "INSERT INTO settings(key, value, updated_at) VALUES('season', 'wait', ?) "
            "ON CONFLICT(key) DO UPDATE SET value='wait', updated_at=excluded.updated_at",
            (now,),
        )
        db.execute(
            "INSERT INTO settings(key, value, updated_at) VALUES('season_number', ?, ?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
            (str(new_number), now),
        )
        db.execute(
            "INSERT INTO season_history(season_number, action, actor_id, details, created_at) VALUES(?, 'reset', ?, ?, ?)",
            (new_number, actor_id, json.dumps({"released_countries": released}, ensure_ascii=False), now),
        )
        db.execute(
            "INSERT INTO audit_log(actor_id, action, target, details, created_at) VALUES(?, 'season_reset', ?, ?, ?)",
            (actor_id, str(new_number), json.dumps({"released_countries": released}, ensure_ascii=False), now),
        )
    return new_number, released


init_db()
