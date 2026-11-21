# Burnt Kingdoms WW2 (1934) Bot & Server
import asyncio
import base64
import hashlib
import hmac
from html import escape as html_escape
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
WEBAPP_LINK = URL + ("&" if "?" in URL else "?") + "v=20261121wikimedia-only-flags" if URL else ""
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
    all_players, find_player_by_country, kget, kset, pdel, pget, pset, reset_season,
    sync_country_catalog, load_country_politics, save_country_politics
)
COUNTRIES = sync_country_catalog(COUNTRIES)

# Documented party / opposition flags. Where no period-appropriate party flag is
# verifiable, the UI deliberately says so instead of fabricating a historical flag.
REVOLUTION_FLAG_META = {
    "DE": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Communist_Party_of_Germany.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Communist_Party_of_Germany.svg", "label": "پرچم حزب کمونیست آلمان (KPD)"},
        "democracy": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Social_Democratic_Party_of_Germany.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Social_Democratic_Party_of_Germany.svg", "label": "پرچم حزب سوسیال‌دموکرات آلمان (SPD)"},
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_NSDAP_(1920%E2%80%931945).svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_NSDAP_(1920%E2%80%931945).svg", "label": "پرچم حزب ناسیونال‌سوسیالیست آلمان (۱۹۲۰ تا ۱۹۴۵)"}
    },
    "IT": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_National_Fascist_Party_(PNF).svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_National_Fascist_Party_(PNF).svg", "label": "پرچم حزب ملی فاشیست ایتالیا (PNF)"},
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Italian_Communist_Party.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Italian_Communist_Party.svg", "label": "پرچم حزب کمونیست ایتالیا؛ بازنمایی معاصر از نشان حزبی"}
    },
    "GB": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_British_Union_of_Fascists.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_British_Union_of_Fascists.svg", "label": "پرچم اتحادیه فاشیست‌های بریتانیا (۱۹۳۲ تا ۱۹۳۵)"}
    },
    "US": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Communist_Party_USA_Flag.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Communist_Party_USA_Flag.svg", "label": "پرچم حزب کمونیست آمریکا"}
    },
    "FR": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Proposed_flag_of_the_French_Communist_Party_(1936).svg", "source_url": "https://commons.wikimedia.org/wiki/File:Proposed_flag_of_the_French_Communist_Party_(1936).svg", "label": "طرح پیشنهادی پرچم حزب کمونیست فرانسه (۱۹۳۶؛ نه پرچم رسمی ۱۹۳۴)"}
    },
    "CN": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinese_soviet_flag.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Chinese_soviet_flag.svg", "label": "پرچم جمهوری شورایی چین (۱۹۳۱ تا ۱۹۳۴)"},
        "democracy": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Prior_Flag_of_the_Kuomintang.svg", "source_url": "https://commons.wikimedia.org/wiki/Blue_Sky_White_Sun", "label": "پرچم حزب کومینتانگ؛ نشان آسمان آبی و خورشید سفید"}
    },
    "ES": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Communist_Party_of_Spain_(1930s).svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Communist_Party_of_Spain_(1930s).svg", "label": "پرچم حزب کمونیست اسپانیا در دههٔ ۱۹۳۰"},
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Bandera_FE_JONS.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Bandera_FE_JONS.svg", "label": "پرچم فالانژ اسپانیا؛ نسخهٔ بازسازی‌شدهٔ ویکی‌مدیا"}
    },
    "BR": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Brasilian_Integralism_Flag.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Brasilian_Integralism_Flag.svg", "label": "پرچم جنبش انتگرالیسم برزیل (AIB)"}
    },
    "PT": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/National_Syndicalist_Movement.png", "source_url": "https://commons.wikimedia.org/wiki/File:National_Syndicalist_Movement.png", "label": "پرچم جنبش ملی‌سندیکالیستی پرتغال"}
    },
    "RO": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Iron_Guard_(Legion_of_the_Archangel_Michael_or_Legionary_Movement).svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Iron_Guard_(Legion_of_the_Archangel_Michael_or_Legionary_Movement).svg", "label": "پرچم گارد آهنین رومانی (جنبش لژیونری)"},
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_PCR.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_PCR.svg", "label": "بازسازی پرچم حزب کمونیست رومانی؛ نسخهٔ شناخته‌شده مربوط به دورهٔ پس از جنگ است"}
    },
    "AT": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Fatherland_Front_of_Austria.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Fatherland_Front_of_Austria.svg", "label": "پرچم جبهه میهن‌پرستان اتریش"}
    },
    "SE": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_Nationalsocialistiska_Arbetarpartiet.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_Nationalsocialistiska_Arbetarpartiet.svg", "label": "پرچم حزب کارگران ناسیونال‌سوسیالیست سوئد (از ۱۹۳۳)"}
    },
    "CL": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_National_Socialist_Movement_of_Chile.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_National_Socialist_Movement_of_Chile.svg", "label": "پرچم جنبش ملی‌سوسیالیست شیلی (۱۹۳۲ تا ۱۹۳۸)"}
    },
    "IE": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Irish_Blueshirts.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Irish_Blueshirts.svg", "label": "پرچم جنبش بلوز‌شرت‌های ایرلند در دههٔ ۱۹۳۰"},
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Communist_Party_of_Ireland.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Communist_Party_of_Ireland.svg", "label": "پرچم حزب کمونیست ایرلند"}
    },
    "NO": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_Nasjonal_Samling.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_Nasjonal_Samling.svg", "label": "پرچم حزب ناسیونال سام‌لینگ نروژ (۱۹۳۳ تا ۱۹۴۵)"}
    },
    "FI": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/IKLlippu.png", "source_url": "https://commons.wikimedia.org/wiki/File:IKLlippu.png", "label": "پرچم جنبش مردمی میهن‌پرست فنلاند (IKL؛ از ۱۹۳۲)"}
    },
    "DK": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/DNSAP-FlagV1.svg", "source_url": "https://commons.wikimedia.org/wiki/File:DNSAP-FlagV1.svg", "label": "پرچم حزب کارگران ناسیونال‌سوسیالیست دانمارک"}
    },
    "HU": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_Party_of_National_Unity_Hungary.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_Party_of_National_Unity_Hungary.svg", "label": "پرچم حزب وحدت ملی مجارستان؛ حزب حاکم دورهٔ گیولا گومبوش"}
    },
    "BG": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Bulgarian_National_Socialist_Workers_Party.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Bulgarian_National_Socialist_Workers_Party.svg", "label": "پرچم حزب کارگران ناسیونال‌سوسیالیست بلغارستان (تأسیس ۱۹۳۲)"},
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_Bulgarian_Communist_Party_-_%D0%91%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B0_%D0%9A%D0%BE%D0%BC%D1%83%D0%BD%D0%B8%D1%81%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0_%D0%9F%D0%B0%D1%80%D1%82%D0%B8%D1%8F_(%D0%91%D0%9A%D0%9F).svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_Bulgarian_Communist_Party_-_Българска_Комунистическа_Партия_(БКП).svg", "label": "پرچم حزب کمونیست بلغارستان (بازنمایی ویکی‌مدیا)"}
    },
    "CZ": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_KSC.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_KSC.svg", "label": "پرچم حزب کمونیست چکسلواکی"}
    },
    "NL": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_National_Socialist_Movement_in_the_Netherlands.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_National_Socialist_Movement_in_the_Netherlands.svg", "label": "پرچم جنبش ملی‌سوسیالیستی هلند (NSB؛ از ۱۹۳۱)"}
    },
    "BE": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_Verdinaso.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_Verdinaso.svg", "label": "پرچم جنبش ملی‌گرای اقتدارگرای وردیناسو"}
    },
    "JP": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Old_Japanese_Communist_Flag.gif", "source_url": "https://commons.wikimedia.org/wiki/File:Old_Japanese_Communist_Flag.gif", "label": "پرچم قدیمی حزب کمونیست ژاپن؛ تاریخ دقیق این نسخه مشخص نیست"}
    },
    "IN": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Communist_Party_of_India.jpg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Communist_Party_of_India.jpg", "label": "پرچم حزب کمونیست هند"},
        "democracy": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Indian_National_Congress_(1931%E2%80%931971).svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Indian_National_Congress_(1931%E2%80%931971).svg", "label": "پرچم کنگرهٔ ملی هند (از ۱۹۳۱)"}
    },
    "ZA": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_South_African_Communist_Party.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_South_African_Communist_Party.svg", "label": "پرچم حزب کمونیست آفریقای جنوبی"}
    },
    "AR": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_Fascist_Party_of_Argentina.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_Fascist_Party_of_Argentina.svg", "label": "بازسازی پرچم حزب فاشیست آرژانتین؛ تصویر بازسازی‌شده در ویکی‌مدیا"}
    },
    "PL": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_Oboz_Narodowo_Radykalny.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_Oboz_Narodowo_Radykalny.svg", "label": "نماد پرچمی اردوگاه ملی رادیکال لهستان؛ نسخهٔ ویکی‌مدیا، نه سند پرچم رسمی ۱۹۳۴"}
    },
    "CA": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Parti_National_Social_Chr%C3%A9tien.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Parti_National_Social_Chr%C3%A9tien.svg", "label": "پرچم حزب ملی‌سوسیالیست مسیحی کانادا؛ گروه سیاسی دههٔ ۱۹۳۰"}
    },
    "GR": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Greek_National_Socialist_party_flag.png", "source_url": "https://commons.wikimedia.org/wiki/File:Greek_National_Socialist_party_flag.png", "label": "پرچم حزب ملی‌سوسیالیست یونان (۱۹۳۲ تا ۱۹۴۳)"}
    },
    "IQ": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Iraqi_Communist_Party_(old).svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Iraqi_Communist_Party_(old).svg", "label": "نسخهٔ قدیمی پرچم حزب کمونیست عراق؛ حزب از ۱۹۳۴"}
    },
    "EG": {
        "democracy": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Wafd_Flag.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Wafd_Flag.svg", "label": "پرچم حزب وفد مصر؛ جنبش سیاسی مشروطه‌خواه و پارلمانی"}
    },
    "AU": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/A_de_facto_flag_used_by_the_CPA.svg", "source_url": "https://commons.wikimedia.org/wiki/File:A_de_facto_flag_used_by_the_CPA.svg", "label": "یکی از پرچم‌های مورد استفادهٔ حزب کمونیست استرالیا؛ حدود دهه‌های ۱۹۴۰ و ۱۹۵۰"}
    },
    "SK": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Hlinka_party_(1938%E2%80%931945)_variant_1.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Hlinka_party_(1938%E2%80%931945)_variant_1.svg", "label": "پرچم حزب مردم هlinka در اسلواکی (۱۹۳۸ تا ۱۹۴۵؛ متأخر نسبت به آغاز سناریو)"}
    },
    "LV": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Perkonkrusta_karogs.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Perkonkrusta_karogs.svg", "label": "پرچم سازمان ملی‌گرای پِرکُن‌کروستس لتونی؛ بازسازی بر پایهٔ توصیف تاریخی"}
    },
    "MZ": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_Concordia_Association.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_Concordia_Association.svg", "label": "پرچم انجمن کنکوردیا در منچوکوئو (۱۹۳۲ تا ۱۹۴۵)"}
    },
    "MN": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Mongolian_People%27s_Party_flag.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Mongolian_People%27s_Party_flag.svg", "label": "پرچم حزب مردم مغولستان؛ حزب تاریخی بنیان‌گذاری‌شده در ۱۹۲۱"}
    },
    "VE": {
        "democracy": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_Partido_liberal_de_Venezuela.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_Partido_liberal_de_Venezuela.svg", "label": "پرچم حزب لیبرال ونزوئلا"}
    },
    "HN": {
        "democracy": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Liberal_Party_of_Honduras_flag.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Liberal_Party_of_Honduras_flag.svg", "label": "پرچم حزب لیبرال هندوراس"},
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Partido_comunista_de_Honduras.png", "source_url": "https://commons.wikimedia.org/wiki/File:Partido_comunista_de_Honduras.png", "label": "نشان پرچمی حزب کمونیست هندوراس"}
    },
    "TR": {
        "democracy": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_CHF.jpg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_CHF.jpg", "label": "پرچم حزب جمهوری‌خواه خلق ترکیه؛ سند تصویری مربوط به ۱۹۳۳"}
    },
    "CO": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Bandera_del_Partido_Comunista_Colombiano.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Bandera_del_Partido_Comunista_Colombiano.svg", "label": "پرچم حزب کمونیست کلمبیا"},
        "democracy": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Bandera_del_Partido_Liberal_Colombiano.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Bandera_del_Partido_Liberal_Colombiano.svg", "label": "پرچم حزب لیبرال کلمبیا"}
    },
    "CR": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Bandera_Partido_Vanguardia_Popular_Costa_Rica.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Bandera_Partido_Vanguardia_Popular_Costa_Rica.svg", "label": "پرچم حزب پیشتاز خلق کاستاریکا؛ اصل پرچم از ۱۹۳۱"}
    },
    "SV": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Bandera_del_pcs.gif", "source_url": "https://commons.wikimedia.org/wiki/File:Bandera_del_pcs.gif", "label": "پرچم حزب کمونیست السالوادور"}
    },
    "GT": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Bandera_pgt.jpg", "source_url": "https://commons.wikimedia.org/wiki/File:Bandera_pgt.jpg", "label": "پرچم حزب کارگران گواتمالا؛ مربوط به دورهٔ بعدی و نه ۱۹۳۴"}
    },
    "UY": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Bandera_PCU.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Bandera_PCU.svg", "label": "پرچم حزب کمونیست اروگوئه"},
        "democracy": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_Colorado_Party_(Uruguay).svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_Colorado_Party_(Uruguay).svg", "label": "پرچم حزب کلرادو اروگوئه"}
    },
    "PE": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Bandera_del_Partit_Comunista_del_Per%C3%BA..png", "source_url": "https://commons.wikimedia.org/wiki/File:Bandera_del_Partit_Comunista_del_Per%C3%BA..png", "label": "پرچم حزب کمونیست پرو"}
    },
    "PH": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Communist_Party_of_the_Philippines.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Communist_Party_of_the_Philippines.svg", "label": "پرچم حزب کمونیست فیلیپین؛ این حزب در ۱۹۶۸ تأسیس شد و با دورهٔ آغازین ۱۹۳۴ هم‌زمان نیست"}
    },
    "BO": {
        "fascism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_FSB.png", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_FSB.png", "label": "پرچم فالانژ سوسیالیست بولیوی؛ جنبش از ۱۹۳۷"}
    },
    "LR": {
        "democracy": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/True_Whig_Party_flag.svg", "source_url": "https://commons.wikimedia.org/wiki/File:True_Whig_Party_flag.svg", "label": "پرچم حزب ویگ واقعی لیبریا"}
    },
    "YU": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Communist_Party_of_Yugoslavia_Flag_(1920%E2%80%931952).svg", "source_url": "https://commons.wikimedia.org/wiki/File:Communist_Party_of_Yugoslavia_Flag_(1920%E2%80%931952).svg", "label": "پرچم حزب کمونیست یوگسلاوی (۱۹۲۰ تا ۱۹۵۲)"}
    },
    "CP": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Chinese_soviet_flag.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Chinese_soviet_flag.svg", "label": "پرچم جمهوری شورایی چین؛ مرتبط با ساختار کمونیستی یان‌آن"}
    },
    "NP": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Communist_Party_of_Nepal_(Unified_Marxist-Leninist).svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Communist_Party_of_Nepal_(Unified_Marxist-Leninist).svg", "label": "پرچم حزب کمونیست نپال (تأسیس ۱۹۹۱؛ متأخر نسبت به سناریوی ۱۹۳۴)"}
    },
    "CU": {
        "communism": {"url": "https://commons.wikimedia.org/wiki/Special:FilePath/Flag_of_the_Communist_Party_of_Cuba.svg", "source_url": "https://commons.wikimedia.org/wiki/File:Flag_of_the_Communist_Party_of_Cuba.svg", "label": "پرچم حزب کمونیست کوبا (تأسیس ۱۹۶۵؛ متأخر نسبت به سناریوی ۱۹۳۴)"}
    }
}
# Preserve the scenario's original national flag, then overlay any persistent
# country-level political changes saved by previous deployments.
for _code, _country in COUNTRIES.items():
    _country.setdefault("base_flag_url", _country.get("flag_url") or "")
    if _code == "DE":
        # The German scenario's original local artwork contains a prohibited-era
        # emblem; revolution variants use the neutral national tricolour instead.
        _country["base_flag_url"] = "https://flagcdn.com/w320/de.png"

