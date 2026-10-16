# ⚔️ Burnt Kingdoms: World War 2 (1934)

ربات و مینی‌اپ تلگرام استراتژیک جنگ جهانی دوم (سال ۱۹۳۴).
این نسخه اختصاصی بر پایه نسخه Burnt Kingdoms توسعه یافته و شامل تمامی تغییرات، نقشه‌ها، پرچم‌های تاریخی، رهبران و ائتلاف‌های دوران جنگ جهانی دوم می‌باشد.

---

## 🌟 ویژگی‌های کلیدی

- 🗺️ **انتخاب دوگانه (کارت و نقشه تعاملی):**
  - امکان انتخاب کشور هم از طریق فهرست کارت‌های تاکتیکی با جستجوی زنده و فیلترها.
  - و هم از روی **نقشه تاکتیکی جهان (Interactive Map)** با کلیک مستقیم روی قلمرو کشورها.
- 🏛️ **پرچم‌ها و تصاویر تاریخی سال‌های ۱۹۳۴ و جنگ جهانی دوم:**
  - استفاده از پرچم‌های دوره ۱۹۳۴–۱۹۴۵ (آلمان رایش، بریتانیا، شوروی سوسیالیستی، ایتالیای پادشاهی، امپراتوری ژاپن، ایران دوره پهلوی و...).
  - تصاویر و پرتره‌های باکیفیت رهبران تاریخی (چرچیل، استالین، روزولت، دوگل، هیتلر، موسولینی، هیروهیتو، رضاشاه و...).
- ⚔️ **ائتلاف‌ها و احزاب سیاسی:**
  - **محور (Axis):** نشان فالکه و علامت ائتلاف محور
  - **متفقین (Allies):** نشان ستاره متفقین و ائتلاف آزادی
  - **کمینترن (Comintern):** داس و چکش سوسیالیسم بین‌الملل
  - **بدون جناح (Neutral):** نماد موازنه و بی‌طرفی
  - نشان‌های چهارگانه ایدئولوژی: فاشیسم / نازیسم، کمونیسم، دموکراسی پارلمانی، سلطنت و بدون جناح.
- 👤 **نمایش مشخصات تصاحب‌کننده و مالک:**
  - نمایش بلادرنگ نام و آیدی تلگرام بازیکنی که هر کشور را انتخاب کرده است، هم روی کارت و هم در پاپ‌آپ نقشه.
- ⏳ **اتاق آماده‌باش سیزن (Season Waiting Room):**
  - پنل وضعیت سیزن، وضعیت آمادگی ناوگان‌ها و شمارش معکوس آغاز درگیری‌ها.
- 🎵 **پخش‌کننده موسیقی نظامی و پس‌زمینه:**
  - موسیقی مارش ارکسترال با دکمه کنترل صدا، قطع/وصل و حفظ وضعیت کاربر.
- 📱 **واکنش‌گرا و سازگار کامل با Telegram Mini App:**
  - رابط کاربری مدرن تیره، نظامی و راست‌چین (RTL فارسی) با انیمیشن‌های روان و بدون نیاز به نصب نرم‌افزار جانبی.

---

## 📂 ساختار فایل‌ها

- `bot.py`: سرور اصلی ربات تلگرام (Aiogram 3) و وب‌سرور REST API (aiohttp) به همراه اعتبارسنجی ورود تلگرام و پایگاه داده SQLite.
- `game_data.py`: دیتابیس جامع بیش از ۴۰ کشور جنگ جهانی دوم، پرچم‌ها، پرتره رهبران، پایتخت‌ها، ائتلاف‌ها و ایدئولوژی‌ها.
- `index.html`: رابط کاربری تک‌صفحه‌ای غنی، نقشه تعاملی لایف‌لت، جستجوی زنده، پخش‌کننده موسیقی و استایل‌های نظامی تاکتیکی.
- `world_geo.json`: داده‌های جغرافیایی برای رندر نقشه جهانی.
- `requirements.txt`: نیازمندی‌های پایتون.
- `.env.example`: نمونه تنظیمات توکن، وب‌اپ و ادمین‌ها.

---

## 🚀 راهنمای راه‌اندازی

### ۱. نصب وابستگی‌ها
```bash
pip install -r requirements.txt
```

### ۲. تنظیم متغیرهای محیطی
یک فایل `.env` بسازید:
```bash
cp .env.example .env
```
و مقادیر زیر را در آن پر کنید:
```env
BOT_TOKEN=توکن_ربات_از_بات_فادر
WEBAPP_URL=https://your-domain.com
ADMINS=شناسه_عددی_ادمین
PORT=8080
```

### ۳. اجرا
```bash
python bot.py
```

---

## 🛠️ دستورات مدیریتی ربات تلگرام

- `/start`: ارسال دکمه ورود به Mini App جنگ جهانی دوم
- `/season wait`: تغییر وضعیت سیزن به «اتاق انتظار»
- `/season pick`: باز کردن مرحله «انتخاب کشور»
- `/season live`: فعال‌سازی رسمی «نبرد سیزن»
- `/status`: مشاهده فهرست کشورهای تصاحب شده و حاکمان آن‌ها
- `/reset <COUNTRY_CODE>`: آزادسازی یک کشور (مثال: `/reset DE`)



### Historical faction icon sources
- Fascism ideology icon: [National Fascist Party logo (Wikimedia Commons)](https://commons.wikimedia.org/wiki/File:National_Fascist_Party_logo.svg), historical Italian National Fascist Party emblem; the Commons page records a public-domain dedication by the uploader.
- Allied faction icon: [Insignia of the South East Asia Command (Wikimedia Commons)](https://commons.wikimedia.org/wiki/File:Insignia_of_the_South_East_Asia_Command.svg). This is a real Allied command insignia, not a universal logo for all Allied countries; there was no single universal Allied logo.


### Historical Italian Fascist Party emblem source
- Axis/fascism icon uses the Wikimedia Commons file [Flag of the PNF (National Fascist Party)](https://commons.wikimedia.org/wiki/File:Flag_of_the_PNF_(National_Fascist_Party).svg), a historical 1927–1943 Italian National Fascist Party design. It is used only as a historical faction/ideology identifier in the game.
- The world map data is bundled locally in `world_geo.json` and loaded only when the map view is opened; Leaflet Canvas and simplified geometry are used to improve mobile performance.
