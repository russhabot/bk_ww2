# Burnt Kingdoms WW2 (1934) Bot & Server
import asyncio
import hashlib
import hmac
import json
import os
import sqlite3
import time
from urllib.parse import parse_qsl

from aiohttp import web
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message, WebAppInfo
from dotenv import load_dotenv

# COUNTRY_CODES was removed from game_data.py and is not used by this bot.
# Import only symbols that the current game_data module actually exports.
from game_data import COUNTRIES, DEFAULT_MUSIC_URL, FACTIONS, IDEOLOGIES


load_dotenv()

TOKEN = os.environ.get("BOT_TOKEN", "").strip()
URL = os.environ.get("WEBAPP_URL", "").strip().rstrip("/")
ADMIN_IDS = [int(x.strip()) for x in os.environ.get("ADMINS", "").split(",") if x.strip().isdigit()]
ANNOUNCE_CHANNEL = os.environ.get("ANNOUNCE_CHANNEL", "").strip()
PORT = int(os.environ.get("PORT", 8080))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
GEOJSON_PATH = os.path.join(BASE_DIR, "world_geo.json")
DB_PATH = os.environ.get("DB_PATH", os.path.join(BASE_DIR, "bk_ww2.db"))
# Ensure custom DB_PATH parent directories exist (e.g. /data/bk_ww2.db on a mounted volume).
os.makedirs(os.path.dirname(os.path.abspath(DB_PATH)), exist_ok=True)

BACKGROUND_MUSIC_URL = os.environ.get("BACKGROUND_MUSIC_URL", DEFAULT_MUSIC_URL).strip()