for _code, _politics in load_country_politics().items():
    if _code not in COUNTRIES or not isinstance(_politics, dict):
        continue
    for _key in (
        "government_type", "ideology", "regime_type", "regime_fa", "leader",
        "leader_fa", "leader_en", "leader_title", "leader_img", "leader_url",
        "revolution_used", "revolution_path", "revolution_previous_government", "ruling_party_fa", "desc",
        "revolution_at"
    ):
        if _key in _politics:
            COUNTRIES[_code][_key] = _politics[_key]
    if COUNTRIES[_code].get("revolution_used"):
        _government = str(COUNTRIES[_code].get("government_type", "democracy"))
        _flag_meta = REVOLUTION_FLAG_META.get(_code, {}).get(_government)
        COUNTRIES[_code]["flag_url"] = (_flag_meta or {}).get("url") or COUNTRIES[_code].get("base_flag_url") or ""

REVOLUTION_RULES = {
    "fascism": {
        "government_type": "fascism", "ideology": "fascism",
        "regime_type": "nationalist_fascist_state",
        "regime_fa": "حکومت ملی‌گرای فاشیستی",
        "party_fa": "حزب ملی‌گرا و فاشیست",
        "leader_prefix": "رهبر شورای ملی",
        "leader_title": "رهبر حزب ملی‌گرا"
    },
    "communism": {
        "government_type": "communism", "ideology": "communism",
        "regime_type": "communist_one_party_state",
        "regime_fa": "جمهوری سوسیالیستی تک‌حزبی",
        "party_fa": "حزب کمونیست",
        "leader_prefix": "رئیس شورای خلق",
        "leader_title": "دبیرکل حزب کمونیست"
    },
    "democracy": {
        "government_type": "democracy", "ideology": "democracy",
        "regime_type": "democratic_republic",
        "regime_fa": "جمهوری دموکراتیک",
        "party_fa": "حزب دموکراتیک",
        "leader_prefix": "رئیس‌جمهور",
        "leader_title": "رئیس‌جمهور"
    }
}
REVOLUTION_TRANSITIONS = {
    "monarchy": ("communism", "fascism", "democracy"),
    "fascism": ("communism", "democracy"),
    "communism": ("fascism", "democracy"),
    "democracy": ("communism", "fascism")
}
REVOLUTION_REQUIREMENTS = {
    "power": 75, "money": 80000, "satisfaction": 65,
    "food": 12000, "oil": 2500, "buildings": 2
}


