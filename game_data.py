# -*- coding: utf-8 -*-
"""
WW2 1930 Historical Countries, Factions, and Ideologies
Burnt Kingdoms WW2
"""


FACTIONS = {
    "axis": {
        "id": "axis",
        "fa": "محور",
        "en": "Axis Powers",
        "color": "#ef4444",
        "bg": "rgba(239, 68, 68, 0.15)",
        "desc": "متحدین محور (آلمان، ژاپن، ایتالیا و متحدانشان در اروپا و آسیا)"
    },
    "allies": {
        "id": "allies",
        "fa": "متفقین",
        "en": "Allies",
        "color": "#3b82f6",
        "bg": "rgba(59, 130, 246, 0.15)",
        "desc": "ائتلاف متفقین (بریتانیا، آمریکا، فرانسه، کشورهای مشترک‌المنافع و شوروی)"
    },
    "comintern": {
        "id": "comintern",
        "fa": "کمینترن",
        "en": "Comintern",
        "color": "#f97316",
        "bg": "rgba(249, 115, 22, 0.15)",
        "desc": "انترناسیونال کمونیستی به رهبری اتحاد جماهیر شوروی سوسیالیستی"
    },
    "neutral": {
        "id": "neutral",
        "fa": "غیرمتعهد / بی‌طرف",
        "en": "Non-Aligned",
        "color": "#94a3b8",
        "bg": "rgba(148, 163, 184, 0.15)",
        "desc": "کشورهای بی‌طرف، مستقل یا غیروابسته در توازن قوای جهانی"
    }
}

IDEOLOGIES = {
    "fascism": {
        "id": "fascism",
        "fa": "فاشیسم / نظامی‌گری",
        "en": "Fascism",
        "color": "#a855f7",
        "desc": "حکومت توتالیتر، اقتدارگرای نظامی و ناسیونالیسم افراطی"
    },
    "communism": {
        "id": "communism",
        "fa": "کمونیسم",
        "en": "Communism",
        "color": "#ef4444",
        "desc": "مارکسیسم-لنینیسم، اقتصاد متمرکز اشتراکی و تک‌حزبی"
    },
    "democracy": {
        "id": "democracy",
        "fa": "دموکراسی",
        "en": "Democracy",
        "color": "#38bdf8",
        "desc": "دموکراسی پارلمانی، حاکمیت قانون و اقتصاد بازار آزاد"
    },
    "neutral": {
        "id": "neutral",
        "fa": "پادشاهی / مستقل",
        "en": "Monarchy / Non-Aligned",
        "color": "#f59e0b",
        "desc": "سلطنت مشروطه، نظام‌های سنتی یا حکومت‌های موقت بی‌طرف"
    }
}

LEADER_FALLBACK = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48Y2lyY2xlIGN4PSI1MCIgY3k9IjUwIiByPSI0OCIgZmlsbD0iIzE3MjMzOCIgc3Ryb2tlPSIjZjZjODZiIiBzdHJva2Utd2lkdGg9IjMiLz48Y2lyY2xlIGN4PSI1MCIgY3k9IjM4IiByPSIxOCIgZmlsbD0iIzlhYWFjMiIvPjxwYXRoIGQ9Ik0yMiw4MiBRNTAsNTYgNzgsODIgWiIgZmlsbD0iIzlhYWFjMiIvPjxwb2x5Z29uIHBvaW50cz0iNTAsNjIgNTMsNzAgNjEsNzAgNTUsNzUgNTcsODMgNTAsNzggNDMsODMgNDUsNzUgMzksNzAgNDcsNzAiIGZpbGw9IiNmNmM4NmIiLz48L3N2Zz4="

