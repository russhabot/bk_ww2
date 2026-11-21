"""Persistent database layer for Burnt Kingdoms WW2.

Uses PostgreSQL when DATABASE_URL is configured (recommended for Railway).
Falls back to SQLite for local development. PostgreSQL is the durable production
store; its schema is created idempotently on application startup.
"""
from __future__ import annotations

import json
import os
import sqlite3
import time
from pathlib import Path
from typing import Any

DATABASE_URL = os.environ.get("DATABASE_URL", "").strip()
USE_POSTGRES = bool(DATABASE_URL)

if USE_POSTGRES:
    import psycopg
    from psycopg.rows import dict_row

    # Railway private-network URLs do not require SSL; psycopg uses the URL's
    # sslmode if one is explicitly supplied.
    db = psycopg.connect(DATABASE_URL, row_factory=dict_row, connect_timeout=15)
else:
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


def _execute(sql: str, params: tuple = ()):
    """Execute portable parameterized SQL on the selected backend."""
    if USE_POSTGRES:
        sql = sql.replace("?", "%s")
    return db.execute(sql, params)


def _table_exists(name: str) -> bool:
    if USE_POSTGRES:
        return _execute(
            "SELECT 1 FROM information_schema.tables WHERE table_schema=current_schema() AND table_name=?",
            (name,),
        ).fetchone() is not None
    return _execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)
    ).fetchone() is not None


def _columns(name: str) -> set[str]:
    if USE_POSTGRES:
        rows = _execute(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_schema=current_schema() AND table_name=?",
            (name,),
        ).fetchall()
        return {row["column_name"] for row in rows}
    return {row["name"] for row in _execute(f"PRAGMA table_info({name})").fetchall()}