def perform_revolution(uid, player, body):
    code = str(player.get("c") or "").strip().upper()
    country = COUNTRIES.get(code)
    target = str(body.get("target") or "").strip().lower()
    if not country or target not in REVOLUTION_RULES:
        return "مسیر انقلاب یا کشور انتخاب‌شده معتبر نیست."
    if country.get("revolution_used"):
        return "این کشور قبلاً یک‌بار انقلاب کرده است؛ امکان انقلاب دوباره وجود ندارد."
    current = str(country.get("government_type") or "democracy").lower()
    allowed = REVOLUTION_TRANSITIONS.get(current, ())
    if target not in allowed:
        return "این مسیر با ساختار سیاسی فعلی کشور سازگار نیست."
    buildings = player.get("buildings") if isinstance(player.get("buildings"), dict) else {}
    built_count = sum(max(0, safe_int(value)) for value in buildings.values())
    checks = {
        "power": safe_float(player.get("power")),
        "money": safe_float(player.get("money")),
        "satisfaction": safe_float(player.get("satisfaction")),
        "food": safe_float(player.get("food")),
        "oil": safe_float(player.get("oil")),
        "buildings": built_count
    }
    labels = {
        "power": "قدرت سیاسی", "money": "خزانه", "satisfaction": "رضایت عمومی",
        "food": "ذخیره غذا", "oil": "ذخیره نفت", "buildings": "ساختمان‌های اقتصادی"
    }
    missing = [
        f"{labels[key]}: حداقل {REVOLUTION_REQUIREMENTS[key]:,}"
        for key in REVOLUTION_REQUIREMENTS
        if checks[key] < REVOLUTION_REQUIREMENTS[key]
    ]
    if missing:
        return "شرایط انقلاب هنوز کامل نیست: " + "، ".join(missing)
    if safe_float(player.get("money")) < 50000 or safe_float(player.get("power")) < 35:
        return "خزانه یا قدرت سیاسی برای تأمین هزینه انقلاب کافی نیست."

    rule = REVOLUTION_RULES[target]
    country_name = str(country.get("name_fa") or code)
    country_name_en = str(country.get("name_en") or code)
    previous = current
    player["power"] = safe_float(player.get("power")) - 35
    player["money"] = safe_int(player.get("money")) - 50000
    player["food"] = safe_int(player.get("food")) - 5000
    player["oil"] = safe_int(player.get("oil")) - 1000
    player["satisfaction"] = max(0, safe_float(player.get("satisfaction")) - 8)

    new_leader = f"{rule['leader_prefix']} {country_name}"
    english_leaders = {"communism": "Chair of the People's Council", "fascism": "Leader of the National Council", "democracy": "President"}
    new_leader_en = f"{english_leaders[target]} of {country_name_en}"
    politics = {
        "government_type": rule["government_type"],
        "ideology": rule["ideology"],
        "regime_type": rule["regime_type"],
        "regime_fa": rule["regime_fa"],
        "leader": new_leader,
        "leader_fa": new_leader,
        "leader_en": new_leader_en,
        "leader_title": rule["leader_title"],
        "leader_img": f"/revolution-leader/{target}.svg",
        "leader_url": f"/revolution-leader/{target}.svg",
        "revolution_used": True,
        "revolution_path": target,
        "ruling_party_fa": rule["party_fa"],
        "revolution_previous_government": previous,
        "revolution_at": int(time.time())
    }
    politics["desc"] = (
        str(country.get("desc") or "").rstrip()
        + f" در جریان سیزن، انقلاب {rule['party_fa']} به پیروزی رسید؛ "
        + f"ساختار حکومت به {rule['regime_fa']} تغییر کرد و {new_leader} زمام امور را به دست گرفت."
    )
    save_country_politics(code, politics)
    country.update(politics)
    _flag_meta = REVOLUTION_FLAG_META.get(code, {}).get(target)
    country["flag_url"] = (_flag_meta or {}).get("url") or country.get("base_flag_url") or ""
    print(f"[revolution] country={code} from={previous} to={target} actor={uid}")
    return None



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
ECONOMY_LOAN_LIMIT = 150_000
EMBASSY_MONEY_COST = 5000
EMBASSY_POWER_COST = 5


