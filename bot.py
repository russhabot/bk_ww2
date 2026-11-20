# Burnt Kingdoms WW2 (1934) Bot & Server
import asyncio
import base64
import hashlib
import hmac
import json
import os
import re
import time
from datetime import datetime
from zoneinfo import ZoneInfo
from urllib.parse import parse_qsl

from aiohttp import web
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import BufferedInputFile, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message, WebAppInfo
from dotenv import load_dotenv

# COUNTRY_CODES was removed from game_data.py and is not used by this bot.
# Import only symbols that the current game_data module actually exports.
from game_data import COUNTRIES, DEFAULT_MUSIC_URL, ECONOMY_BUILDINGS, FACTIONS, IDEOLOGIES


load_dotenv()

TOKEN = os.environ.get("BOT_TOKEN", "").strip()
URL = os.environ.get("WEBAPP_URL", "").strip().rstrip("/")
# Bump this value when publishing UI changes to avoid Telegram WebView caching the old Mini App.
WEBAPP_LINK = URL + ("&" if "?" in URL else "?") + "v=20261120g" if URL else ""
def parse_admin_ids():
    raw = (
        os.environ.get("ADMINS")
        or os.environ.get("ADMIN_IDS")
        or os.environ.get("ADMIN_ID")
        or ""
    )
    normalized = raw.replace(";", ",").replace("\\n", ",").replace("\\r", ",")
    values = []
    for part in normalized.split(","):
        values.extend(part.split())
    return {int(value) for value in values if value.isdigit()}


ADMIN_IDS = parse_admin_ids()


def is_admin(user_id):
    try:
        return int(user_id) in ADMIN_IDS
    except (TypeError, ValueError):
        return False
ANNOUNCE_CHANNEL = os.environ.get("ANNOUNCE_CHANNEL", "").strip()
PORT = int(os.environ.get("PORT", 8080))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
GEOJSON_PATH = os.path.join(BASE_DIR, "world_geo.json")
BACKGROUND_MUSIC_URL = os.environ.get("BACKGROUND_MUSIC_URL", DEFAULT_MUSIC_URL).strip()

# Mandatory channels that players must join
REQUIRED_CHANNELS = [
    {
        "id": "burnt_kingdoms",
        "username": "burnt_kingdoms",
        "name": "کانال رسمی Burnt Kingdoms",
        "link": "https://t.me/burnt_kingdoms",
        "desc": "اخبار، رویدادها و اطلاعیه‌های رسمی ستاد کل"
    },
    {
        "id": "bk_chatt",
        "username": "bk_chatt",
        "name": "گروه نبرد و گفتگوی جنگ جهانی دوم",
        "link": "https://t.me/bk_chatt",
        "desc": "مذاکرات دیپلماتیک و پیمان‌های نظامی فرماندهان"
    }
]

from database import (
    all_players, find_player_by_country, kget, kset, pdel, pget, pset, reset_season
)

# Start the current season workflow in the waiting room on its first launch.
if kget("season_default_migrated") is None:
    kset("season", "wait")
    kset("season_default_migrated", "1")
elif kget("season") is None:
    kset("season", "wait")

ACTION_LOCK = asyncio.Lock()


TEHRAN_TZ = ZoneInfo("Asia/Tehran")
ECONOMY_DAILY_FOOD_USE = 100
ECONOMY_TAX_AMOUNT = 35_000
ECONOMY_BANK_LIMIT = 250_000
ECONOMY_LOAN_LIMIT = 250_000


def safe_int(value, default=0):
    try:
        if isinstance(value, bool):
            return default
        return int(value)
    except (TypeError, ValueError, OverflowError):
        return default


def safe_float(value, default=0.0):
    try:
        if isinstance(value, bool):
            return default
        return float(value)
    except (TypeError, ValueError, OverflowError):
        return default