def init_db() -> None:
    if USE_POSTGRES:
        _execute("""
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL,
                updated_at BIGINT NOT NULL
            )
        """)
        _execute("""
            CREATE TABLE IF NOT EXISTS players (
                uid BIGINT PRIMARY KEY,
                country_code TEXT UNIQUE,
                data TEXT NOT NULL,
                created_at BIGINT NOT NULL,
                updated_at BIGINT NOT NULL
            )
        """)
        _execute("""
            CREATE TABLE IF NOT EXISTS country_catalog (
                country_code TEXT PRIMARY KEY,
                government_type TEXT NOT NULL,
                data TEXT NOT NULL,
                updated_at BIGINT NOT NULL
            )
        """)
        _execute("""
            CREATE TABLE IF NOT EXISTS season_history (
                id BIGSERIAL PRIMARY KEY,
                season_number BIGINT NOT NULL,
                action TEXT NOT NULL,
                actor_id BIGINT,
                details TEXT NOT NULL DEFAULT '{}',
                created_at BIGINT NOT NULL
            )
        """)
        _execute("""
            CREATE TABLE IF NOT EXISTS audit_log (
                id BIGSERIAL PRIMARY KEY,
                actor_id BIGINT,
                action TEXT NOT NULL,
                target TEXT,
                details TEXT NOT NULL DEFAULT '{}',
                created_at BIGINT NOT NULL
            )
        """)
        _execute("CREATE INDEX IF NOT EXISTS idx_players_country ON players(country_code)")
        _execute("CREATE INDEX IF NOT EXISTS idx_season_history_number ON season_history(season_number)")
        now = int(time.time())
        _execute(
            "INSERT INTO settings(key, value, updated_at) VALUES(?, ?, ?) ON CONFLICT(key) DO NOTHING",
            ("season", "wait", now),
        )
        _execute(
            "INSERT INTO settings(key, value, updated_at) VALUES(?, ?, ?) ON CONFLICT(key) DO NOTHING",
            ("season_number", "1", now),
        )
        _execute(
            "INSERT INTO settings(key, value, updated_at) VALUES(?, ?, ?) ON CONFLICT(key) DO NOTHING",
            ("schema_version", "3", now),
        )
        db.commit()
        print("[database] PostgreSQL connected; schema ready")
        return

    # SQLite path retained for local development and legacy local databases.
    if _table_exists("players") and not {"uid", "data", "country_code"}.issubset(_columns("players")):
        if not _table_exists("players_legacy"):
            _execute("ALTER TABLE players RENAME TO players_legacy")
        else:
            _execute("DROP TABLE players")
    _execute("""
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY, value TEXT NOT NULL, updated_at INTEGER NOT NULL
        )
    """)
    _execute("""
        CREATE TABLE IF NOT EXISTS players (
            uid INTEGER PRIMARY KEY, country_code TEXT UNIQUE, data TEXT NOT NULL,
            created_at INTEGER NOT NULL, updated_at INTEGER NOT NULL
        )
    """)
    _execute("""
        CREATE TABLE IF NOT EXISTS country_catalog (
            country_code TEXT PRIMARY KEY,
            government_type TEXT NOT NULL,
            data TEXT NOT NULL,
            updated_at INTEGER NOT NULL
        )
    """)
    _execute("""
        CREATE TABLE IF NOT EXISTS season_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT, season_number INTEGER NOT NULL,
            action TEXT NOT NULL, actor_id INTEGER, details TEXT NOT NULL DEFAULT '{}',
            created_at INTEGER NOT NULL
        )
    """)
    _execute("""
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT, actor_id INTEGER, action TEXT NOT NULL,
            target TEXT, details TEXT NOT NULL DEFAULT '{}', created_at INTEGER NOT NULL
        )
    """)
    _execute("CREATE INDEX IF NOT EXISTS idx_players_country ON players(country_code)")
    _execute("CREATE INDEX IF NOT EXISTS idx_season_history_number ON season_history(season_number)")

    if _table_exists("kv"):
        for row in _execute("SELECT k, v FROM kv").fetchall():
            _execute(
                "INSERT OR IGNORE INTO settings(key, value, updated_at) VALUES(?, ?, ?)",
                (str(row["k"]), str(row["v"]), int(time.time())),
            )

    if _table_exists("players_legacy"):
        rows = _execute("SELECT uid, data FROM players_legacy").fetchall()
        for row in rows:
            try:
                data = json.loads(row["data"])
                if not isinstance(data, dict):
                    continue
                code = str(data.get("c") or "").strip().upper() or None
                if code and _execute("SELECT 1 FROM players WHERE country_code=?", (code,)).fetchone():
                    code = None
                    data["c"] = ""
                now = int(time.time())
                _execute(
                    "INSERT OR IGNORE INTO players(uid, country_code, data, created_at, updated_at) VALUES(?, ?, ?, ?, ?)",
                    (int(row["uid"]), code, json.dumps(data, ensure_ascii=False), int(data.get("created_at") or now), now),
                )
            except (ValueError, TypeError, json.JSONDecodeError):
                continue

    now = int(time.time())
    _execute("INSERT OR IGNORE INTO settings(key, value, updated_at) VALUES('season', 'wait', ?)", (now,))
    _execute("INSERT OR IGNORE INTO settings(key, value, updated_at) VALUES('season_number', '1', ?)", (now,))
    _execute("INSERT OR IGNORE INTO settings(key, value, updated_at) VALUES('schema_version', '3', ?)", (now,))
    db.commit()


def kget(key: str, default: Any = None) -> Any:
    row = _execute("SELECT value FROM settings WHERE key=?", (key,)).fetchone()
    return row["value"] if row else default


def kset(key: str, value: Any) -> None:
    _execute(
        "INSERT INTO settings(key, value, updated_at) VALUES(?, ?, ?) "
        "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
        (str(key), str(value), int(time.time())),
    )
    db.commit()


def pget(uid: int) -> dict[str, Any] | None:
    row = _execute("SELECT data FROM players WHERE uid=?", (int(uid),)).fetchone()
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
    _execute(
        "INSERT INTO players(uid, country_code, data, created_at, updated_at) VALUES(?, ?, ?, ?, ?) "
        "ON CONFLICT(uid) DO UPDATE SET country_code=excluded.country_code, data=excluded.data, updated_at=excluded.updated_at",
        (int(uid), code, payload, int(data.get("created_at") or now), now),
    )
    db.commit()