def safe_int(value, default=0):
    try:
        if isinstance(value, bool):
            return default
        return int(value)
    except (TypeError, ValueError, OverflowError):
        return default


def same_user_pair(item, first, second):
    return {safe_int(item.get("from"), -1), safe_int(item.get("to"), -1)} == {safe_int(first, -2), safe_int(second, -2)}


def embassy_endpoint_uid(value):
    """Resolve numeric Telegram IDs (including legacy numeric strings) and country codes."""
    if isinstance(value, bool):
        return 0
    if isinstance(value, (int, float)):
        return safe_int(value) if float(value).is_integer() else 0
    raw = str(value or "").strip()
    if not raw:
        return 0
    try:
        numeric = float(raw)
        if numeric.is_integer():
            return int(numeric)
    except (TypeError, ValueError, OverflowError):
        pass
    found_uid, _ = find_player_by_country(raw.upper())
    return safe_int(found_uid)


def embassy_endpoint_code(item, side):
    keys = ("from_country", "from_code", "from") if side == "from" else ("to_country", "to_code", "to")
    for key in keys:
        value = item.get(key)
        if value is None or str(value).strip() == "":
            continue
        raw = str(value).strip()
        if embassy_endpoint_uid(raw) == 0:
            return raw.upper()
    uid = embassy_endpoint_uid(item.get(side + "_uid") or item.get(side))
    player = pget(uid) if uid else None
    return str((player or {}).get("c") or "").strip().upper()