COUNTRIES = {
  "DE": {
    "code": "DE",
    "name_fa": "آلمان (رایش سوم)",
    "name_en": "Germany",
    "faction": "axis",
    "ideology": "fascism",
    "leader": "آدولف هیتلر",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Hitler_portrait_crop.jpg/250px-Hitler_portrait_crop.jpg",
    "flag_url": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjAgODAiPjxyZWN0IHdpZHRoPSIxMjAiIGhlaWdodD0iODAiIGZpbGw9IiNkMDAwMDAiLz48Y2lyY2xlIGN4PSI2MCIgY3k9IjQwIiByPSIyNCIgZmlsbD0iI2ZmZmZmZiIvPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDYwLDQwKSByb3RhdGUoNDUpIiBmaWxsPSIjMDAwMDAwIj48cmVjdCB4PSItMyIgeT0iLTE4IiB3aWR0aD0iNiIgaGVpZ2h0PSIzNiIvPjxyZWN0IHg9Ii0xOCIgeT0iLTMiIHdpZHRoPSIzNiIgaGVpZ2h0PSI2Ii8+PHJlY3QgeD0iLTMiIHk9Ii0xOCIgd2lkdGg9IjE1IiBoZWlnaHQ9IjYiLz48cmVjdCB4PSItMyIgeT0iMTIiIHdpZHRoPSIxNSIgaGVpZ2h0PSI2IiB0cmFuc2Zvcm09InJvdGF0ZSgxODApIi8+PHJlY3QgeD0iMTIiIHk9Ii0zIiB3aWR0aD0iNiIgaGVpZ2h0PSIxNSIvPjxyZWN0IHg9Ii0xOCIgeT0iLTMiIHdpZHRoPSI2IiBoZWlnaHQ9IjE1IiB0cmFuc2Zvcm09InJvdGF0ZSgxODApIi8+PC9nPjwvc3ZnPg=="
  },
  "IT": {
    "code": "IT",
    "name_fa": "پادشاهی ایتالیا",
    "name_en": "Italy",
    "faction": "axis",
    "ideology": "fascism",
    "leader": "بنیتو موسولینی",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Mussolini_mezzobusto.jpg/250px-Mussolini_mezzobusto.jpg",
    "flag_url": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjAgODAiPjxyZWN0IHdpZHRoPSI0MCIgaGVpZ2h0PSI4MCIgZmlsbD0iIzAwOTI0NiIvPjxyZWN0IHg9IjQwIiB3aWR0aD0iNDAiIGhlaWdodD0iODAiIGZpbGw9IiNmZmZmZmYiLz48cmVjdCB4PSI4MCIgd2lkdGg9IjQwIiBoZWlnaHQ9IjgwIiBmaWxsPSIjY2UyYjM3Ii8+PHJlY3QgeD0iNTEiIHk9IjI4IiB3aWR0aD0iMTgiIGhlaWdodD0iMjQiIHJ4PSIzIiBmaWxsPSIjMDAzMzk5Ii8+PHJlY3QgeD0iNTMiIHk9IjMwIiB3aWR0aD0iMTQiIGhlaWdodD0iMjAiIHJ4PSIyIiBmaWxsPSIjY2UyYjM3Ii8+PHJlY3QgeD0iNTgiIHk9IjMwIiB3aWR0aD0iNCIgaGVpZ2h0PSIyMCIgZmlsbD0iI2ZmZmZmZiIvPjxyZWN0IHg9IjUzIiB5PSIzOCIgd2lkdGg9IjE0IiBoZWlnaHQ9IjQiIGZpbGw9IiNmZmZmZmYiLz48cGF0aCBkPSJNNTMsMjQgbDMsNCBsNCwtNCBsNCw0IGwzLC00IGwtMSw0IGgtMTIgeiIgZmlsbD0iI2Y1YjMwMCIvPjwvc3ZnPg=="
  },
  "JP": {
    "code": "JP",
    "name_fa": "امپراتوری ژاپن",
    "name_en": "Japan",
    "faction": "axis",
    "ideology": "fascism",
    "leader": "امپراتور هیروهیتو",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Hirohito_in_dress_uniform_%28cropped%29.jpg/250px-Hirohito_in_dress_uniform_%28cropped%29.jpg",
    "flag_url": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjAgODAiPjxyZWN0IHdpZHRoPSIxMjAiIGhlaWdodD0iODAiIGZpbGw9IiNmZmZmZmYiLz48ZyBmaWxsPSIjYmUwMDI5Ij48cG9seWdvbiBwb2ludHM9IjYwLDQwIC0yMCwyMCAtMjAsMTAiLz48cG9seWdvbiBwb2ludHM9IjYwLDQwIDEwLC0yMCAyMCwtMjAiLz48cG9seWdvbiBwb2ludHM9IjYwLDQwIDUwLC0yMCA3MCwtMjAiLz48cG9seWdvbiBwb2ludHM9IjYwLDQwIDEwMCwtMjAgMTEwLC0yMCIvPjxwb2x5Z29uIHBvaW50cz0iNjAsNDAgMTQwLDEwIDE0MCwyMCIvPjxwb2x5Z29uIHBvaW50cz0iNjAsNDAgMTQwLDQwIDE0MCw1MCIvPjxwb2x5Z29uIHBvaW50cz0iNjAsNDAgMTQwLDcwIDE0MCw4MCIvPjxwb2x5Z29uIHBvaW50cz0iNjAsNDAgMTEwLDEwMCAxMDAsMTAwIi8+PHBvbHlnb24gcG9pbnRzPSI2MCw0MCA3MCwxMDAgNTAsMTAwIi8+PHBvbHlnb24gcG9pbnRzPSI2MCw0MCAyMCwxMDAgMTAsMTAwIi8+PHBvbHlnb24gcG9pbnRzPSI2MCw0MCAtMjAsODAgLTIwLDcwIi8+PHBvbHlnb24gcG9pbnRzPSI2MCw0MCAtMjAsNTAgLTIwLDQwIi8+PGNpcmNsZSBjeD0iNjAiIGN5PSI0MCIgcj0iMTgiLz48L2c+PC9zdmc+"
  },
  "HU": {
    "code": "HU",
    "name_fa": "پادشاهی مجارستان",
    "name_en": "Hungary",
    "faction": "axis",
    "ideology": "fascism",
    "leader": "میکلوش هورتی",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Horthy_Mikl%C3%B3s_%281930s%29.jpg/250px-Horthy_Mikl%C3%B3s_%281930s%29.jpg",
    "flag_url": "https://flagcdn.com/w160/hu.png"
  },
  "RO": {
    "code": "RO",
    "name_fa": "پادشاهی رومانی",
    "name_en": "Romania",
    "faction": "axis",
    "ideology": "fascism",
    "leader": "یون آنتونسکو",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Ion_Antonescu_%281940s%29.jpg/250px-Ion_Antonescu_%281940s%29.jpg",
    "flag_url": "https://flagcdn.com/w160/ro.png"
  },
  "BG": {
    "code": "BG",
    "name_fa": "پادشاهی بلغارستان",
    "name_en": "Bulgaria",
    "faction": "axis",
    "ideology": "nonaligned",
    "leader": "تزار بوریس سوم",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Boris_III_of_Bulgaria.jpg/250px-Boris_III_of_Bulgaria.jpg",
    "flag_url": "https://flagcdn.com/w160/bg.png"
  },
  "FI": {
    "code": "FI",
    "name_fa": "جمهوری فنلاند",
    "name_en": "Finland",
    "faction": "axis",
    "ideology": "democracy",
    "leader": "کارل گوستاف مانرهایم",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Mannerheim_1940.jpg/250px-Mannerheim_1940.jpg",
    "flag_url": "https://flagcdn.com/w160/fi.png"
  },
  "TH": {
    "code": "TH",
    "name_fa": "پادشاهی تایلند (سیام)",
    "name_en": "Thailand",
    "faction": "axis",
    "ideology": "fascism",
    "leader": "پلاک فیبونسونگکرام",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Plaek_Phibunsongkhram_1941.jpg/250px-Plaek_Phibunsongkhram_1941.jpg",
    "flag_url": "https://flagcdn.com/w160/th.png"
  },
  "GB": {
    "code": "GB",
    "name_fa": "بریتانیای کبیر",
    "name_en": "United Kingdom",
    "faction": "allies",
    "ideology": "democracy",
    "leader": "وینستون چرچیل",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Sir_Winston_Churchill_-_19086236948_%28restored%29.jpg/250px-Sir_Winston_Churchill_-_19086236948_%28restored%29.jpg",
    "flag_url": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjAgODAiPjxyZWN0IHdpZHRoPSIxMjAiIGhlaWdodD0iODAiIGZpbGw9IiMwMTIxNjkiLz48cG9seWdvbiBwb2ludHM9IjAsMCAxMiwwIDEyMCw3MiAxMjAsODAgMTA4LDgwIDAsOCIgZmlsbD0iI2ZmZmZmZiIvPjxwb2x5Z29uIHBvaW50cz0iMTIwLDAgMTA4LDAgMCw3MiAwLDgwIDEyLDgwIDEyMCw4IiBmaWxsPSIjZmZmZmZmIi8+PHBvbHlnb24gcG9pbnRzPSIwLDAgNiwwIDEyMCw3NiAxMjAsODAgMTE0LDgwIDAsNCIgZmlsbD0iI2M4MTAyZSIvPjxwb2x5Z29uIHBvaW50cz0iMTIwLDAgMTE0LDAgMCw3NiAwLDgwIDYsODAgMTIwLDQiIGZpbGw9IiNjODEwMmUiLz48cmVjdCB4PSI0OCIgeT0iMCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjgwIiBmaWxsPSIjZmZmZmZmIi8+PHJlY3QgeD0iMCIgeT0iMjgiIHdpZHRoPSIxMjAiIGhlaWdodD0iMjQiIGZpbGw9IiNmZmZmZmYiLz48cmVjdCB4PSI1MiIgeT0iMCIgd2lkdGg9IjE2IiBoZWlnaHQ9IjgwIiBmaWxsPSIjYzgxMDJlIi8+PHJlY3QgeD0iMCIgeT0iMzIiIHdpZHRoPSIxMjAiIGhlaWdodD0iMTYiIGZpbGw9IiNjODEwMmUiLz48L3N2Zz4="
  },
  "US": {
    "code": "US",
    "name_fa": "ایالات متحده آمریکا",
    "name_en": "United States",
    "faction": "allies",
    "ideology": "democracy",
    "leader": "فرانکلین دی. روزولت",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/FDR-1944-Campaign-Portrait_%283x4_retouched%2C_cropped%29.jpg/250px-FDR-1944-Campaign-Portrait_%283x4_retouched%2C_cropped%29.jpg",
    "flag_url": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjAgODAiPjxyZWN0IHdpZHRoPSIxMjAiIGhlaWdodD0iODAiIGZpbGw9IiNiMjIyMzQiLz48cGF0aCBkPSJNMCw2LjE1IGgxMjAgdjYuMTUgaC0xMjAgeiBNMCwxOC40NiBoMTIwIHY2LjE1IGgtMTIwIHogTTAsMzAuNzcgaDEyMCB2Ni4xNSBoLTEyMCB6IE0wLDQzLjA4IGgxMjAgdjYuMTUgaC0xMjAgeiBNMCw1NS4zOCBoMTIwIHY2LjE1IGgtMTIwIHogTTAsNjcuNjkgaDEyMCB2Ni4xNSBoLTEyMCB6IiBmaWxsPSIjZmZmZmZmIi8+PHJlY3Qgd2lkdGg9IjUyIiBoZWlnaHQ9IjQzLjA4IiBmaWxsPSIjM2MzYjZlIi8+PGNpcmNsZSBjeD0iMTAiIGN5PSI4IiByPSIyLjUiIGZpbGw9IiNmZmYiLz48Y2lyY2xlIGN4PSIyMCIgY3k9IjgiIHI9IjIuNSIgZmlsbD0iI2ZmZiIvPjxjaXJjbGUgY3g9IjMwIiBjeT0iOCIgcj0iMi41IiBmaWxsPSIjZmZmIi8+PGNpcmNsZSBjeD0iNDAiIGN5PSI4IiByPSIyLjUiIGZpbGw9IiNmZmYiLz48Y2lyY2xlIGN4PSIxMCIgY3k9IjE4IiByPSIyLjUiIGZpbGw9IiNmZmYiLz48Y2lyY2xlIGN4PSIyMCIgY3k9IjE4IiByPSIyLjUiIGZpbGw9IiNmZmYiLz48Y2lyY2xlIGN4PSIzMCIgY3k9IjE4IiByPSIyLjUiIGZpbGw9IiNmZmYiLz48Y2lyY2xlIGN4PSI0MCIgY3k9IjE4IiByPSIyLjUiIGZpbGw9IiNmZmYiLz48Y2lyY2xlIGN4PSIxMCIgY3k9IjI4IiByPSIyLjUiIGZpbGw9IiNmZmYiLz48Y2lyY2xlIGN4PSIyMCIgY3k9IjI4IiByPSIyLjUiIGZpbGw9IiNmZmYiLz48Y2lyY2xlIGN4PSIzMCIgY3k9IjI4IiByPSIyLjUiIGZpbGw9IiNmZmYiLz48Y2lyY2xlIGN4PSI0MCIgY3k9IjI4IiByPSIyLjUiIGZpbGw9IiNmZmYiLz48Y2lyY2xlIGN4PSIxMCIgY3k9IjM4IiByPSIyLjUiIGZpbGw9IiNmZmYiLz48Y2lyY2xlIGN4PSIyMCIgY3k9IjM4IiByPSIyLjUiIGZpbGw9IiNmZmYiLz48Y2lyY2xlIGN4PSIzMCIgY3k9IjM4IiByPSIyLjUiIGZpbGw9IiNmZmYiLz48Y2lyY2xlIGN4PSI0MCIgY3k9IjM4IiByPSIyLjUiIGZpbGw9IiNmZmYiLz48L3N2Zz4="
  },
  "FR": {
    "code": "FR",
    "name_fa": "جمهوری فرانسه",
    "name_en": "France",
    "faction": "allies",
    "ideology": "democracy",
    "leader": "شارل دو گل",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/De_Gaulle-OWI_%28cropped%29_%28c%29%282%29.jpg/250px-De_Gaulle-OWI_%28cropped%29_%28c%29%282%29.jpg",
    "flag_url": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjAgODAiPjxyZWN0IHdpZHRoPSI0MCIgaGVpZ2h0PSI4MCIgZmlsbD0iIzAwMjY1NCIvPjxyZWN0IHg9IjQwIiB3aWR0aD0iNDAiIGhlaWdodD0iODAiIGZpbGw9IiNmZmZmZmYiLz48cmVjdCB4PSI4MCIgd2lkdGg9IjQwIiBoZWlnaHQ9IjgwIiBmaWxsPSIjY2UxMTI2Ii8+PC9zdmc+"
  },
  "PL": {
    "code": "PL",
    "name_fa": "جمهوری لهستان",
    "name_en": "Poland",
    "faction": "allies",
    "ideology": "democracy",
    "leader": "ولادیسلاو راچکیویچ",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/W%C5%82adys%C5%82aw_Raczkiewicz_1930.jpg/250px-W%C5%82adys%C5%82aw_Raczkiewicz_1930.jpg",
    "flag_url": "https://flagcdn.com/w160/pl.png"
  },
  "CN": {
    "code": "CN",
    "name_fa": "جمهوری چین (ملی‌گرا)",
    "name_en": "Republic of China",
    "faction": "allies",
    "ideology": "nonaligned",
    "leader": "چیانگ کای‌شک",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/%E8%94%A3%E4%B8%AD%E6%AD%A3%E7%B8%BD%E7%B5%B1%E7%8E%89%E7%85%A7.png/250px-%E8%94%A3%E4%B8%AD%E6%AD%A3%E7%B8%BD%E7%B5%B1%E7%8E%89%E7%85%A7.png",
    "flag_url": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjAgODAiPjxyZWN0IHdpZHRoPSIxMjAiIGhlaWdodD0iODAiIGZpbGw9IiNmZTAwMDAiLz48cmVjdCB3aWR0aD0iNjAiIGhlaWdodD0iNDAiIGZpbGw9IiMwMDAwOTUiLz48Y2lyY2xlIGN4PSIzMCIgY3k9IjIwIiByPSIxMCIgZmlsbD0iI2ZmZmZmZiIvPjxjaXJjbGUgY3g9IjMwIiBjeT0iMjAiIHI9IjcuNSIgZmlsbD0iIzAwMDA5NSIvPjxjaXJjbGUgY3g9IjMwIiBjeT0iMjAiIHI9IjUiIGZpbGw9IiNmZmZmZmYiLz48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzMCwyMCkiIGZpbGw9IiNmZmZmZmYiPjxwb2x5Z29uIHBvaW50cz0iMCwtMTQgMi41LC05IC0yLjUsLTkiLz48cG9seWdvbiBwb2ludHM9IjAsLTE0IDIuNSwtOSAtMi41LC05IiB0cmFuc2Zvcm09InJvdGF0ZSgzMCkiLz48cG9seWdvbiBwb2ludHM9IjAsLTE0IDIuNSwtOSAtMi41LC05IiB0cmFuc2Zvcm09InJvdGF0ZSg2MCkiLz48cG9seWdvbiBwb2ludHM9IjAsLTE0IDIuNSwtOSAtMi41LC05IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCkiLz48cG9seWdvbiBwb2ludHM9IjAsLTE0IDIuNSwtOSAtMi41LC05IiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIi8+PHBvbHlnb24gcG9pbnRzPSIwLC0xNCAyLjUsLTkgLTIuNSwtOSIgdHJhbnNmb3JtPSJyb3RhdGUoMTUwKSIvPjxwb2x5Z29uIHBvaW50cz0iMCwtMTQgMi41LC05IC0yLjUsLTkiIHRyYW5zZm9ybT0icm90YXRlKDE4MCkiLz48cG9seWdvbiBwb2ludHM9IjAsLTE0IDIuNSwtOSAtMi41LC05IiB0cmFuc2Zvcm09InJvdGF0ZSgyMTApIi8+PHBvbHlnb24gcG9pbnRzPSIwLC0xNCAyLjUsLTkgLTIuNSwtOSIgdHJhbnNmb3JtPSJyb3RhdGUoMjQwKSIvPjxwb2x5Z29uIHBvaW50cz0iMCwtMTQgMi41LC05IC0yLjUsLTkiIHRyYW5zZm9ybT0icm90YXRlKDI3MCkiLz48cG9seWdvbiBwb2ludHM9IjAsLTE0IDIuNSwtOSAtMi41LC05IiB0cmFuc2Zvcm09InJvdGF0ZSgzMDApIi8+PHBvbHlnb24gcG9pbnRzPSIwLC0xNCAyLjUsLTkgLTIuNSwtOSIgdHJhbnNmb3JtPSJyb3RhdGUoMzMwKSIvPjwvZz48L3N2Zz4="
  },
  "CA": {
    "code": "CA",
    "name_fa": "دومینیون کانادا",
    "name_en": "Canada",
    "faction": "allies",
    "ideology": "democracy",
    "leader": "مکنزی کینگ",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/William_Lyon_Mackenzie_King_1942_%28cropped%29.jpg/250px-William_Lyon_Mackenzie_King_1942_%28cropped%29.jpg",
    "flag_url": "https://flagcdn.com/w160/ca.png"
  },
  "AU": {
    "code": "AU",
    "name_fa": "استرالیا",
    "name_en": "Australia",
    "faction": "allies",
    "ideology": "democracy",
    "leader": "جان کورتین",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/John_Curtin_1942.jpg/250px-John_Curtin_1942.jpg",
    "flag_url": "https://flagcdn.com/w160/au.png"
  },
  "NZ": {
    "code": "NZ",
    "name_fa": "نیوزیلند",
    "name_en": "New Zealand",
    "faction": "allies",
    "ideology": "democracy",
    "leader": "پیتر فریزر",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Peter_Fraser_%28politician%29.jpg/250px-Peter_Fraser_%28politician%29.jpg",
    "flag_url": "https://flagcdn.com/w160/nz.png"
  },
  "IN": {
    "code": "IN",
    "name_fa": "راج بریتانیا (هند)",
    "name_en": "British Raj",
    "faction": "allies",
    "ideology": "nonaligned",
    "leader": "لرد لینلیثگو",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Lord_Linlithgow.jpg/250px-Lord_Linlithgow.jpg",
    "flag_url": "https://flagcdn.com/w160/in.png"
  },
  "ZA": {
    "code": "ZA",
    "name_fa": "آفریقای جنوبی",
    "name_en": "South Africa",
    "faction": "allies",
    "ideology": "democracy",
    "leader": "یان اسموتس",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Jan_Smuts_1941.jpg/250px-Jan_Smuts_1941.jpg",
    "flag_url": "https://flagcdn.com/w160/za.png"
  },
  "NL": {
    "code": "NL",
    "name_fa": "پادشاهی هلند",
    "name_en": "Netherlands",
    "faction": "allies",
    "ideology": "democracy",
    "leader": "ملکه ویلهلمینا",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Koningin_Wilhelmina_%281940%29.jpg/250px-Koningin_Wilhelmina_%281940%29.jpg",
    "flag_url": "https://flagcdn.com/w160/nl.png"
  },
  "BE": {
    "code": "BE",
    "name_fa": "پادشاهی بلژیک",
    "name_en": "Belgium",
    "faction": "allies",
    "ideology": "democracy",
    "leader": "لئوپولد سوم",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Leopold_III_of_Belgium_%281934%29.jpg/250px-Leopold_III_of_Belgium_%281934%29.jpg",
    "flag_url": "https://flagcdn.com/w160/be.png"
  },
  "NO": {
    "code": "NO",
    "name_fa": "پادشاهی نروژ",
    "name_en": "Norway",
    "faction": "allies",
    "ideology": "democracy",
    "leader": "هاکون هفتم",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Haakon_VII_1940.jpg/250px-Haakon_VII_1940.jpg",
    "flag_url": "https://flagcdn.com/w160/no.png"
  },
  "DK": {
    "code": "DK",
    "name_fa": "پادشاهی دانمارک",
    "name_en": "Denmark",
    "faction": "allies",
    "ideology": "democracy",
    "leader": "کریستیان دهم",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Christian_X_of_Denmark_1940.jpg/250px-Christian_X_of_Denmark_1940.jpg",
    "flag_url": "https://flagcdn.com/w160/dk.png"
  },
  "GR": {
    "code": "GR",
    "name_fa": "پادشاهی یونان",
    "name_en": "Greece",
    "faction": "allies",
    "ideology": "nonaligned",
    "leader": "یوآنیس متاکساس",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Ioannis_Metaxas.jpg/250px-Ioannis_Metaxas.jpg",
    "flag_url": "https://flagcdn.com/w160/gr.png"
  },
  "YU": {
    "code": "YU",
    "name_fa": "پادشاهی یوگسلاوی",
    "name_en": "Yugoslavia",
    "faction": "allies",
    "ideology": "nonaligned",
    "leader": "پیتر دوم",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Peter_II_of_Yugoslavia_in_uniform.jpg/250px-Peter_II_of_Yugoslavia_in_uniform.jpg",
    "flag_url": "https://flagcdn.com/w160/yu.png"
  },
  "CZ": {
    "code": "CZ",
    "name_fa": "چکسلواکی",
    "name_en": "Czechoslovakia",
    "faction": "allies",
    "ideology": "democracy",
    "leader": "ادوارد بنش",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Edvard_Bene%C5%A1_1938.jpg/250px-Edvard_Bene%C5%A1_1938.jpg",
    "flag_url": "https://flagcdn.com/w160/cz.png"
  },
  "LU": {
    "code": "LU",
    "name_fa": "لوکزامبورگ",
    "name_en": "Luxembourg",
    "faction": "allies",
    "ideology": "democracy",
    "leader": "گراندوشس شارلوت",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Grand_Duchess_Charlotte_of_Luxembourg.jpg/250px-Grand_Duchess_Charlotte_of_Luxembourg.jpg",
    "flag_url": "https://flagcdn.com/w160/lu.png"
  },
  "BR": {
    "code": "BR",
    "name_fa": "برزیل",
    "name_en": "Brazil",
    "faction": "allies",
    "ideology": "nonaligned",
    "leader": "ژتولیو وارگاس",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Getulio_Vargas_%281930%29.jpg/250px-Getulio_Vargas_%281930%29.jpg",
    "flag_url": "https://flagcdn.com/w160/br.png"
  },
  "MX": {
    "code": "MX",
    "name_fa": "مکزیک",
    "name_en": "Mexico",
    "faction": "allies",
    "ideology": "democracy",
    "leader": "لازارو کاردناس",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/L%C3%A1zaro.C%C3%A1rdenas.jpg/250px-L%C3%A1zaro.C%C3%A1rdenas.jpg",
    "flag_url": "https://flagcdn.com/w160/mx.png"
  },
  "SU": {
    "code": "SU",
    "name_fa": "اتحاد جماهیر شوروی",
    "name_en": "Soviet Union",
    "faction": "comintern",
    "ideology": "communism",
    "leader": "ژوزف استالین",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/StalinCropped1943.jpg/250px-StalinCropped1943.jpg",
    "flag_url": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjAgODAiPjxyZWN0IHdpZHRoPSIxMjAiIGhlaWdodD0iODAiIGZpbGw9IiNjYzAwMDAiLz48cGF0aCBkPSJNMjIsMTIgbDIsNiBoNiBsLTUsNCBsMiw2IGwtNSwtNCBsLTUsNCBsMiwtNiBsLTUsLTQgaDYgeiIgZmlsbD0iI2ZmY2MwMCIvPjxwYXRoIGQ9Ik0yMCwyNCBhMTEsMTEgMCAxLDEgMTIsMTIgbC0zLC0zIGE3LDcgMCAxLDAgLTcsLTcgeiIgZmlsbD0iI2ZmY2MwMCIvPjxyZWN0IHg9IjIyIiB5PSIzMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjQiIHRyYW5zZm9ybT0icm90YXRlKC00NSAyMiAzMikiIGZpbGw9IiNmZmNjMDAiLz48L3N2Zz4="
  },
  "MN": {
    "code": "MN",
    "name_fa": "جمهوری خلق مغولستان",
    "name_en": "Mongolia",
    "faction": "comintern",
    "ideology": "communism",
    "leader": "خورلوگین چویبالسان",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Khorloogiin_Choibalsan.jpg/250px-Khorloogiin_Choibalsan.jpg",
    "flag_url": "https://flagcdn.com/w160/mn.png"
  },
  "IR": {
    "code": "IR",
    "name_fa": "شاهنشاهی ایران",
    "name_en": "Iran",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "رضاشاه پهلوی",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Reza_shah_uniform.jpg/250px-Reza_shah_uniform.jpg",
    "flag_url": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjAgODAiPjxyZWN0IHdpZHRoPSIxMjAiIGhlaWdodD0iMjYuNiIgZmlsbD0iIzIzOWY0MCIvPjxyZWN0IHk9IjI2LjYiIHdpZHRoPSIxMjAiIGhlaWdodD0iMjYuNiIgZmlsbD0iI2ZmZmZmZiIvPjxyZWN0IHk9IjUzLjMiIHdpZHRoPSIxMjAiIGhlaWdodD0iMjYuNyIgZmlsbD0iI2RhMDAwMCIvPjxjaXJjbGUgY3g9IjYwIiBjeT0iMzgiIHI9IjkiIGZpbGw9IiNmNWIzMDAiLz48ZWxsaXBzZSBjeD0iNTgiIGN5PSI0MiIgcng9IjEwIiByeT0iNiIgZmlsbD0iI2Y1YjMwMCIvPjxjaXJjbGUgY3g9IjUyIiBjeT0iMzgiIHI9IjQuNSIgZmlsbD0iI2Y1YjMwMCIvPjxwYXRoIGQ9Ik00Nyw0MCBsLTgsLTMgbDEsLTIgbDgsMiB6IiBmaWxsPSIjZjViMzAwIi8+PHBhdGggZD0iTTY2LDQwIHE1LC02IDMsLTEyIiBzdHJva2U9IiNmNWIzMDAiIHN0cm9rZS13aWR0aD0iMi41IiBmaWxsPSJub25lIi8+PC9zdmc+"
  },
  "TR": {
    "code": "TR",
    "name_fa": "جمهوری ترکیه",
    "name_en": "Turkey",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "مصطفی کمال آتاتورک",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Ataturk1930s.jpg/250px-Ataturk1930s.jpg",
    "flag_url": "https://flagcdn.com/w160/tr.png"
  },
  "ES": {
    "code": "ES",
    "name_fa": "اسپانیا",
    "name_en": "Spain",
    "faction": "neutral",
    "ideology": "fascism",
    "leader": "فرانسیسکو فرانکو",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Francisco_Franco_posed_portrait_photograph.jpg/250px-Francisco_Franco_posed_portrait_photograph.jpg",
    "flag_url": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjAgODAiPjxyZWN0IHdpZHRoPSIxMjAiIGhlaWdodD0iMjYuNyIgZmlsbD0iI2FhMTUxYiIvPjxyZWN0IHk9IjI2LjciIHdpZHRoPSIxMjAiIGhlaWdodD0iMjYuNiIgZmlsbD0iI2YxYmYwMCIvPjxyZWN0IHk9IjUzLjMiIHdpZHRoPSIxMjAiIGhlaWdodD0iMjYuNyIgZmlsbD0iIzRiMWU0ZiIvPjxjaXJjbGUgY3g9IjQwIiBjeT0iNDAiIHI9IjciIGZpbGw9IiNhYTE1MWIiLz48cmVjdCB4PSIzNiIgeT0iMzYiIHdpZHRoPSI4IiBoZWlnaHQ9IjgiIGZpbGw9IiNmMWJmMDAiLz48L3N2Zz4="
  },
  "PT": {
    "code": "PT",
    "name_fa": "پرتغال",
    "name_en": "Portugal",
    "faction": "neutral",
    "ideology": "fascism",
    "leader": "آنتونیو دی اولیویرا سالازار",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Ant%C3%B3nio_de_Oliveira_Salazar_%281930s%29.jpg/250px-Ant%C3%B3nio_de_Oliveira_Salazar_%281930s%29.jpg",
    "flag_url": "https://flagcdn.com/w160/pt.png"
  },
  "SE": {
    "code": "SE",
    "name_fa": "پادشاهی سوئد",
    "name_en": "Sweden",
    "faction": "neutral",
    "ideology": "democracy",
    "leader": "گوستاو پنجم",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Gustaf_V_of_Sweden.jpg/250px-Gustaf_V_of_Sweden.jpg",
    "flag_url": "https://flagcdn.com/w160/se.png"
  },
  "CH": {
    "code": "CH",
    "name_fa": "کنفدراسیون سوئیس",
    "name_en": "Switzerland",
    "faction": "neutral",
    "ideology": "democracy",
    "leader": "فیلیپ اتر",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Philipp_Etter.jpg/250px-Philipp_Etter.jpg",
    "flag_url": "https://flagcdn.com/w160/ch.png"
  },
  "IE": {
    "code": "IE",
    "name_fa": "جمهوری ایرلند",
    "name_en": "Ireland",
    "faction": "neutral",
    "ideology": "democracy",
    "leader": "ایمون دو والرا",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Eamon_de_Valera_1932.jpg/250px-Eamon_de_Valera_1932.jpg",
    "flag_url": "https://flagcdn.com/w160/ie.png"
  },
  "AF": {
    "code": "AF",
    "name_fa": "پادشاهی افغانستان",
    "name_en": "Afghanistan",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "محمد ظاهرشاه",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Zahir_Shah_1930s.jpg/250px-Zahir_Shah_1930s.jpg",
    "flag_url": "https://flagcdn.com/w160/af.png"
  },
  "SA": {
    "code": "SA",
    "name_fa": "پادشاهی عربستان سعودی",
    "name_en": "Saudi Arabia",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "ملک عبدالعزیز آل سعود",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Ibn_Saud_1930s.jpg/250px-Ibn_Saud_1930s.jpg",
    "flag_url": "https://flagcdn.com/w160/sa.png"
  },
  "IQ": {
    "code": "IQ",
    "name_fa": "پادشاهی عراق",
    "name_en": "Iraq",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "ملک غازی اول",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Ghazi_of_Iraq.jpg/250px-Ghazi_of_Iraq.jpg",
    "flag_url": "https://flagcdn.com/w160/iq.png"
  },
  "EG": {
    "code": "EG",
    "name_fa": "پادشاهی مصر",
    "name_en": "Egypt",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "ملک فاروق اول",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/King_Farouk_1937.jpg/250px-King_Farouk_1937.jpg",
    "flag_url": "https://flagcdn.com/w160/eg.png"
  },
  "ET": {
    "code": "ET",
    "name_fa": "امپراتوری اتیوپی",
    "name_en": "Ethiopia",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "هایله سلاسی",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Haile_Selassie_in_full_dress_%283x4_cropped%29.jpg/250px-Haile_Selassie_in_full_dress_%283x4_cropped%29.jpg",
    "flag_url": "https://flagcdn.com/w160/et.png"
  },
  "AR": {
    "code": "AR",
    "name_fa": "آرژانتین",
    "name_en": "Argentina",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "روبرتو ماریا اورتیز",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Roberto_Mar%C3%ADa_Ortiz.jpg/250px-Roberto_Mar%C3%ADa_Ortiz.jpg",
    "flag_url": "https://flagcdn.com/w160/ar.png"
  },
  "CL": {
    "code": "CL",
    "name_fa": "جمهوری شیلی",
    "name_en": "Chile",
    "faction": "neutral",
    "ideology": "democracy",
    "leader": "پدرو آگوئیره سردار",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Pedro_Aguirre_Cerda_1938.jpg/250px-Pedro_Aguirre_Cerda_1938.jpg",
    "flag_url": "https://flagcdn.com/w160/cl.png"
  },
  "CO": {
    "code": "CO",
    "name_fa": "جمهوری کلمبیا",
    "name_en": "Colombia",
    "faction": "neutral",
    "ideology": "democracy",
    "leader": "ادواردو سانتوس",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Eduardo_Santos_Montealegre.jpg/250px-Eduardo_Santos_Montealegre.jpg",
    "flag_url": "https://flagcdn.com/w160/co.png"
  },
  "PE": {
    "code": "PE",
    "name_fa": "پرو",
    "name_en": "Peru",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "اسکار بناویدس",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/%C3%93scar_R._Benavides.jpg/250px-Oscar_R._Benavides.jpg",
    "flag_url": "https://flagcdn.com/w160/pe.png"
  },
  "VE": {
    "code": "VE",
    "name_fa": "ونزوئلا",
    "name_en": "Venezuela",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "الازار لوپز کنتراس",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Eleazar_L%C3%B3pez_Contreras.jpg/250px-Eleazar_L%C3%B3pez_Contreras.jpg",
    "flag_url": "https://flagcdn.com/w160/ve.png"
  },
  "CU": {
    "code": "CU",
    "name_fa": "کوبا",
    "name_en": "Cuba",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "فولخنسیو باتیستا",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Fulgencio_Batista_1938.jpg/250px-Fulgencio_Batista_1938.jpg",
    "flag_url": "https://flagcdn.com/w160/cu.png"
  },
  "EE": {
    "code": "EE",
    "name_fa": "استونی",
    "name_en": "Estonia",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "کنستانتین پاتس",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Konstantin_P%C3%A4ts_1934.jpg/250px-Konstantin_P%C3%A4ts_1934.jpg",
    "flag_url": "https://flagcdn.com/w160/ee.png"
  },
  "LV": {
    "code": "LV",
    "name_fa": "لتونی",
    "name_en": "Latvia",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "کارلیس اولمانیس",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/K%C4%81rlis_Ulmanis_1934.jpg/250px-K%C4%81rlis_Ulmanis_1934.jpg",
    "flag_url": "https://flagcdn.com/w160/lv.png"
  },
  "LT": {
    "code": "LT",
    "name_fa": "لیتوانی",
    "name_en": "Lithuania",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "آنتاناس اسمتونا",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Antanas_Smetona.jpg/250px-Antanas_Smetona.jpg",
    "flag_url": "https://flagcdn.com/w160/lt.png"
  },
  "TB": {
    "code": "TB",
    "name_fa": "تبت",
    "name_en": "Tibet",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "دالایی لاما چهاردهم",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Dalai_Lama_1940.jpg/250px-Dalai_Lama_1940.jpg",
    "flag_url": "https://flagcdn.com/w160/tb.png"
  },
  "NP": {
    "code": "NP",
    "name_fa": "نپال",
    "name_en": "Nepal",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "جودا شومشر رانا",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Juddha_Shumsher.jpg/250px-Juddha_Shumsher.jpg",
    "flag_url": "https://flagcdn.com/w160/np.png"
  },
  "BT": {
    "code": "BT",
    "name_fa": "بوتان",
    "name_en": "Bhutan",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "جیگمه وانگچوک",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Jigme_Wangchuck.jpg/250px-Jigme_Wangchuck.jpg",
    "flag_url": "https://flagcdn.com/w160/bt.png"
  },
  "YE": {
    "code": "YE",
    "name_fa": "پادشاهی یمن",
    "name_en": "Yemen",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "امام یحیی حمیدالدین",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Imam_Yahya.jpg/250px-Imam_Yahya.jpg",
    "flag_url": "https://flagcdn.com/w160/ye.png"
  },
  "OM": {
    "code": "OM",
    "name_fa": "سلطنت عمان",
    "name_en": "Oman",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "سلطان سعید بن تیمور",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Said_bin_Taimur.jpg/250px-Said_bin_Taimur.jpg",
    "flag_url": "https://flagcdn.com/w160/om.png"
  },
  "IS": {
    "code": "IS",
    "name_fa": "ایسلند",
    "name_en": "Iceland",
    "faction": "neutral",
    "ideology": "democracy",
    "leader": "هرماند یوناسون",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Hermann_J%C3%B3nasson.jpg/250px-Hermann_J%C3%B3nasson.jpg",
    "flag_url": "https://flagcdn.com/w160/is.png"
  },
  "AL": {
    "code": "AL",
    "name_fa": "پادشاهی آلبانی",
    "name_en": "Albania",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "شاه زوگ اول",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/King_Zog_I.jpg/250px-King_Zog_I.jpg",
    "flag_url": "https://flagcdn.com/w160/al.png"
  },
  "UY": {
    "code": "UY",
    "name_fa": "اروگوئه",
    "name_en": "Uruguay",
    "faction": "neutral",
    "ideology": "democracy",
    "leader": "آلفردو بالدومیر",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Alfredo_Baldomir.jpg/250px-Alfredo_Baldomir.jpg",
    "flag_url": "https://flagcdn.com/w160/uy.png"
  },
  "PY": {
    "code": "PY",
    "name_fa": "پاراگوئه",
    "name_en": "Paraguay",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "خوزه فلیکس استیگاریبیا",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Jos%C3%A9_F%C3%A9lix_Estigarribia.jpg/250px-Jos%C3%A9_F%C3%A9lix_Estigarribia.jpg",
    "flag_url": "https://flagcdn.com/w160/py.png"
  },
  "BO": {
    "code": "BO",
    "name_fa": "بولیوی",
    "name_en": "Bolivia",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "خرمان بوش",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Germ%C3%A1n_Busch.jpg/250px-Germ%C3%A1n_Busch.jpg",
    "flag_url": "https://flagcdn.com/w160/bo.png"
  },
  "EC": {
    "code": "EC",
    "name_fa": "اکوادور",
    "name_en": "Ecuador",
    "faction": "neutral",
    "ideology": "democracy",
    "leader": "آئورلیو موسکئرا",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Aurelio_Mosquera_Narv%C3%A1ez.jpg/250px-Aurelio_Mosquera_Narv%C3%A1ez.jpg",
    "flag_url": "https://flagcdn.com/w160/ec.png"
  },
  "GT": {
    "code": "GT",
    "name_fa": "گواتمالا",
    "name_en": "Guatemala",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "خورخه اوبیکو",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Jorge_Ubico.jpg/250px-Jorge_Ubico.jpg",
    "flag_url": "https://flagcdn.com/w160/gt.png"
  },
  "HN": {
    "code": "HN",
    "name_fa": "هندوراس",
    "name_en": "Honduras",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "تیبورسیو کاریاس آندینو",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Tiburcio_Car%C3%ADas_Andino.jpg/250px-Tiburcio_Car%C3%ADas_Andino.jpg",
    "flag_url": "https://flagcdn.com/w160/hn.png"
  },
  "SV": {
    "code": "SV",
    "name_fa": "السالوادور",
    "name_en": "El Salvador",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "ماکسیمیلیانو هرناندز مارتینز",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Maximiliano_Hern%C3%A1ndez_Mart%C3%ADnez.jpg/250px-Maximiliano_Hern%C3%A1ndez_Mart%C3%ADnez.jpg",
    "flag_url": "https://flagcdn.com/w160/sv.png"
  },
  "NI": {
    "code": "NI",
    "name_fa": "نیکاراگوئه",
    "name_en": "Nicaragua",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "آناستاسیو سوموسا گارسیا",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Anastasio_Somoza_Garc%C3%ADa.jpg/250px-Anastasio_Somoza_Garc%C3%ADa.jpg",
    "flag_url": "https://flagcdn.com/w160/ni.png"
  },
  "CR": {
    "code": "CR",
    "name_fa": "کاستاریکا",
    "name_en": "Costa Rica",
    "faction": "neutral",
    "ideology": "democracy",
    "leader": "لئون کورتس کاسترو",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Le%C3%B3n_Cort%C3%A9s_Castro.jpg/250px-Le%C3%B3n_Cort%C3%A9s_Castro.jpg",
    "flag_url": "https://flagcdn.com/w160/cr.png"
  },
  "PA": {
    "code": "PA",
    "name_fa": "پاناما",
    "name_en": "Panama",
    "faction": "neutral",
    "ideology": "democracy",
    "leader": "خوان دموستنس آروزمنا",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Juan_Dem%C3%B3stenes_Arosemena.jpg/250px-Juan_Dem%C3%B3stenes_Arosemena.jpg",
    "flag_url": "https://flagcdn.com/w160/pa.png"
  },
  "DO": {
    "code": "DO",
    "name_fa": "جمهوری دومینیکن",
    "name_en": "Dominican Republic",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "رافائل تروخیو",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Rafael_Trujillo_1933.jpg/250px-Rafael_Trujillo_1933.jpg",
    "flag_url": "https://flagcdn.com/w160/do.png"
  },
  "HT": {
    "code": "HT",
    "name_fa": "هائیتی",
    "name_en": "Haiti",
    "faction": "neutral",
    "ideology": "nonaligned",
    "leader": "استنیو ونسنت",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/St%C3%A9nio_Vincent.jpg/250px-St%C3%A9nio_Vincent.jpg",
    "flag_url": "https://flagcdn.com/w160/ht.png"
  },
  "LR": {
    "code": "LR",
    "name_fa": "لیبریا",
    "name_en": "Liberia",
    "faction": "neutral",
    "ideology": "democracy",
    "leader": "ادوین بارکلی",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Edwin_Barclay.jpg/250px-Edwin_Barclay.jpg",
    "flag_url": "https://flagcdn.com/w160/lr.png"
  },
  "PH": {
    "code": "PH",
    "name_fa": "فیلیپین (مشترک‌المنافع)",
    "name_en": "Philippines",
    "faction": "allies",
    "ideology": "democracy",
    "leader": "مانوئل ال. کوئزون",
    "leader_img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Manuel_Quezon_%28cropped%29.jpg/250px-Manuel_Quezon_%28cropped%29.jpg",
    "flag_url": "https://flagcdn.com/w160/ph.png"
  },
  "SK": {
    "name_fa": "جمهوری اسلواکی",
    "name_en": "Slovakia",
    "code": "SK",
    "faction": "axis",
    "ideology": "fascism",
    "capital": "براتیسلاوا",
    "leader": {
      "name": "یوزف تیسو",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Jozef_Tiso_1940.jpg/480px-Jozef_Tiso_1940.jpg"
    },
    "flag": "https://flagcdn.com/w160/sk.png",
    "desc": "دولت اقماری نوپای محور پس از تجزیه چکسلواکی در مارس ۱۹۳۹."
  },
  "CP": {
    "name_fa": "جمهوری شورایی چین (یان‌آن)",
    "name_en": "Communist China",
    "code": "CP",
    "faction": "comintern",
    "ideology": "communism",
    "capital": "یان‌آن",
    "leader": {
      "name": "مائو تسه‌تونگ",
      "title": "رئیس حزب کمونیست",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Mao_Zedong_1938.jpg/480px-Mao_Zedong_1938.jpg"
    },
    "flag": "https://flagcdn.com/w160/cn.png",
    "desc": "پایگاه ارتش سرخ چین در غارهای یان‌آن پس از راهپیمایی طولانی و آغاز نبردهای چریکی علیه ژاپن."
  },
  "TU": {
    "name_fa": "جمهوری خلق تووا",
    "name_en": "Tannu Tuva",
    "code": "TU",
    "faction": "comintern",
    "ideology": "communism",
    "capital": "کیزیل",
    "leader": {
      "name": "سالچاک توکا",
      "title": "دبیرکل حزب تووا",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Salchak_Toka_1940s.jpg/480px-Salchak_Toka_1940s.jpg"
    },
    "flag": "https://flagcdn.com/w160/ru.png",
    "desc": "جمهوری کوهستانی آسیای میانه و نخستین کشوری که در کنار مسکو علیه آلمان اعلان جنگ داد."
  },
  "MZ": {
    "name_fa": "امپراتوری منچوکوئو",
    "name_en": "Manchukuo",
    "code": "MZ",
    "faction": "axis",
    "ideology": "fascism",
    "capital": "شین‌جینگ",
    "leader": {
      "name": "پویی (امپراتور کانگ‌ده)",
      "title": "امپراتور منچوکوئو",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Puyi_Manchukuo_emperor.jpg/480px-Puyi_Manchukuo_emperor.jpg"
    },
    "flag": "https://flagcdn.com/w160/cn.png",
    "desc": "دولت اقماری صنعتی در شمال شرق چین به رهبری آخرین امپراتور چین با معادن غنی زغال‌سنگ و آهن."
  }
}

COUNTRY_CODES = list(COUNTRIES.keys())