def sync_country_catalog(countries: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Persist the authoritative country catalog and return its database-backed records."""
    allowed = {"fascism", "communism", "monarchy", "democracy"}
    now = int(time.time())
    country_codes = []
    for raw_code, raw_country in countries.items():
        code = str(raw_code or "").strip().upper()
        if not code or not isinstance(raw_country, dict):
            continue
        government_type = str(raw_country.get("government_type") or "").strip().lower()
        if government_type not in allowed:
            raise ValueError(f"Invalid government_type for {code}: {government_type!r}")
        country = dict(raw_country)
        country["government_type"] = government_type
        _execute(
            "INSERT INTO country_catalog(country_code, government_type, data, updated_at) VALUES(?, ?, ?, ?) "
            "ON CONFLICT(country_code) DO UPDATE SET government_type=excluded.government_type, "
            "data=excluded.data, updated_at=excluded.updated_at",
            (code, government_type, json.dumps(country, ensure_ascii=False), now),
        )
        country_codes.append(code)
    db.commit()

    stored = {}
    for row in _execute("SELECT country_code, data FROM country_catalog ORDER BY country_code").fetchall():
        code = str(row["country_code"])
        if code not in country_codes:
            continue
        try:
            country = json.loads(row["data"])
        except (ValueError, TypeError):
            continue
        if isinstance(country, dict):
            stored[code] = country
    if len(stored) != len(country_codes):
        raise RuntimeError(f"Country catalog sync mismatch: expected {len(country_codes)}, got {len(stored)}")
    print(f"[database] Country catalog synced; {len(stored)} countries across 4 government tags")
    return stored


def pdel(uid: int) -> None:
    _execute("DELETE FROM players WHERE uid=?", (int(uid),))
    db.commit()


def all_players() -> list[tuple[int, dict[str, Any]]]:
    result: list[tuple[int, dict[str, Any]]] = []
    for row in _execute("SELECT uid, data FROM players ORDER BY uid").fetchall():
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
    row = _execute("SELECT uid, data FROM players WHERE country_code=?", (normalized,)).fetchone()
    if not row:
        return None, None
    try:
        value = json.loads(row["data"])
        if isinstance(value, dict) and value.get("alive", True) is False:
            return None, None
        return int(row["uid"]), value if isinstance(value, dict) else None
    except (ValueError, TypeError):
        return None, None


def reset_season(actor_id: int | None = None) -> tuple[int, int]:
    """Return (new season number, released country count). Profiles are retained."""
    now = int(time.time())
    current = int(kget("season_number", "1") or "1")
    new_number = current + 1
    released = len(all_players())
    rows = _execute("SELECT uid, data FROM players").fetchall()
    # psycopg connection context managers close the connection on exit.
    # Use transaction() for PostgreSQL so the shared connection remains usable
    # by subsequent bot commands and HTTP requests. SQLite keeps its normal context.
    transaction = db.transaction() if USE_POSTGRES else db
    with transaction:
        for row in rows:
            try:
                data = json.loads(row["data"])
                if not isinstance(data, dict):
                    continue
                data["c"] = ""
                data["alive"] = True
                data.pop("last_country", None)
                _execute(
                    "UPDATE players SET country_code=NULL, data=?, updated_at=? WHERE uid=?",
                    (json.dumps(data, ensure_ascii=False), now, int(row["uid"])),
                )
            except (ValueError, TypeError):
                continue
        _execute(
            "INSERT INTO settings(key, value, updated_at) VALUES('season', 'wait', ?) "
            "ON CONFLICT(key) DO UPDATE SET value='wait', updated_at=excluded.updated_at",
            (now,),
        )
        _execute(
            "INSERT INTO settings(key, value, updated_at) VALUES('season_number', ?, ?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
            (str(new_number), now),
        )
        _execute(
            "INSERT INTO season_history(season_number, action, actor_id, details, created_at) VALUES(?, 'reset', ?, ?, ?)",
            (new_number, actor_id, json.dumps({"released_countries": released}, ensure_ascii=False), now),
        )
        _execute(
            "INSERT INTO audit_log(actor_id, action, target, details, created_at) VALUES(?, 'season_reset', ?, ?, ?)",
            (actor_id, str(new_number), json.dumps({"released_countries": released}, ensure_ascii=False), now),
        )
    return new_number, released


init_db()