def same_embassy_pair(item, first_uid, second_uid):
    first_uid, second_uid = safe_int(first_uid), safe_int(second_uid)
    raw_from = item.get("from_uid") or item.get("from") or item.get("from_country") or item.get("from_code")
    raw_to = item.get("to_uid") or item.get("to") or item.get("to_country") or item.get("to_code")
    endpoints = {embassy_endpoint_uid(raw_from), embassy_endpoint_uid(raw_to)}
    if endpoints == {first_uid, second_uid}:
        return True
    first, second = pget(first_uid) or {}, pget(second_uid) or {}
    codes = {str(first.get("c") or "").strip().upper(), str(second.get("c") or "").strip().upper()}
    record_codes = {embassy_endpoint_code(item, "from"), embassy_endpoint_code(item, "to")}
    return bool("" not in codes and codes == record_codes)


def active_embassy(item):
    status = str(item.get("status", "")).strip().lower()
    return status in {"active", "accepted", "approved", "established", "open"}


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
            player["vault"] = safe_int(player.get("vault")) + int(safe_int(player.get("vault")) * 0.001)
        daily_food_need = 150 + max(0, safe_int(player.get("infantry"))) // 3000
        next_food = safe_int(player.get("food")) + food_output - daily_food_need
        if next_food < 0:
            player["food"] = 0
            player["famine_days"] = safe_int(player.get("famine_days")) + 1
            player["satisfaction"] = max(0.0, safe_float(player.get("satisfaction")) - 10)
        else:
            player["food"] = next_food
            player["famine_days"] = 0
        daily_welfare_need = 2 + max(0, safe_int(player.get("infantry"))) // 150000
        player["satisfaction"] = max(0.0, min(100.0, safe_float(player.get("satisfaction")) + welfare * 0.5 - daily_welfare_need))
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
            interest = max(1, int(debt * 0.025))
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



def load_diplomacy():
    try:
        value = json.loads(kget("diplomacy_state", "{}") or "{}")
        return value if isinstance(value, dict) else {}
    except (ValueError, TypeError):
        return {}


def save_diplomacy(value):
    kset("diplomacy_state", json.dumps(value, ensure_ascii=False))