def starting_resources(code):
    profiles = {
        "DE": {"power":86,"money":85000,"income":6200,"infantry":620000,"satisfaction":72,"oil":18000,"food":42000},
        "IT": {"power":68,"money":59000,"income":4100,"infantry":390000,"satisfaction":69,"oil":8500,"food":31000},
        "JP": {"power":79,"money":71000,"income":5000,"infantry":500000,"satisfaction":73,"oil":8000,"food":36000},
        "GB": {"power":88,"money":101000,"income":6900,"infantry":450000,"satisfaction":76,"oil":32000,"food":56000},
        "US": {"power":100,"money":125000,"income":9500,"infantry":700000,"satisfaction":82,"oil":90000,"food":90000},
        "FR": {"power":82,"money":78000,"income":5200,"infantry":500000,"satisfaction":74,"oil":12000,"food":48000},
        "SU": {"power":96,"money":92000,"income":7000,"infantry":900000,"satisfaction":68,"oil":24000,"food":70000},
        "RU": {"power":96,"money":92000,"income":7000,"infantry":900000,"satisfaction":68,"oil":24000,"food":70000},
        "CN": {"power":60,"money":35000,"income":2200,"infantry":350000,"satisfaction":58,"oil":2000,"food":50000},
        "PL": {"power":64,"money":42000,"income":2600,"infantry":300000,"satisfaction":70,"oil":1000,"food":28000},
        "IR": {"power":50,"money":25000,"income":1700,"infantry":120000,"satisfaction":75,"oil":5000,"food":30000},
        "IN": {"power":57,"money":30000,"income":2100,"infantry":280000,"satisfaction":63,"oil":3500,"food":45000},
        "CA": {"power":58,"money":48000,"income":3300,"infantry":160000,"satisfaction":80,"oil":18000,"food":36000},
        "AU": {"power":48,"money":37000,"income":2400,"infantry":110000,"satisfaction":79,"oil":7000,"food":28000},
        "BR": {"power":45,"money":33000,"income":2100,"infantry":140000,"satisfaction":73,"oil":4000,"food":38000},
        "TR": {"power":52,"money":31000,"income":2000,"infantry":220000,"satisfaction":67,"oil":2500,"food":30000},
        "ES": {"power":49,"money":32000,"income":1900,"infantry":180000,"satisfaction":61,"oil":1500,"food":26000},
    }
    if code in profiles:
        return dict(profiles[code])
    seed = sum(ord(ch) for ch in str(code or "XX"))
    tier = 0.78 if seed % 5 == 0 else 0.64 if seed % 3 == 0 else 0.48
    faction = COUNTRIES.get(code, {}).get("faction")
    faction_boost = 1.04 if faction == "allies" else 1.02 if faction == "comintern" else 1 if faction == "axis" else 0.88
    return {
        "power": round((30 + seed % 38) * faction_boost),
        "money": round((16000 + (seed % 15) * 1800) * tier),
        "income": round((900 + (seed % 11) * 170) * tier),
        "infantry": round((45000 + (seed % 16) * 18000) * tier),
        "satisfaction": 55 + seed % 31,
        "oil": round((500 + (seed % 13) * 900) * tier),
        "food": round((8000 + (seed % 17) * 2100) * tier),
    }


def ensure_economy(player):
    if not player or not player.get("c"):
        return False
    base = starting_resources(str(player.get("c")).upper())
    changed = False
    defaults = {
        "money": base["money"],
        "income_base": base["income"],
        "power": base["power"],
        "infantry": base["infantry"],
        "oil": base["oil"],
        "food": base["food"],
        "satisfaction": safe_int(player.get("happy"), base["satisfaction"]),
        "buildings": {},
        "vault": 0,
        "loan": 0,
        "loan_original": 0,
        "tax_date": "",
        "economy_day": datetime.now(TEHRAN_TZ).date().toordinal(),
        "statement_history": [],
        "statement_strikes": 0,
        "statement_suspended_until": 0,
        "materials": {"gold": 0, "iron": 0, "coal": 0},
        "famine_days": 0,
        "unrest_days": 0,
        "elimination_reason": "",
    }
    for key, value in defaults.items():
        if key not in player:
            player[key] = value
            changed = True
    if not isinstance(player.get("buildings"), dict):
        player["buildings"] = {}
        changed = True
    if not isinstance(player.get("statement_history"), list):
        player["statement_history"] = []
        changed = True
    if not isinstance(player.get("materials"), dict):
        player["materials"] = {"gold": 0, "iron": 0, "coal": 0}
        changed = True
    for material in ("gold", "iron", "coal"):
        if material not in player["materials"]:
            player["materials"][material] = 0
            changed = True
    for key in ("famine_days", "unrest_days"):
        if key not in player:
            player[key] = 0
            changed = True
    player["satisfaction"] = max(0.0, min(100.0, safe_float(player.get("satisfaction"), base["satisfaction"])))
    return changed