# Mandatory channels that players must join
REQUIRED_CHANNELS = [
    {
        "id": "Burnt_kingdoms",
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

db = sqlite3.connect(DB_PATH, check_same_thread=False)
db.execute("PRAGMA journal_mode = WAL;")
db.execute("CREATE TABLE IF NOT EXISTS kv (k TEXT PRIMARY KEY, v TEXT);")
db.execute("CREATE TABLE IF NOT EXISTS players (uid INTEGER PRIMARY KEY, data TEXT);")
db.commit()

ACTION_LOCK = asyncio.Lock()


def kget(key, default=None):
    row = db.execute("SELECT v FROM kv WHERE k=?", (key,)).fetchone()
    return row[0] if row else default


def kset(key, value):
    db.execute("INSERT INTO kv (k, v) VALUES (?, ?) ON CONFLICT(k) DO UPDATE SET v=excluded.v", (key, str(value)))
    db.commit()


def pget(uid):
    row = db.execute("SELECT data FROM players WHERE uid=?", (uid,)).fetchone()
    return json.loads(row[0]) if row else None


def pset(uid, data):
    db.execute("INSERT INTO players (uid, data) VALUES (?, ?) ON CONFLICT(uid) DO UPDATE SET data=excluded.data", (uid, json.dumps(data, ensure_ascii=False)))
    db.commit()


def pdel(uid):
    db.execute("DELETE FROM players WHERE uid=?", (uid,))
    db.commit()


def all_players():
    rows = db.execute("SELECT uid, data FROM players").fetchall()
    result = []
    for uid, raw in rows:
        try:
            result.append((uid, json.loads(raw)))
        except Exception:
            pass
    return result


def find_player_by_country(code):
    code = code.upper()
    for uid, p in all_players():
        if str(p.get("c", "")).upper() == code:
            return uid, p
    return None, None


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
    if uid in ADMIN_IDS:
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
    taken_codes = []
    owners = {}

    for p_uid, p in players:
        c = str(p.get("c", "")).strip().upper()
        if not c:
            continue
        taken_codes.append(c)
        p_name = str(p.get("name", "")).strip()
        p_uname = str(p.get("username", "")).strip().lstrip("@")
        owners[c] = {"name": p_name or p_uname or "فرمانروا", "username": p_uname, "uid": p_uid}
        owners[c.lower()] = owners[c]

    return {
        "season": season,
        "p": player,
        "taken": taken_codes,
        "owners": owners,
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
            pass

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
            elif player and player.get("c"):
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
                    pset(uid, new_player)
                    player = new_player

                    c_info = COUNTRIES.get(code, {})
                    c_name = c_info.get("name_fa", code)
                    fac_name = FACTIONS.get(c_info.get("faction", ""), {}).get("fa", "")
                    print(f"[PICK] {uid} claimed {code} ({c_name})")

                    if bot and ANNOUNCE_CHANNEL:
                        asyncio.create_task(send_channel_announcement(full_name, username, c_name, fac_name))

        return web.json_response({
            "s": get_api_state(uid, player, season, membership_info),
            "err": error
        })


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
        is_member, missing = await check_user_membership(msg.from_user.id)
        if not is_member:
            rows = [[InlineKeyboardButton(text=f"عضویت در {ch['name']}", url=ch["link"])] for ch in REQUIRED_CHANNELS]
            rows.append([InlineKeyboardButton(text="بررسی عضویت", callback_data="verify_membership")])
            await msg.answer(
                "⛔ <b>ورود به بازی قفل است.</b>\nبرای ورود باید در هر دو مورد زیر عضو باشید:\n• @burnt_kingdoms\n• @bk_chatt\n\nپس از عضویت، روی «بررسی عضویت» بزنید.",
                reply_markup=InlineKeyboardMarkup(inline_keyboard=rows), parse_mode="HTML"
            )
            return
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="ورود به کارزار جهانی دوم (Mini App)", web_app=WebAppInfo(url=URL))]
        ]) if URL else None
        await msg.answer(
            "⚔️ <b>به کارزار جهانی دوم ۱۹۳۴ خوش آمدید!</b>\n\nسناریو از ۱ ژانویهٔ ۱۹۳۴ آغاز می‌شود. رهبران و ساختار حکومت‌ها بر اساس همین تاریخ ثبت شده‌اند.\n\nمرحلهٔ سیزن توسط ادمین تعیین می‌شود: wait، pick یا live.",
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
            [InlineKeyboardButton(text="ورود به کارزار جهانی دوم (Mini App)", web_app=WebAppInfo(url=URL))]
        ]) if URL else None
        if call.message:
            await call.message.answer("✅ عضویت تأیید شد. اکنون می‌توانید وارد بازی شوید.", reply_markup=kb)

    @dp.message(Command("season"))
    async def cmd_season(msg: Message):
        if msg.from_user.id not in ADMIN_IDS:
            return await msg.answer("شما دسترسی مدیریت ندارید.")
        p = msg.text.split()
        labels = {"wait": "اتاق انتظار؛ انتخاب کشور بسته", "pick": "انتخاب کشور باز", "live": "سیزن فعال؛ انتخاب کشور بسته"}
        if len(p) < 2:
            current = kget("season", "wait")
            return await msg.answer(f"وضعیت فعلی سیزن: {labels.get(current, current)}\nتغییر با: /season wait یا /season pick یا /season live")
        if p[1] not in ("wait", "pick", "live"):
            return await msg.answer("استفاده: /season wait | pick | live")
        kset("season", p[1])
        await msg.answer(f"وضعیت سیزن تغییر کرد: {labels[p[1]]}.")

    @dp.message(Command("status"))
    async def cmd_status(msg: Message):
        pl = all_players()
        lines = [f"[آمار] <b>آمار سیزن:</b> {len(pl)} از {sum(1 for c in COUNTRIES.values() if c.get("selectable") != "no")} کشور تصاحب شده"]
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


async def main():
    app = web.Application()
    app.router.add_get("/health", health_handler)
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
            bot_me = await bot.get_me()
            print(f"[*] Telegram Bot @{bot_me.username} connected successfully!")
            # Do not swallow polling errors. TelegramConflictError means another process
            # is polling this token; exit visibly instead of leaving a web-only half-alive app.
            await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
        else:
            print("[*] Running in standalone web server mode (No BOT_TOKEN configured)")
            await asyncio.Event().wait()
    finally:
        await runner.cleanup()
        if bot:
            await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