def diplomacy_state_for(uid):
    state = load_diplomacy()
    incoming, outgoing, relations, pacts_incoming, pacts_outgoing, money_incoming, money_outgoing = [], [], [], [], [], [], []
    current_uid = safe_int(uid)
    current_player = pget(current_uid) or {}
    current_code = str(current_player.get("c") or "").strip().upper()
    now = int(time.time())
    changed = False
    for item in state.get("embassies", []):
        from_raw = item.get("from_uid") or item.get("from") or item.get("from_country") or item.get("from_code")
        to_raw = item.get("to_uid") or item.get("to") or item.get("to_country") or item.get("to_code")
        from_uid, to_uid = embassy_endpoint_uid(from_raw), embassy_endpoint_uid(to_raw)
        from_code, to_code = embassy_endpoint_code(item, "from"), embassy_endpoint_code(item, "to")
        status = str(item.get("status", "")).strip().lower()
        is_from = from_uid == current_uid or (current_code and from_code == current_code)
        is_to = to_uid == current_uid or (current_code and to_code == current_code)
        if is_to and status == "pending":
            sender = pget(from_uid) or {}
            incoming.append({**item, "from": from_uid, "to": current_uid,
                "from_country": str(sender.get("c") or from_code).upper()})
        elif is_from and status == "pending":
            receiver = pget(to_uid) or {}
            outgoing.append({**item, "from": current_uid, "to": to_uid,
                "to_country": str(receiver.get("c") or to_code).upper()})
        elif (is_from or is_to) and active_embassy(item):
            other_uid = to_uid if is_from else from_uid
            other_code = to_code if is_from else from_code
            other = pget(other_uid) or {}
            other_code = str(other.get("c") or other_code or "").strip().upper()
            if item.get("pact_until") and safe_int(item.get("pact_until")) <= now:
                item.pop("pact_until", None)
                item.pop("pact_years", None)
                changed = True
            relations.append({"uid": other_uid, "country": other_code,
                "name": other.get("name") or other.get("username") or "فرمانروا",
                "pact_until": item.get("pact_until", 0), "pact_years": item.get("pact_years", 0)})
    for proposal in state.get("pacts", []):
        other_uid = safe_int(proposal.get("from")) if safe_int(proposal.get("to")) == safe_int(uid) else safe_int(proposal.get("to"))
        other = pget(other_uid) or {}
        if safe_int(proposal.get("to")) == safe_int(uid) and proposal.get("status") == "pending":
            pacts_incoming.append({**proposal, "from_country": other.get("c", "")})
        elif safe_int(proposal.get("from")) == safe_int(uid) and proposal.get("status") == "pending":
            pacts_outgoing.append({**proposal, "to_country": other.get("c", "")})
    for transfer in state.get("money_transfers", []):
        other_uid = safe_int(transfer.get("from")) if safe_int(transfer.get("to")) == safe_int(uid) else safe_int(transfer.get("to"))
        other = pget(other_uid) or {}
        if safe_int(transfer.get("to")) == safe_int(uid) and transfer.get("status") == "pending":
            money_incoming.append({**transfer, "from_country": other.get("c", "")})
        elif safe_int(transfer.get("from")) == safe_int(uid) and transfer.get("status") == "pending":
            money_outgoing.append({**transfer, "to_country": other.get("c", "")})
    if changed:
        save_diplomacy(state)
    return {"incoming": incoming, "outgoing": outgoing, "relations": relations,
        "pacts_incoming": pacts_incoming, "pacts_outgoing": pacts_outgoing,
        "money_incoming": money_incoming, "money_outgoing": money_outgoing,
        "war_open": kget("diplomacy_war_open", "0") == "1"}


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
            active_countries.append({
                "code": c, "uid": p_uid,
                "name_fa": COUNTRIES[c].get("name_fa", c),
                "name_en": COUNTRIES[c].get("name_en", c),
                "ruler": p_name or p_uname or COUNTRIES[c].get("leader_fa") or "فرمانروا",
                "username": p_uname,
                "faction": COUNTRIES[c].get("faction", "neutral"),
                "government_type": COUNTRIES[c].get("government_type", "democracy"),
                "regime_type": COUNTRIES[c].get("regime_type", ""),
                "regime_fa": COUNTRIES[c].get("regime_fa", "نوع حکومت ثبت نشده"),
                "flag_url": COUNTRIES[c].get("flag_url", ""),
                "base_flag_url": COUNTRIES[c].get("base_flag_url", ""),
                "revolution_flags": REVOLUTION_FLAG_META.get(c, {}),
                "leader_fa": COUNTRIES[c].get("leader_fa", ""),
                "leader_title": COUNTRIES[c].get("leader_title", ""),
                "leader_img": COUNTRIES[c].get("leader_img", ""),
                "ideology": COUNTRIES[c].get("ideology", ""),
                "revolution_used": bool(COUNTRIES[c].get("revolution_used", False)),
                "revolution_path": COUNTRIES[c].get("revolution_path", ""),
                "ruling_party_fa": COUNTRIES[c].get("ruling_party_fa", "")
            })

    return {
        "season": season,
        "p": player,
        "taken": taken_codes,
        "owners": owners,
        "active_countries": active_countries,
        "diplomacy": diplomacy_state_for(uid),
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


async def revolution_flag_handler(request):
    code = str(request.match_info.get("code") or "").upper()
    government = str(request.match_info.get("government") or "").lower()
    country = COUNTRIES.get(code)
    if not country or government not in REVOLUTION_RULES:
        return web.Response(status=404, text="Flag not found")
    flag_meta = REVOLUTION_FLAG_META.get(code, {}).get(government)
    target = (flag_meta or {}).get("url") or country.get("base_flag_url") or country.get("flag_url") or ""
    if target.startswith("static/"):
        target = "/" + target
    if not target:
        return web.Response(status=404, text="No documented flag available")
    raise web.HTTPFound(target)


async def revolution_leader_handler(request):
    government = str(request.match_info.get("government") or "").lower()
    if government not in REVOLUTION_RULES:
        return web.Response(status=404, text="Leader emblem not found")
    colors = {"communism": "#ef4444", "fascism": "#c49a43", "democracy": "#38bdf8"}
    color = colors[government]
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240">'
        '<circle cx="120" cy="120" r="112" fill="#0b1728" stroke="' + color + '" stroke-width="8"/>'
        '<circle cx="120" cy="84" r="38" fill="' + color + '" opacity=".9"/>'
        '<path d="M48 204c6-45 34-68 72-68s66 23 72 68" fill="' + color + '" opacity=".9"/>'
        '<path d="M32 218h176" stroke="#e2e8f0" stroke-opacity=".45" stroke-width="4"/>'
        '</svg>'
    )
    return web.Response(text=svg, content_type="image/svg+xml", headers={"Cache-Control": "public, max-age=3600"})


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


        elif action == "revolution":
            if not player or not player.get("c"):
                error = "ابتدا باید یک کشور انتخاب کنید."
            elif season != "live":
                error = "انقلاب فقط پس از آغاز رسمی سیزن قابل انجام است."
            elif player.get("alive", True) is False:
                error = "کشور شما از بازی خارج شده است."
            else:
                changed = apply_daily_economy(player)
                if player.get("alive", True) is False:
                    error = "کشور شما پس از محاسبه اقتصاد روزانه از بازی خارج شده است."
                else:
                    error = perform_revolution(uid, player, body)
                if error is None or changed:
                    pset(uid, player)

        elif action in ("embassy_request", "embassy_respond", "embassy_close", "diplomacy_transfer", "diplomacy_money_respond", "diplomacy_pact", "diplomacy_pact_respond"):
            if not player or not player.get("c"):
                error = "ابتدا باید کشور خود را انتخاب کنید."
            elif player.get("alive", True) is False:
                error = "کشور شما از بازی خارج شده است."
            else:
                dstate = load_diplomacy()
                dstate.setdefault("embassies", [])
                dstate.setdefault("pacts", [])
                now = int(time.time())
                if action == "embassy_request":
                    target_code = str(body.get("country", "")).upper()
                    target_uid, target = find_player_by_country(target_code)
                    if not target_uid or target_uid == uid or not target or target.get("alive", True) is False:
                        error = "کشور مقصد معتبر یا فعال نیست."
                    elif any(active_embassy(e) and same_embassy_pair(e, uid, target_uid) for e in dstate["embassies"]):
                        error = "سفارت متقابل با این کشور از قبل برقرار است."
                    elif any(str(e.get("status", "")).strip().lower() == "pending" and same_embassy_pair(e, uid, target_uid) for e in dstate["embassies"]):
                        error = "درخواست سفارت با این کشور قبلاً ارسال شده یا از طرف آن کشور منتظر پاسخ شماست."
                    else:
                        dstate["embassies"].append({"from": uid, "to": target_uid, "status": "pending", "created": now})
                        save_diplomacy(dstate)
                        # Embassy requests are delivered only through the in-app Announcements panel.
                        print(f"[embassy-request] from={uid} to={target_uid} status=pending")
                elif action == "embassy_close":
                    target_uid = safe_int(body.get("target_uid"))
                    target = pget(target_uid)
                    relation = next((e for e in dstate["embassies"]
                        if active_embassy(e) and same_embassy_pair(e, uid, target_uid)), None)
                    if not target_uid or target_uid == uid or not target or not relation:
                        error = "سفارت فعالی میان دو کشور پیدا نشد."
                    else:
                        relation["status"] = "closed"
                        relation["closed_at"] = now
                        relation["closed_by"] = uid
                        for proposal in dstate.get("pacts", []):
                            if same_user_pair(proposal, uid, target_uid) and proposal.get("status") == "pending":
                                proposal["status"] = "cancelled"
                                proposal["responded"] = now
                        for transfer in dstate.get("money_transfers", []):
                            if same_user_pair(transfer, uid, target_uid) and transfer.get("status") == "pending":
                                transfer["status"] = "cancelled"
                                transfer["responded"] = now
                        save_diplomacy(dstate)
                        if bot:
                            try:
                                await bot.send_message(target_uid, f"🏛 کشور {player.get('c')} سفارت متقابل را تعطیل کرد. پیمان‌ها و درخواست‌های در انتظار این رابطه نیز لغو شدند.")
                            except Exception as exc:
                                print(f"[embassy-close-notification-error] {exc}")
                elif action == "embassy_respond":
                    sender_uid = safe_int(body.get("from"))
                    decision = str(body.get("decision", ""))
                    req = next((e for e in dstate["embassies"] if embassy_endpoint_uid(e.get("from_uid") or e.get("from") or e.get("from_country") or e.get("from_code")) == safe_int(sender_uid) and embassy_endpoint_uid(e.get("to_uid") or e.get("to") or e.get("to_country") or e.get("to_code")) == safe_int(uid) and str(e.get("status", "")).strip().lower() == "pending"), None)
                    sender = pget(sender_uid) if req else None
                    if not req or decision not in ("accept", "decline"):
                        error = "درخواست سفارت معتبر نیست یا قبلاً پاسخ داده شده است."
                    elif decision == "decline":
                        req["status"] = "declined"
                        req["responded"] = now
                        save_diplomacy(dstate)
                        if bot:
                            try:
                                await bot.send_message(sender_uid, f"🏛 درخواست سفارت متقابل شما توسط کشور {player.get('c')} رد شد.")
                            except Exception as exc:
                                print(f"[embassy-decline-notification-error] {exc}")
                    elif not sender or safe_int(sender.get("money")) < EMBASSY_MONEY_COST or safe_int(player.get("money")) < EMBASSY_MONEY_COST or safe_int(sender.get("power")) < EMBASSY_POWER_COST or safe_int(player.get("power")) < EMBASSY_POWER_COST:
                        error = "برای تأسیس سفارت، هر دو کشور باید ۵٬۰۰۰ دلار و ۵ واحد قدرت سیاسی داشته باشند."
                    else:
                        sender["money"] -= EMBASSY_MONEY_COST
                        player["money"] -= EMBASSY_MONEY_COST
                        sender["power"] -= EMBASSY_POWER_COST
                        player["power"] -= EMBASSY_POWER_COST
                        pset(sender_uid, sender)
                        req["status"] = "active"
                        req["responded"] = now
                        save_diplomacy(dstate)
                        if bot:
                            try:
                                await bot.send_message(sender_uid, f"🏛 درخواست سفارت متقابل شما توسط کشور {player.get('c')} پذیرفته شد.")
                            except Exception as exc:
                                print(f"[embassy-response-notification-error] {exc}")
                elif action == "diplomacy_transfer":
                    target_uid = safe_int(body.get("target_uid"))
                    amount = safe_int(body.get("amount"))
                    note = str(body.get("note", "")).strip()[:300]
                    target = pget(target_uid)
                    relation = any(active_embassy(e) and same_embassy_pair(e, uid, target_uid) for e in dstate["embassies"])
                    if not target or target_uid == uid or target.get("alive", True) is False or safe_int(target.get("buildings", {}).get("bank")) < 1 or safe_int(player.get("buildings", {}).get("bank")) < 1:
                        error = "برای انتقال پول، هر دو کشور باید بانک فعال داشته باشند."
                    elif not relation:
                        error = "ابتدا باید سفارت متقابل برقرار شود."
                    elif not 1000 <= amount <= 100000 or safe_int(player.get("money")) < amount:
                        error = "مبلغ انتقال باید بین ۱٬۰۰۰ تا ۱۰۰٬۰۰۰ دلار و در حد موجودی خزانه باشد."
                    elif len(note) < 5:
                        error = "توضیح درخواست انتقال حداقل ۵ نویسه باشد."
                    elif any(x.get("status") == "pending" and safe_int(x.get("from")) == safe_int(uid) and safe_int(x.get("to")) == safe_int(target_uid) for x in dstate.get("money_transfers", [])):
                        error = "برای این کشور درخواست انتقال وجه در انتظار پاسخ دارید."
                    else:
                        dstate.setdefault("money_transfers", []).append({"from": uid, "to": target_uid, "amount": amount, "note": note, "status": "pending", "created": now})
                        save_diplomacy(dstate)
                        if bot:
                            try:
                                await bot.send_message(target_uid, f"💰 کشور {player.get('c')} درخواست انتقال {amount:,} دلار فرستاده است. برای تأیید یا رد، بخش اعلانات مینی‌اپ را باز کنید.")
                            except Exception as exc:
                                print(f"[money-transfer-notification-error] {exc}")
                elif action == "diplomacy_money_respond":
                    sender_uid = safe_int(body.get("from"))
                    decision = str(body.get("decision", ""))
                    transfer = next((x for x in dstate.get("money_transfers", []) if safe_int(x.get("from")) == safe_int(sender_uid) and safe_int(x.get("to")) == safe_int(uid) and x.get("status") == "pending"), None)
                    sender = pget(sender_uid) if transfer else None
                    amount = safe_int(transfer.get("amount")) if transfer else 0
                    if not transfer or decision not in ("accept", "decline") or not sender:
                        error = "درخواست انتقال وجه معتبر نیست یا قبلاً پاسخ داده شده است."
                    elif decision == "decline":
                        transfer["status"] = "declined"
                        transfer["responded"] = now
                        save_diplomacy(dstate)
                        if bot:
                            try:
                                await bot.send_message(sender_uid, f"💰 درخواست انتقال وجه شما توسط کشور {player.get('c')} رد شد.")
                            except Exception as exc:
                                print(f"[money-transfer-decline-notification-error] {exc}")
                    elif safe_int(sender.get("money")) < amount or safe_int(sender.get("buildings", {}).get("bank")) < 1 or safe_int(player.get("buildings", {}).get("bank")) < 1:
                        error = "موجودی فرستنده یا بانک یکی از دو کشور برای تکمیل انتقال کافی نیست."
                    else:
                        sender["money"] -= amount
                        player["money"] = safe_int(player.get("money")) + amount
                        pset(sender_uid, sender)
                        transfer["status"] = "accepted"
                        transfer["responded"] = now
                        save_diplomacy(dstate)
                        if bot:
                            try:
                                await bot.send_message(sender_uid, f"💰 انتقال {amount:,} دلار به کشور {player.get('c')} تأیید و انجام شد.")
                            except Exception as exc:
                                print(f"[money-transfer-accept-notification-error] {exc}")
                elif action == "diplomacy_pact":
                    target_uid = safe_int(body.get("target_uid"))
                    years = safe_int(body.get("years"))
                    note = str(body.get("note", "")).strip()[:500]
                    relation = next((e for e in dstate["embassies"] if active_embassy(e) and same_embassy_pair(e, uid, target_uid)), None)
                    target = pget(target_uid)
                    if not relation or not target or target.get("alive", True) is False or target_uid == uid or years not in (1, 2, 3, 5) or len(note) < 5:
                        error = "ابتدا سفارت برقرار کنید و مدت معتبر انتخاب کنید."
                    elif relation.get("pact_until") and safe_int(relation.get("pact_until")) > now:
                        error = "پیمان عدم تجاوز فعالی با این کشور دارید."
                    elif any(p.get("status") == "pending" and same_user_pair(p, uid, target_uid) for p in dstate["pacts"]):
                        error = "درخواست پیمان قبلاً ارسال شده و منتظر پاسخ است."
                    else:
                        dstate["pacts"].append({"from": uid, "to": target_uid, "years": years, "note": note, "status": "pending", "created": now})
                        save_diplomacy(dstate)
                        if bot:
                            try:
                                await bot.send_message(target_uid, f"📜 کشور {player.get('c')} پیشنهاد پیمان عدم تجاوز برای {years} سال فرستاده است. برای پذیرش یا رد، بخش اعلانات خانه را باز کنید.")
                            except Exception as exc:
                                print(f"[pact-notification-error] {exc}")
                elif action == "diplomacy_pact_respond":
                    sender_uid = safe_int(body.get("from"))
                    decision = str(body.get("decision", ""))
                    proposal = next((p for p in dstate["pacts"] if safe_int(p.get("from")) == safe_int(sender_uid) and safe_int(p.get("to")) == safe_int(uid) and p.get("status") == "pending"), None)
                    relation = next((e for e in dstate["embassies"] if e.get("status") == "active" and {e.get("from"), e.get("to")} == {uid, sender_uid}), None)
                    if not proposal or not relation or decision not in ("accept", "decline"):
                        error = "درخواست پیمان معتبر نیست یا قبلاً پاسخ داده شده است."
                    else:
                        proposal["status"] = "accepted" if decision == "accept" else "declined"
                        proposal["responded"] = now
                        if decision == "accept":
                            relation["pact_until"] = now + safe_int(proposal.get("years")) * 365 * 86400
                            relation["pact_years"] = safe_int(proposal.get("years"))
                        save_diplomacy(dstate)
                        if bot:
                            try:
                                status_text = "پذیرفته شد" if decision == "accept" else "رد شد"
                                await bot.send_message(sender_uid, f"📜 پیشنهاد پیمان عدم تجاوز شما توسط کشور {player.get('c')} {status_text}.")
                            except Exception as exc:
                                print(f"[pact-response-notification-error] {exc}")

                if error is None:
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


    @dp.message(Command("war"))
    async def cmd_war(msg: Message):
        if not is_admin(msg.from_user.id):
            return await msg.answer("شما دسترسی مدیریت ندارید.")
        parts = (msg.text or "").split()
        if len(parts) != 2 or parts[1].lower() not in ("open", "close"):
            return await msg.answer("استفاده: /war open یا /war close")
        opened = parts[1].lower() == "open"
        kset("diplomacy_war_open", "1" if opened else "0")
        await msg.answer("گزینه جنگ در پنل دیپلماسی فعال شد." if opened else "گزینه جنگ در پنل دیپلماسی غیرفعال شد.")

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
    app.router.add_get("/flag/{code}/{government}.svg", revolution_flag_handler)
    app.router.add_get("/revolution-leader/{government}.svg", revolution_leader_handler)
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