def apply_daily_economy(player):
    if not player or not player.get("c") or player.get("alive") is False:
        return False
    changed = ensure_economy(player)
    today = datetime.now(TEHRAN_TZ).date().toordinal()
    last_day = safe_int(player.get("economy_day"), today)
    days = max(0, min(30, today - last_day))
    if days <= 0:
        return changed
    buildings = player.get("buildings", {})
    for _ in range(days):
        cash_income = safe_int(player.get("income_base"))
        food_output = 0
        welfare = 0.0
        materials = player.setdefault("materials", {"gold": 0, "iron": 0, "coal": 0})
        for key, count in buildings.items():
            data = ECONOMY_BUILDINGS.get(key)
            amount = max(0, safe_int(count))
            if not data or amount <= 0:
                continue
            cash_income += safe_int(data.get("income")) * amount
            food_output += safe_int(data.get("food")) * amount
            welfare += float(data.get("happy", 0)) * amount
            resource = data.get("resource")
            if resource == "oil":
                player["oil"] = safe_int(player.get("oil")) + safe_int(data.get("production")) * amount
            elif resource:
                materials[resource] = safe_int(materials.get(resource)) + safe_int(data.get("production")) * amount
        player["money"] = safe_int(player.get("money")) + cash_income
        if safe_int(buildings.get("bank")) > 0:
            player["vault"] = safe_int(player.get("vault")) + int(safe_int(player.get("vault")) * 0.005)
        daily_food_need = 100 + max(0, safe_int(player.get("infantry"))) // 5000
        next_food = safe_int(player.get("food")) + food_output - daily_food_need
        if next_food < 0:
            player["food"] = 0
            player["famine_days"] = safe_int(player.get("famine_days")) + 1
            player["satisfaction"] = max(0.0, safe_float(player.get("satisfaction")) - 10)
        else:
            player["food"] = next_food
            player["famine_days"] = 0
        player["satisfaction"] = max(0.0, min(100.0, safe_float(player.get("satisfaction")) + welfare * 0.5 - 2))
        if safe_float(player.get("satisfaction")) < 20:
            player["unrest_days"] = safe_int(player.get("unrest_days")) + 1
        else:
            player["unrest_days"] = 0
        # A country enters an inactive crisis state after three consecutive
        # daily settlements with famine or severe public unrest. Player data is retained.
        if safe_int(player.get("famine_days")) >= 3:
            player["alive"] = False
            player["elimination_reason"] = "famine"
        elif safe_int(player.get("unrest_days")) >= 3:
            player["alive"] = False
            player["elimination_reason"] = "public_unrest"
        debt = safe_int(player.get("loan"))
        if debt > 0:
            interest = max(1, int(debt * 0.005))
            payment = min(safe_int(player.get("money")), interest + max(1000, int(debt * 0.1)))
            player["money"] = max(0, safe_int(player.get("money")) - payment)
            player["loan"] = max(0, debt + interest - payment)
            if player["loan"] == 0:
                player["loan_original"] = 0
    player["economy_day"] = today
    changed = True
    return changed


def economy_action(player, action, body):
    ensure_economy(player)
    if action == "economy_build":
        key = str(body.get("id", ""))
        amount = safe_int(body.get("amount", 1))
        data = ECONOMY_BUILDINGS.get(key)
        if not data or not 1 <= amount <= 10:
            return "ساختمان یا تعداد انتخاب‌شده معتبر نیست."
        owned = safe_int(player["buildings"].get(key))
        if data.get("unique") and owned:
            return "هر کشور فقط یک بانک ملی می‌تواند داشته باشد."
        cost = safe_int(data.get("cost")) * amount
        if safe_int(player.get("money")) < cost:
            return "موجودی خزانه برای این ساخت‌وساز کافی نیست."
        player["money"] -= cost
        player["buildings"][key] = owned + amount
    elif action == "economy_tax":
        today = datetime.now(TEHRAN_TZ).date().isoformat()
        if player.get("tax_date") == today:
            return "مالیات امروز قبلاً دریافت شده است."
        player["tax_date"] = today
        player["money"] = safe_int(player.get("money")) + ECONOMY_TAX_AMOUNT
        player["satisfaction"] = max(0, safe_int(player.get("satisfaction")) - 4)
    elif action == "economy_bank":
        if safe_int(player.get("buildings", {}).get("bank")) < 1:
            return "برای استفاده از خدمات بانکی ابتدا بانک ملی بسازید."
        kind = str(body.get("kind", ""))
        amount = safe_int(body.get("amount"))
        if not 1000 <= amount <= ECONOMY_BANK_LIMIT:
            return "مبلغ باید بین ۱٬۰۰۰ تا ۲۵۰٬۰۰۰ دلار باشد."
        if kind == "deposit":
            if safe_int(player.get("money")) < amount:
                return "پول نقد کافی نیست."
            player["money"] -= amount
            player["vault"] = safe_int(player.get("vault")) + amount
        elif kind == "withdraw":
            if safe_int(player.get("vault")) < amount:
                return "موجودی سپرده کافی نیست."
            player["vault"] -= amount
            player["money"] = safe_int(player.get("money")) + amount
        elif kind == "loan":
            if safe_int(player.get("loan")) > 0:
                return "ابتدا وام فعلی را تسویه کنید."
            if amount > ECONOMY_LOAN_LIMIT:
                return f"حداکثر وام قابل دریافت {ECONOMY_LOAN_LIMIT:,}$ است."
            player["loan"] = amount
            player["loan_original"] = amount
            player["money"] = safe_int(player.get("money")) + amount
        elif kind == "repay":
            debt = safe_int(player.get("loan"))
            if debt <= 0:
                return "وام فعالی ندارید."
            payment = min(amount, debt)
            if safe_int(player.get("money")) < payment:
                return "پول نقد کافی نیست."
            player["money"] -= payment
            player["loan"] = debt - payment
            if player["loan"] == 0:
                player["loan_original"] = 0
        else:
            return "عملیات بانکی نامعتبر است."
    else:
        return "عملیات اقتصادی نامعتبر است."
    return None


def statement_violation(uid, player, reason, severe=False):
    player["statement_strikes"] = safe_int(player.get("statement_strikes")) + (2 if severe else 1)
    if player["statement_strikes"] >= 3:
        player["statement_suspended_until"] = int(time.time()) + 86400
        pset(uid, player)
        return "به‌دلیل تکرار تخلف، صدور بیانیه برای ۲۴ ساعت غیرفعال شد."
    pset(uid, player)
    return reason + " در صورت تکرار، امکان صدور بیانیه موقتاً محدود می‌شود."


async def publish_statement(uid, user, player, body):
    ensure_economy(player)
    now = int(time.time())
    suspended = safe_int(player.get("statement_suspended_until"))
    if suspended > now:
        hours = max(1, (suspended - now + 3599) // 3600)
        return f"صدور بیانیه موقتاً غیرفعال است؛ حدود {hours} ساعت دیگر دوباره تلاش کنید."
    text = str(body.get("text", "")).strip()
    if not 5 <= len(text) <= 850:
        return "متن بیانیه باید بین ۵ تا ۸۵۰ نویسه باشد."
    image_data = str(body.get("image", "")).strip()
    image_file = None
    if image_data:
        match = re.fullmatch(r"data:(image/(?:jpeg|png|webp));base64,([A-Za-z0-9+/=]+)", image_data)
        if not match:
            return "تصویر باید از نوع JPG، PNG یا WEBP باشد."
        try:
            raw = base64.b64decode(match.group(2), validate=True)
        except Exception:
            return "فایل تصویر قابل خواندن نیست."
        if not raw or len(raw) > 4 * 1024 * 1024:
            return "حجم تصویر باید کمتر از ۴ مگابایت باشد."
        extension = {"image/jpeg": "jpg", "image/png": "png", "image/webp": "webp"}[match.group(1)]
        image_file = BufferedInputFile(raw, filename=f"statement.{extension}")

    history = [
        item for item in player.get("statement_history", [])
        if safe_int(item.get("time")) > now - 86400
    ]
    digest = hashlib.sha256(text.casefold().encode("utf-8")).hexdigest()
    if any(item.get("hash") == digest for item in history):
        return statement_violation(uid, player, "این متن قبلاً ارسال شده است.", severe=True)
    last_time = max((safe_int(item.get("time")) for item in history), default=0)
    if last_time and now - last_time < 900:
        return statement_violation(uid, player, "بین دو بیانیه باید حداقل ۱۵ دقیقه فاصله باشد.")
    if len(history) >= 5:
        return statement_violation(uid, player, "سقف مجاز بیانیه روزانه ۵ مورد است.")
    if not bot or not ANNOUNCE_CHANNEL:
        return "ربات یا کانال اعلامی برای انتشار بیانیه تنظیم نشده است."

    country_name = COUNTRIES.get(player.get("c"), {}).get("name_fa", player.get("c"))
    caption = f"📢 بیانیه رسمی {country_name}\n\n{text}"
    try:
        if image_file:
            await bot.send_photo(ANNOUNCE_CHANNEL, photo=image_file, caption=caption)
        else:
            await bot.send_message(ANNOUNCE_CHANNEL, caption)
    except Exception as exc:
        print(f"[statement-delivery-error] {exc}")
        return "ارسال بیانیه انجام نشد؛ دسترسی ربات به کانال را بررسی کنید."
    history.append({"time": now, "hash": digest})
    player["statement_history"] = history
    player["statement_strikes"] = max(0, safe_int(player.get("statement_strikes")) - 1)
    pset(uid, player)
    return None



def auth(init_data):
    # Never accept a missing Telegram initData when a real bot token is configured.
    # The old fallback let unauthenticated requests act as the shared test user (1001).
    if not init_data:
        if TOKEN:
            return None
        return {"id": 1001, "first_name": "فرمانده آزمایشی", "username": "commander_dev"}

    # Tokenless mode is only for local UI development; it is not secure for public hosting.
    if not TOKEN:
        try:
            fields = dict(parse_qsl(init_data, keep_blank_values=True, max_num_fields=64))
            if "user" in fields:
                user = json.loads(fields["user"])
                return user if isinstance(user, dict) and str(user.get("id", "")).isdigit() else None
        except Exception:
            pass
        return {"id": 1001, "first_name": "فرمانده", "username": "commander"}

    try:
        fields = dict(parse_qsl(init_data, keep_blank_values=True, max_num_fields=64))
        received_hash = fields.pop("hash", "")
        if not received_hash:
            return None

        secret = hmac.new(b"WebAppData", TOKEN.encode("utf-8"), hashlib.sha256).digest()
        candidates = [fields]
        if "signature" in fields:
            candidates.append({k: v for k, v in fields.items() if k != "signature"})

        sep = chr(10)
        valid_hash = any(
            hmac.compare_digest(
                hmac.new(secret, sep.join(f"{k}={v}" for k, v in sorted(candidate.items())).encode("utf-8"), hashlib.sha256).hexdigest(),
                received_hash,
            )
            for candidate in candidates
        )

        if not valid_hash:
            return None

        if "user" in fields:
            return json.loads(fields["user"])
        return {"id": int(fields.get("id", 1001)), "first_name": "کاربر"}
    except Exception as exc:
        print("[auth-error]", exc)
        return None


async def check_user_membership(uid: int):
    # Local tokenless development is allowed; production fails closed.
    if not bot:
        return (not TOKEN), ([] if not TOKEN else REQUIRED_CHANNELS)
    if is_admin(uid):
        return True, []
    missing = []
    for ch in REQUIRED_CHANNELS:
        try:
            member = await bot.get_chat_member(chat_id=f"@{ch['username']}", user_id=uid)
            status = getattr(member, "status", "")
            is_member_flag = getattr(member, "is_member", True)
            if status not in ("creator", "administrator", "member") and not (status == "restricted" and is_member_flag):
                missing.append(ch)
        except Exception as e:
            print(f"[membership-check] @{ch['username']} for {uid}: {e}")
            missing.append(ch)
    return len(missing) == 0, missing


def get_api_state(uid, player, season, membership_info=None):
    players = all_players()
    active_countries = []
    taken_codes = []
    owners = {}

    for p_uid, p in players:
        c = str(p.get("c", "")).strip().upper()
        if not c or p.get("alive", True) is False:
            continue
        taken_codes.append(c)
        p_name = str(p.get("name", "")).strip()
        p_uname = str(p.get("username", "")).strip().lstrip("@")
        owners[c] = {"name": p_name or p_uname or "فرمانروا", "username": p_uname, "uid": p_uid}
        owners[c.lower()] = owners[c]
        if c in COUNTRIES:
            active_countries.append({"code": c, "name_fa": COUNTRIES[c].get("name_fa", c), "name_en": COUNTRIES[c].get("name_en", c), "ruler": p_name or p_uname or "فرمانروا", "username": p_uname, "faction": COUNTRIES[c].get("faction", "neutral")})

    return {
        "season": season,
        "p": player,
        "taken": taken_codes,
        "owners": owners,
        "active_countries": active_countries,
        "economy_buildings": ECONOMY_BUILDINGS,
        "bg_music": BACKGROUND_MUSIC_URL,
        "membership": membership_info or {"ok": True, "missing": [], "channels": REQUIRED_CHANNELS},
        "required_channels": REQUIRED_CHANNELS,
    }


async def health_handler(request):
    return web.json_response({"status": "ok", "app": "bk_ww2", "season": kget("season", "wait")})


async def options_handler(request):
    resp = web.Response(status=204)
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    resp.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return resp


async def index_handler(request):
    target = INDEX_PATH if os.path.exists(INDEX_PATH) else "index.html"
    if not os.path.exists(target):
        return web.Response(text="index.html not found on server", status=404)
    resp = web.FileResponse(target)
    resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, max-age=0"
    resp.headers["Pragma"] = "no-cache"
    resp.headers["Expires"] = "0"
    return resp


async def geojson_handler(request):
    target = GEOJSON_PATH if os.path.exists(GEOJSON_PATH) else "world_geo.json"
    if os.path.exists(target):
        return web.FileResponse(target)
    return web.json_response({"error": "world_geo.json not found"}, status=404)


async def catalog_handler(request):
    # Public, read-only game catalog. All UI surfaces use this single source of truth.
    return web.json_response({
        "countries": COUNTRIES,
        "factions": FACTIONS,
        "ideologies": IDEOLOGIES,
        "default_music": BACKGROUND_MUSIC_URL
    })


async def api_handler(request):
    try:
        body = await request.json()
    except Exception:
        body = {}

    action = request.match_info.get("a", "state")
    init_data = body.get("init", "")
    user = auth(init_data)
    if not user:
        return web.json_response({"err": "داده‌های ورود تلگرام نامعتبر است."}, status=401)

    uid = int(user.get("id", 1001))
    season = kget("season", "pick")

    # Check channels membership
    is_member, missing_channels = await check_user_membership(uid)
    membership_info = {"ok": is_member, "missing": missing_channels, "channels": REQUIRED_CHANNELS}

    if action == "check_membership":
        return web.json_response({
            "ok": is_member,
            "missing": missing_channels,
            "channels": REQUIRED_CHANNELS,
            "s": get_api_state(uid, pget(uid), season, membership_info)
        })

    if not is_member:
        return web.json_response({
            "err": "برای ورود به بازی باید در @burnt_kingdoms و @bk_chatt عضو باشید.",
            "must_join": True, "missing": missing_channels, "channels": REQUIRED_CHANNELS,
            "s": get_api_state(uid, pget(uid), season, membership_info)
        }, status=403)

    async with ACTION_LOCK:
        player = pget(uid)
        error = None

        if action == "state":
            if player and player.get("c"):
                changed = ensure_economy(player)
                changed = apply_daily_economy(player) or changed
                if changed:
                    pset(uid, player)

        elif action in ("economy_build", "economy_tax", "economy_bank"):
            if not player or not player.get("c"):
                error = "ابتدا باید یک کشور انتخاب کنید."
            elif player.get("alive", True) is False:
                error = "کشور شما به‌دلیل بحران اقتصادی یا اجتماعی از بازی خارج شده است."
            else:
                changed = apply_daily_economy(player)
                error = economy_action(player, action, body)
                if error is None or changed:
                    pset(uid, player)

        elif action == "statement":
            if not player or not player.get("c"):
                error = "ابتدا باید یک کشور انتخاب کنید."
            elif player.get("alive", True) is False:
                error = "کشور شما از بازی خارج شده و امکان صدور بیانیه ندارد."
            else:
                error = await publish_statement(uid, user, player, body)

        elif action in ("pick", "claim"):
            if season != "pick":
                phase_text = "سیزن در حالت انتظار است؛ انتخاب کشور هنوز فعال نشده." if season == "wait" else "سیزن شروع شده و انتخاب کشور بسته است."
                return web.json_response({"err": phase_text, "season_locked": True, "s": get_api_state(uid, player, season, membership_info)}, status=409)
            # Membership has already been enforced above.
            if not is_member:
                ch_names = " و ".join(f"@{ch['username']}" for ch in missing_channels)
                error = "برای انتخاب کشور و ورود به بازی، ابتدا باید در کانال‌های زیر عضو شوید:\n" + ch_names
                return web.json_response({
                    "err": error,
                    "must_join": True,
                    "missing": missing_channels,
                    "channels": REQUIRED_CHANNELS,
                    "s": get_api_state(uid, player, season, membership_info)
                })

            code = str(body.get("c", "") or body.get("country", "")).strip().upper()
            if not code or code not in COUNTRIES or COUNTRIES[code].get("selectable") == "no":
                error = "کد کشور نامعتبر است."
            elif player and player.get("c") and player.get("alive", True) is not False:
                error = "شما قبلاً کشور خود را انتخاب کرده‌اید."
            else:
                existing_uid, _ = find_player_by_country(code)
                if existing_uid:
                    error = "این کشور قبلاً توسط فرمانده دیگری تصاحب شده است."
                else:
                    first_name = user.get("first_name", "")
                    last_name = user.get("last_name", "")
                    full_name = f"{first_name} {last_name}".strip() or "فرمانده"
                    username = str(user.get("username", "")).strip().lstrip("@")

                    new_player = {
                        "c": code,
                        "name": full_name,
                        "username": username,
                        "alive": True,
                        "created_at": int(time.time())
                    }
                    ensure_economy(new_player)
                    pset(uid, new_player)
                    player = new_player

                    c_info = COUNTRIES.get(code, {})
                    c_name = c_info.get("name_fa", code)
                    fac_name = FACTIONS.get(c_info.get("faction", ""), {}).get("fa", "")
                    print(f"[PICK] {uid} claimed {code} ({c_name})")

                    if bot and ANNOUNCE_CHANNEL:
                        asyncio.create_task(send_channel_announcement(full_name, username, c_name, fac_name))

        return web.json_response({
            "ok": error is None,
            "s": get_api_state(uid, player, season, membership_info),
            "err": error
        })


async def announce_season_status(phase: str, season_number=None):
    """Publish season transitions to the configured main announcement channel."""
    if not bot or not ANNOUNCE_CHANNEL:
        return
    labels = {
        "wait": ("اتاق انتظار", "انتخاب کشور غیرفعال است."),
        "pick": ("مرحلهٔ انتخاب کشور", "فرماندهان می‌توانند کشور خود را انتخاب کنند."),
        "live": ("سیزن فعال", "مرحلهٔ انتخاب کشور بسته شده و سیزن آغاز شده است.")
    }
    title, detail = labels.get(phase, ("وضعیت نامشخص", ""))
    number = season_number if season_number is not None else kget("season_number", "1")
    message = (
        "<b>اطلاعیهٔ رسمی Burnt Kingdoms</b>\n\n"
        f"<b>سیزن شمارهٔ {number}</b>\n"
        f"وضعیت جدید: <b>{title}</b>\n"
        f"{detail}"
    )
    try:
        await bot.send_message(ANNOUNCE_CHANNEL, message, parse_mode="HTML")
        print(f"[season-announcement] published phase={phase} season={number}")
    except Exception as exc:
        print(f"[season-announcement-error] {exc}")


async def send_channel_announcement(name, username, country_name, faction_name):
    if not bot or not ANNOUNCE_CHANNEL:
        return
    try:
        user_tag = f"@{username}" if username else name
        text = f"[اعلان] <b>اعلان ستاد کل جنگ جهانی دوم</b>\n\nفرمانده <b>{user_tag}</b> رسماً زمام امور کشور <b>{country_name}</b> را در ائتلاف <b>{faction_name}</b> به دست گرفت!\n\n نیروها در حالت آماده‌باش قرار گرفتند."
        await bot.send_message(ANNOUNCE_CHANNEL, text, parse_mode="HTML")
    except Exception as exc:
        print("[announce-error]", exc)


bot = Bot(token=TOKEN) if TOKEN else None
dp = Dispatcher() if TOKEN else None


if dp:
    @dp.message(Command("start"))
    async def cmd_start(msg: Message):
        # Membership is checked immediately after the Mini App opens via /api/state.
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="ورود به کارزار جهانی دوم (Mini App)", web_app=WebAppInfo(url=WEBAPP_LINK))]
        ]) if URL else None
        await msg.answer(
            "⚔️ <b>به کارزار جهانی دوم ۱۹۳۴ خوش آمدید!</b>\n\nبا ورود به Mini App، عضویت شما در @burnt_kingdoms و @bk_chatt بررسی می‌شود. در صورت نیاز، پنجرهٔ عضویت نمایش داده خواهد شد.\n\nسناریو از ۱ ژانویهٔ ۱۹۳۴ آغاز می‌شود.",
            reply_markup=kb, parse_mode="HTML"
        )

    @dp.callback_query(F.data == "verify_membership")
    async def verify_membership_callback(call: CallbackQuery):
        is_member, _missing = await check_user_membership(call.from_user.id)
        if not is_member:
            await call.answer("هنوز عضویت در هر دو کانال تأیید نشده است.", show_alert=True)
            return
        await call.answer("عضویت تأیید شد.")
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="ورود به کارزار جهانی دوم (Mini App)", web_app=WebAppInfo(url=WEBAPP_LINK))]
        ]) if URL else None
        if call.message:
            await call.message.answer("✅ عضویت تأیید شد. اکنون می‌توانید وارد بازی شوید.", reply_markup=kb)

    @dp.message(Command("season"))
    async def cmd_season(msg: Message):
        if not is_admin(msg.from_user.id):
            return await msg.answer("شما دسترسی مدیریت ندارید.")
        p = (msg.text or "").split()
        labels = {"wait": "اتاق انتظار؛ انتخاب کشور بسته", "pick": "انتخاب کشور باز", "live": "سیزن فعال؛ انتخاب کشور بسته"}
        if len(p) < 2:
            current = kget("season", "wait")
            number = kget("season_number", "1")
            return await msg.answer(
                f"سیزن شمارهٔ {number}\nوضعیت فعلی: {labels.get(current, current)}\n"
                "دستورات: /season wait | /season pick | /season live | /season reset"
            )
        if p[1].lower() in ("reset", "restart"):
            number, released = reset_season(msg.from_user.id)
            await announce_season_status("wait", number)
            return await msg.answer(
                f"سیزن ریست شد.\nشمارهٔ سیزن جدید: {number}\n"
                f"کشورهای آزادشده: {released}\nوضعیت جدید: اتاق انتظار.\n"
                "پروفایل بازیکنان حفظ شد؛ انتخاب کشور پس از /season pick فعال می‌شود."
            )
        phase = p[1].lower()
        if phase not in labels:
            return await msg.answer("استفاده: /season wait | /season pick | /season live | /season reset")
        previous = kget("season", "wait")
        if previous == phase:
            return await msg.answer(f"وضعیت سیزن از قبل «{labels[phase]}» است؛ تغییری انجام نشد.")
        kset("season", phase)
        await announce_season_status(phase)
        await msg.answer(f"وضعیت سیزن تغییر کرد: {labels[phase]}.")

    @dp.message(Command("resetseason"))
    async def cmd_resetseason(msg: Message):
        if msg.from_user.id not in ADMIN_IDS:
            return await msg.answer("شما دسترسی مدیریت ندارید.")
        number, released = reset_season(msg.from_user.id)
        await announce_season_status("wait", number)
        await msg.answer(
            f"سیزن ریست شد.\nشمارهٔ جدید: {number}\nکشورهای آزادشده: {released}\n"
            "وضعیت: اتاق انتظار. پروفایل بازیکنان حفظ شد."
        )

    @dp.message(Command("status"))
    async def cmd_status(msg: Message):
        pl = all_players()
        lines = [f"[آمار] <b>آمار سیزن:</b> {len(pl)} از {sum(1 for c in COUNTRIES.values() if c.get('selectable') != 'no')} کشور تصاحب شده"]
        for uid, p in pl:
            code = p.get("c", "")
            c_name = COUNTRIES.get(code, {}).get("name_fa", code)
            ruler = p.get("name") or (f"@{p.get('username')}" if p.get('username') else str(uid))
            lines.append(f"• <b>{c_name}</b>: {ruler}")
        await msg.answer(chr(10).join(lines), parse_mode="HTML")

    @dp.message(Command("reset"))
    async def cmd_reset(msg: Message):
        if msg.from_user.id not in ADMIN_IDS:
            return await msg.answer("شما دسترسی مدیریت ندارید.")
        p = msg.text.split()
        if len(p) < 2:
            return await msg.answer("استفاده: /reset [کد کشور مانند DE یا شناسه عددی]")
        t = p[1].strip().upper()
        uid, _ = find_player_by_country(t)
        if uid:
            pdel(uid)
            return await msg.answer(f"[تأیید] کشور {t} آزاد شد.")
        if t.isdigit():
            pdel(int(t))
            return await msg.answer(f"[تأیید] کاربر {t} ریست شد.")
        await msg.answer("کشور یا کاربری یافت نشد.")


async def economy_scheduler():
    """Apply one civilian-economy settlement per Tehran calendar day."""
    while True:
        try:
            async with ACTION_LOCK:
                for uid, player in all_players():
                    if apply_daily_economy(player):
                        pset(uid, player)
        except Exception as exc:
            print(f"[economy-scheduler-error] {exc}")
        await asyncio.sleep(60)


async def safe_bot_polling():
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except asyncio.CancelledError:
        raise
    except Exception as exc:
        # A second process may own getUpdates (common when testing locally).
        # Keep the web API alive: outbound channel posts still use the Bot API.
        print(f"[bot-polling-error] {exc}")


async def main():
    economy_task = asyncio.create_task(economy_scheduler())
    polling_task = None
    app = web.Application(client_max_size=6 * 1024 * 1024)
    app.router.add_get("/health", health_handler)
    app.router.add_get("/api/catalog", catalog_handler)
    app.router.add_get("/", index_handler)
    static_dir = os.path.join(BASE_DIR, "static")
    if os.path.isdir(static_dir):
        app.router.add_static("/static/", static_dir, name="static")

    app.router.add_get("/world_geo.json", geojson_handler)
    app.router.add_route("OPTIONS", "/api/{a}", options_handler)
    app.router.add_post("/api/{a}", api_handler)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)

    try:
        await site.start()
        print(f"[*] WW2 Web server running on http://0.0.0.0:{PORT}")

        if bot and dp:
            try:
                bot_me = await bot.get_me()
                print(f"[*] Telegram Bot @{bot_me.username} connected successfully!")
            except Exception as exc:
                print(f"[bot-connection-warning] {exc}")
            polling_task = asyncio.create_task(safe_bot_polling())
        else:
            print("[*] Running in standalone web server mode (No BOT_TOKEN configured)")

        # Keep the web app and outbound statement publishing alive even if
        # Telegram polling is already running in another test process.
        await asyncio.Event().wait()
    finally:
        if polling_task:
            polling_task.cancel()
            try:
                await polling_task
            except asyncio.CancelledError:
                pass
        economy_task.cancel()
        try:
            await economy_task
        except asyncio.CancelledError:
            pass
        await runner.cleanup()
        if bot:
            await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
