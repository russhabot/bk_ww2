# Burnt Kingdoms WW2 (1939) Game Data
# 75 Sovereign States, Factions, Ideologies, Historical Badges, and WW2 dossiers.

FACTIONS = {
  "axis": {
    "fa": "محور (متحدین)",
    "en": "Axis Powers",
    "color": "#dc2626",
    "bg": "#450a0a",
    "border": "#ef4444",
    "badge_svg": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj4KICA8ZGVmcz4KICAgIDxyYWRpYWxHcmFkaWVudCBpZD0iYWciIGN4PSI1MCUiIGN5PSI1MCUiIHI9IjUwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNkYzI2MjYiLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjNDUwYTBhIi8+CiAgICA8L3JhZGlhbEdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSI1MCIgY3k9IjUwIiByPSI0NiIgZmlsbD0idXJsKCNhZykiIHN0cm9rZT0iI2VhYjMwOCIgc3Ryb2tlLXdpZHRoPSIzIi8+CiAgPHBhdGggZD0iTTUwIDE1IEw1NyAzMiBMNzUgMzIgTDYwIDQ0IEw2NiA2MiBMNTAgNTAgTDM0IDYyIEw0MCA0NCBMMjUgMzIgTDQzIDMyIFoiIGZpbGw9IiNlYWIzMDgiIHN0cm9rZT0iIzc4MzUwZiIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KICA8cGF0aCBkPSJNMzggNDggTDUwIDM2IEw2MiA0OCBMNTAgNjAgWiIgZmlsbD0iIzE4MTgxYiIgc3Ryb2tlPSIjZWFiMzA4IiBzdHJva2Utd2lkdGg9IjIiLz4KICA8cGF0aCBkPSJNNDIgNzAgTDUwIDgyIEw1OCA3MCBMNTAgNzQgWiIgZmlsbD0iI2VhYjMwOCIvPgogIDxjaXJjbGUgY3g9IjUwIiBjeT0iNDgiIHI9IjQiIGZpbGw9IiNlZjQ0NDQiLz4KPC9zdmc+",
    "desc": "ائتلاف نظامی آلمان، ایتالیا، ژاپن و دولت‌های هم‌پیمان با هدف تغییر نظم جهانی."
  },
  "allies": {
    "fa": "متفقین",
    "en": "Allied Powers",
    "color": "#2563eb",
    "bg": "#172554",
    "border": "#3b82f6",
    "badge_svg": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj4KICA8ZGVmcz4KICAgIDxyYWRpYWxHcmFkaWVudCBpZD0iYWxnIiBjeD0iNTAlIiBjeT0iNTAlIiByPSI1MCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMjU2M2ViIi8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzBmMTcyYSIvPgogICAgPC9yYWRpYWxHcmFkaWVudD4KICA8L2RlZnM+CiAgPGNpcmNsZSBjeD0iNTAiIGN5PSI1MCIgcj0iNDYiIGZpbGw9InVybCgjYWxnKSIgc3Ryb2tlPSIjMzhiZGY4IiBzdHJva2Utd2lkdGg9IjMiLz4KICA8cG9seWdvbiBwb2ludHM9IjUwLDE2IDYwLDM4IDg0LDM4IDY1LDUzIDcyLDc2IDUwLDYyIDI4LDc2IDM1LDUzIDE2LDM4IDQwLDM4IiBmaWxsPSIjMzhiZGY4IiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMS41Ii8+CiAgPGNpcmNsZSBjeD0iNTAiIGN5PSI0OSIgcj0iMTIiIGZpbGw9IiMxZTNhOGEiIHN0cm9rZT0iIzY3ZThmOSIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgPHBhdGggZD0iTTQzIDQ5IEw0OCA1NCBMNTggNDQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI2ZmZmZmZiIgc3Ryb2tlLXdpZHRoPSIzIiBzdHJva2UtbGluZWNhcD0icm91bmQiLz4KPC9zdmc+",
    "desc": "اتحاد بریتانیا، فرانسه، ایالات متحده، چین و دموکراسی‌ها برای دفاع در برابر سلطه‌طلبی محور."
  },
  "comintern": {
    "fa": "کمینترن (کمونیسم بین‌الملل)",
    "en": "Comintern",
    "color": "#dc2626",
    "bg": "#7f1d1d",
    "border": "#f87171",
    "badge_svg": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj4KICA8ZGVmcz4KICAgIDxyYWRpYWxHcmFkaWVudCBpZD0iY2ciIGN4PSI1MCUiIGN5PSI1MCUiIHI9IjUwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNlZjQ0NDQiLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjN2YxZDFkIi8+CiAgICA8L3JhZGlhbEdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSI1MCIgY3k9IjQ2IiByPSI0NCIgZmlsbD0idXJsKCNjZykiIHN0cm9rZT0iI2ZiYmYyNCIgc3Ryb2tlLXdpZHRoPSIzIi8+CiAgPHBvbHlnb24gcG9pbnRzPSI1MCwxNCA1OCwzMiA3OCwzMiA2Miw0NCA2OCw2NCA1MCw1MiAzMiw2NCAzOCw0NCAyMiwzMiA0MiwzMiIgZmlsbD0iI2ZiYmYyNCIgc3Ryb2tlPSIjZDk3NzA2IiBzdHJva2Utd2lkdGg9IjEuNSIvPgogIDxwYXRoIGQ9Ik00MCA2OCBDMzQgNjIgMzMgNTAgNDIgNDIgQzQ5IDM1IDU5IDM2IDY1IDQxIEM2NyA0MyA2NSA0NiA2MiA0NCBDNTcgNDEgNDkgNDAgNDUgNDUgQzM4IDUyIDQwIDYwIDQ1IDY0IFoiIGZpbGw9IiNmZmZmZmYiLz4KICA8cmVjdCB4PSI0NyIgeT0iNDciIHdpZHRoPSI2IiBoZWlnaHQ9IjI0IiByeD0iMiIgdHJhbnNmb3JtPSJyb3RhdGUoLTM1IDUwIDU5KSIgZmlsbD0iI2ZmZmZmZiIvPgogIDxyZWN0IHg9IjM2IiB5PSI1MiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjYiIHJ4PSIyIiB0cmFuc2Zvcm09InJvdGF0ZSgtMzUgNTAgNTkpIiBmaWxsPSIjZmZmZmZmIi8+Cjwvc3ZnPg==",
    "desc": "بلوک سوسیالیستی به رهبری اتحاد جماهیر شوروی، مغولستان و احزاب کارگری جهان."
  },
  "neutral": {
    "fa": "غیرمتعهد / بی‌طرف",
    "en": "Non-Aligned / Neutral",
    "color": "#64748b",
    "bg": "#1e293b",
    "border": "#94a3b8",
    "badge_svg": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj4KICA8ZGVmcz4KICAgIDxyYWRpYWxHcmFkaWVudCBpZD0ibmciIGN4PSI1MCUiIGN5PSI1MCUiIHI9IjUwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM0NzU1NjkiLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMGYxNzJhIi8+CiAgICA8L3JhZGlhbEdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSI1MCIgY3k9IjUwIiByPSI0NiIgZmlsbD0idXJsKCNuZykiIHN0cm9rZT0iIzk0YTNiOCIgc3Ryb2tlLXdpZHRoPSIzIi8+CiAgPHBhdGggZD0iTTUwIDIwIEw1MCA3OCBNMzUgODAgTDY1IDgwIiBzdHJva2U9IiNmMWY1ZjkiIHN0cm9rZS13aWR0aD0iNCIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIi8+CiAgPHBhdGggZD0iTTI1IDM2IEw3NSAzNiIgc3Ryb2tlPSIjZjFmNWY5IiBzdHJva2Utd2lkdGg9IjMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogIDxwYXRoIGQ9Ik0yNSAzNiBMMTcgNTYgTDMzIDU2IFoiIGZpbGw9IiM5NGEzYjgiIHN0cm9rZT0iI2YxZjVmOSIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KICA8cGF0aCBkPSJNNzUgMzYgTDY3IDU2IEw4MyA1NiBaIiBmaWxsPSIjOTRhM2I4IiBzdHJva2U9IiNmMWY1ZjkiIHN0cm9rZS13aWR0aD0iMS41Ii8+CiAgPGNpcmNsZSBjeD0iNTAiIGN5PSIyMCIgcj0iNSIgZmlsbD0iI2ZiYmYyNCIvPgo8L3N2Zz4=",
    "desc": "کشورهای مستقل و اعلام‌کننده بی‌طرفی رسمی که از پیوستن به بلوک‌های نظامی خودداری کرده‌اند."
  }
}

IDEOLOGIES = {
  "fascism": {
    "fa": "فاشیسم / تمامیت‌خواهی",
    "en": "Fascism & National Socialism",
    "color": "#b91c1c",
    "badge_svg": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj4KICA8ZGVmcz4KICAgIDxyYWRpYWxHcmFkaWVudCBpZD0iZmciIGN4PSI1MCUiIGN5PSI1MCUiIHI9IjUwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM3ZjFkMWQiLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMTgxODFiIi8+CiAgICA8L3JhZGlhbEdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSI1MCIgY3k9IjUwIiByPSI0NiIgZmlsbD0idXJsKCNmZykiIHN0cm9rZT0iI2RjMjYyNiIgc3Ryb2tlLXdpZHRoPSIzIi8+CiAgPHJlY3QgeD0iNDYiIHk9IjIwIiB3aWR0aD0iOCIgaGVpZ2h0PSI2MCIgZmlsbD0iI2Q5NzcwNiIgcng9IjIiLz4KICA8bGluZSB4MT0iNDIiIHkxPSIzMCIgeDI9IjU4IiB5Mj0iMzAiIHN0cm9rZT0iI2Y1OWUwYiIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgPGxpbmUgeDE9IjQyIiB5MT0iNTAiIHgyPSI1OCIgeTI9IjUwIiBzdHJva2U9IiNmNTllMGIiIHN0cm9rZS13aWR0aD0iMiIvPgogIDxsaW5lIHgxPSI0MiIgeTE9IjcwIiB4Mj0iNTgiIHkyPSI3MCIgc3Ryb2tlPSIjZjU5ZTBiIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8cGF0aCBkPSJNNTQgMzIgQzY1IDI1IDc0IDM4IDY4IDQ4IEM2MyA1NiA1NCA1MiA1NCA1MiBaIiBmaWxsPSIjZjg3MTcxIiBzdHJva2U9IiNmZWYwOGEiIHN0cm9rZS13aWR0aD0iMiIvPgo8L3N2Zz4=",
    "desc": "حکومت توتالیتر متمرکز با نظامی‌گری و ناسیونالیسم رادیکال."
  },
  "communism": {
    "fa": "کمونیسم / سوسیالیسم مارکسیستی",
    "en": "Marxist-Leninist Communism",
    "color": "#dc2626",
    "badge_svg": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj4KICA8ZGVmcz4KICAgIDxyYWRpYWxHcmFkaWVudCBpZD0iY29tZyIgY3g9IjUwJSIgY3k9IjUwJSIgcj0iNTAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iI2I5MWMxYyIvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiM0NTBhMGEiLz4KICAgIDwvcmFkaWFsR3JhZGllbnQ+CiAgPC9kZWZzPgogIDxjaXJjbGUgY3g9IjUwIiBjeT0iNTAiIHI9IjQ2IiBmaWxsPSJ1cmwoI2NvbWcpIiBzdHJva2U9IiNmYWNjMTUiIHN0cm9rZS13aWR0aD0iMyIvPgogIDxwb2x5Z29uIHBvaW50cz0iNTAsMTggNTYsMzIgNzEsMzIgNTksNDIgNjMsNTcgNTAsNDggMzcsNTcgNDEsNDIgMjksMzIgNDQsMzIiIGZpbGw9IiNmYWNjMTUiLz4KICA8cGF0aCBkPSJNMzggNzIgQzMyIDY2IDMyIDU0IDQxIDQ2IEM0OCAzOSA1NyA0MCA2MyA0NSBDNjUgNDcgNjMgNTAgNjAgNDggQzU1IDQ1IDQ3IDQ0IDQzIDQ5IEMzNiA1NiAzOCA2NCA0MyA2OCBaIiBmaWxsPSIjZmFjYzE1Ii8+CiAgPHJlY3QgeD0iNDYiIHk9IjUyIiB3aWR0aD0iNiIgaGVpZ2h0PSIyNCIgcng9IjIiIHRyYW5zZm9ybT0icm90YXRlKC0zNSA1MCA2NCkiIGZpbGw9IiNmYWNjMTUiLz4KPC9zdmc+",
    "desc": "دیکتاتوری پرولتاریا، اقتصاد برنامه‌ریزی‌شده دولتی و مالکیت اشتراکی."
  },
  "democracy": {
    "fa": "دموکراسی پارلمانی",
    "en": "Parliamentary Democracy",
    "color": "#2563eb",
    "badge_svg": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj4KICA8ZGVmcz4KICAgIDxyYWRpYWxHcmFkaWVudCBpZD0iZGVtZyIgY3g9IjUwJSIgY3k9IjUwJSIgcj0iNTAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzFkNGVkOCIvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMwMjg0YzciLz4KICAgIDwvcmFkaWFsR3JhZGllbnQ+CiAgPC9kZWZzPgogIDxjaXJjbGUgY3g9IjUwIiBjeT0iNTAiIHI9IjQ2IiBmaWxsPSJ1cmwoI2RlbWcpIiBzdHJva2U9IiM2N2U4ZjkiIHN0cm9rZS13aWR0aD0iMyIvPgogIDxwYXRoIGQ9Ik00NyA1MiBMNTMgNTIgTDUxIDc4IEw0OSA3OCBaIiBmaWxsPSIjZmFjYzE1IiBzdHJva2U9IiNjYThhMDQiIHN0cm9rZS13aWR0aD0iMS41Ii8+CiAgPHBhdGggZD0iTTQzIDQ4IEw1NyA0OCBMNTMgNTQgTDQ3IDU0IFoiIGZpbGw9IiNlYWIzMDgiLz4KICA8cGF0aCBkPSJNNTAgMjAgQzQyIDMwIDQ2IDQwIDUwIDQ4IEM1NCA0MCA1OCAzMCA1MCAyMCBaIiBmaWxsPSIjZmI5MjNjIiBzdHJva2U9IiNmZWYwOGEiIHN0cm9rZS13aWR0aD0iMS41Ii8+CiAgPGNpcmNsZSBjeD0iNTAiIGN5PSIzOCIgcj0iNCIgZmlsbD0iI2ZlZjA4YSIvPgo8L3N2Zz4=",
    "desc": "نظام چندحزبی، آزادی‌های مدنی و پارلمان قانون‌گذار."
  },
  "neutral": {
    "fa": "سلطنت و محافظه‌کاری",
    "en": "Monarchy & Authoritarian Neutrality",
    "color": "#7c3aed",
    "badge_svg": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj4KICA8ZGVmcz4KICAgIDxyYWRpYWxHcmFkaWVudCBpZD0ibW9uX2ciIGN4PSI1MCUiIGN5PSI1MCUiIHI9IjUwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiM2YjIxYTgiLz4KICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMWUxYjRiIi8+CiAgICA8L3JhZGlhbEdyYWRpZW50PgogIDwvZGVmcz4KICA8Y2lyY2xlIGN4PSI1MCIgY3k9IjUwIiByPSI0NiIgZmlsbD0idXJsKCNtb25fZykiIHN0cm9rZT0iI2VhYjMwOCIgc3Ryb2tlLXdpZHRoPSIzIi8+CiAgPHBhdGggZD0iTTI2IDY0IEw3NCA2NCBMNzAgNDIgTDU4IDU0IEw1MCAzMiBMNDIgNTQgTDMwIDQyIFoiIGZpbGw9IiNlYWIzMDgiIHN0cm9rZT0iI2NhOGEwNCIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgPGNpcmNsZSBjeD0iNTAiIGN5PSIzMCIgcj0iNCIgZmlsbD0iI2ZlZjA4YSIvPgogIDxjaXJjbGUgY3g9IjMwIiBjeT0iNDAiIHI9IjMiIGZpbGw9IiNmZWYwOGEiLz4KICA8Y2lyY2xlIGN4PSI3MCIgY3k9IjQwIiByPSIzIiBmaWxsPSIjZmVmMDhhIi8+CiAgPHJlY3QgeD0iMjYiIHk9IjY2IiB3aWR0aD0iNDgiIGhlaWdodD0iNiIgcng9IjIiIGZpbGw9IiNjYThhMDQiLz4KPC9zdmc+",
    "desc": "پادشاهی‌های سنتی، رژیم‌های نظامی خودکامه یا بی‌طرفی پایدار."
  }
}

COUNTRIES = {
  "DE": {
    "name_fa": "آلمان نازی",
    "name_en": "Nazi Germany",
    "code": "DE",
    "faction": "axis",
    "ideology": "fascism",
    "capital": "برلین",
    "leader": {
      "name": "آدولف هیتلر",
      "title": "پیشوا و صدراعظم",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Hitler_portrait_crop.jpg/480px-Hitler_portrait_crop.jpg"
    },
    "flag": "https://flagcdn.com/w160/de.png",
    "desc": "قدرت نظامی برتر اروپای مرکزی با دکترین جنگ برق‌آسا (بلایتس‌کریگ) و ارتش ورماخت."
  },
  "GB": {
    "name_fa": "بریتانیای کبیر",
    "name_en": "United Kingdom",
    "code": "GB",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "لندن",
    "leader": {
      "name": "وینستون چرچیل",
      "title": "نخست‌وزیر",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Sir_Winston_Churchill_-_1941_%28cropped%29.jpg/480px-Sir_Winston_Churchill_-_1941_%28cropped%29.jpg"
    },
    "flag": "https://flagcdn.com/w160/gb.png",
    "desc": "بزرگ‌ترین امپراتوری دریایی جهان با نیروی دریایی سلطنتی مقتدر و ناوگان هوایی RAF."
  },
  "SU": {
    "name_fa": "اتحاد جماهیر شوروی",
    "name_en": "Soviet Union",
    "code": "SU",
    "faction": "comintern",
    "ideology": "communism",
    "capital": "مسکو",
    "leader": {
      "name": "ژوزف استالین",
      "title": "دبیرکل حزب کمونیست",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Stalin_lg_zendf.jpg/480px-Stalin_lg_zendf.jpg"
    },
    "flag": "https://flagcdn.com/w160/ru.png",
    "desc": "ابرقدرت سوسیالیستی شرق با ارتش سرخ عظیم، منابع بیکران معدنی و عمق استراتژیک اوراسیا."
  },
  "US": {
    "name_fa": "ایالات متحده آمریکا",
    "name_en": "United States",
    "code": "US",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "واشینگتن",
    "leader": {
      "name": "فرانکلین روزولت",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/FDR_1944_Color_Portrait.jpg/480px-FDR_1944_Color_Portrait.jpg"
    },
    "flag": "https://flagcdn.com/w160/us.png",
    "desc": "غول اقتصادی و صنعتی جهان با ظرفیت نامحدود کارخانه‌ای و پتانسیل ساخت عظیم‌ترین زرادخانه دموکراسی."
  },
  "JP": {
    "name_fa": "امپراتوری ژاپن",
    "name_en": "Empire of Japan",
    "code": "JP",
    "faction": "axis",
    "ideology": "fascism",
    "capital": "توکیو",
    "leader": {
      "name": "هیروهیتو (شووا)",
      "title": "امپراتور ژاپن",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Hirohito_in_dress_uniform.jpg/480px-Hirohito_in_dress_uniform.jpg"
    },
    "flag": "https://flagcdn.com/w160/jp.png",
    "desc": "نیروی دریایی پیشرفته امپراتوری در اقیانوس آرام با ناوهای هواپیمابر و روحیه سامورایی."
  },
  "FR": {
    "name_fa": "جمهوری فرانسه",
    "name_en": "France",
    "code": "FR",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "پاریس",
    "leader": {
      "name": "شارل دوگل",
      "title": "رهبر فرانسه آزاد",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Charles_de_Gaulle_1942.jpg/480px-Charles_de_Gaulle_1942.jpg"
    },
    "flag": "https://flagcdn.com/w160/fr.png",
    "desc": "قدرت تاریخی غرب اروپا با خط دفاعی مستحکم ماژینو و مستعمرات گسترده در آفریقا و آسیا."
  },
  "IT": {
    "name_fa": "پادشاهی ایتالیا",
    "name_en": "Kingdom of Italy",
    "code": "IT",
    "faction": "axis",
    "ideology": "fascism",
    "capital": "رم",
    "leader": {
      "name": "بنیتو موسولینی",
      "title": "دوچه فاشیسم",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Mussolini_in_uniform.jpg/480px-Mussolini_in_uniform.jpg"
    },
    "flag": "https://flagcdn.com/w160/it.png",
    "desc": "خاستگاه فاشیسم با تسلط بر دریای مدیترانه، ادعای بازسازی شکوه روم باستان و متصرفات در شمال آفریقا."
  },
  "CN": {
    "name_fa": "جمهوری چین (ملی‌گرا)",
    "name_en": "Republic of China",
    "code": "CN",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "چونگ‌کینگ",
    "leader": {
      "name": "چیانگ کای‌شک",
      "title": "ژنرالیسیمو",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Chiang_Kai-shek_1943.jpg/480px-Chiang_Kai-shek_1943.jpg"
    },
    "flag": "https://flagcdn.com/w160/tw.png",
    "desc": "دولت ملی‌گرای کومینتانگ که در برابر تهاجم سراسری ژاپن ایستادگی کرده و جبهه وسیع آسیا را حفظ کرده است."
  },
  "PL": {
    "name_fa": "جمهوری لهستان",
    "name_en": "Poland",
    "code": "PL",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "ورشو",
    "leader": {
      "name": "ایگناتسی موشچیتسکی",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Ignacy_Mo%C5%9Bcicki_1934.jpg/480px-Ignacy_Mo%C5%9Bcicki_1934.jpg"
    },
    "flag": "https://flagcdn.com/w160/pl.png",
    "desc": "دژ شرقی اروپا در میان دو غول تمامیت‌خواه، با ارتش شجاع اما آسیب‌پذیر در برابر محاصره دوگانه."
  },
  "ES": {
    "name_fa": "اسپانیای ملی‌گرا",
    "name_en": "Spain",
    "code": "ES",
    "faction": "neutral",
    "ideology": "fascism",
    "capital": "مادرید",
    "leader": {
      "name": "فرانسیسکو فرانکو",
      "title": "کائودیلو",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Francisco_Franco_1930s.jpg/480px-Francisco_Franco_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/es.png",
    "desc": "تازه رهاشده از جنگ داخلی خونین با رویکرد فاشیستی؛ حفظ بی‌طرفی رسمی و ارسال لشکر آبی."
  },
  "PT": {
    "name_fa": "پرتغال (استادو نوو)",
    "name_en": "Portugal",
    "code": "PT",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "لیسبون",
    "leader": {
      "name": "آنتونیو سالازار",
      "title": "نخست‌وزیر",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Salazar_1940.jpg/480px-Salazar_1940.jpg"
    },
    "flag": "https://flagcdn.com/w160/pt.png",
    "desc": "حکومت مقتدر سالازار با کنترل مستعمرات ثروتمند در آنگولا و موزامبیک و حفظ موازنه بین دو بلوک."
  },
  "NL": {
    "name_fa": "پادشاهی هلند",
    "name_en": "Netherlands",
    "code": "NL",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "آمستردام",
    "leader": {
      "name": "ملکه ویلهلمینا",
      "title": "ملکه هلند",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Koningin_Wilhelmina_1942.jpg/480px-Koningin_Wilhelmina_1942.jpg"
    },
    "flag": "https://flagcdn.com/w160/nl.png",
    "desc": "کشور پیشرفته با امپراتوری غنی هند شرقی (اندونزی) سرشار از نفت و لاستیک حیاتی جنگ."
  },
  "BE": {
    "name_fa": "پادشاهی بلژیک",
    "name_en": "Belgium",
    "code": "BE",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "بروکسل",
    "leader": {
      "name": "لئوپولد سوم",
      "title": "پادشاه بلژیک",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Leopold_III_of_Belgium.jpg/480px-Leopold_III_of_Belgium.jpg"
    },
    "flag": "https://flagcdn.com/w160/be.png",
    "desc": "دروازه تاریخی دشت فلاندر با ذخایر عظیم اورانیوم و کبالت کنگوی بلژیک."
  },
  "LU": {
    "name_fa": "لوکزامبورگ",
    "name_en": "Luxembourg",
    "code": "LU",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "لوکزامبورگ",
    "leader": {
      "name": "شارلوت",
      "title": "دوک بزرگ",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Grand_Duchess_Charlotte_of_Luxembourg.jpg/480px-Grand_Duchess_Charlotte_of_Luxembourg.jpg"
    },
    "flag": "https://flagcdn.com/w160/lu.png",
    "desc": "دوک‌نشین صنعتی کوچک اما دارای یکی از قطب‌های کلیدی فولاد در غرب اروپا."
  },
  "CH": {
    "name_fa": "کنفدراسیون سوئیس",
    "name_en": "Switzerland",
    "code": "CH",
    "faction": "neutral",
    "ideology": "democracy",
    "capital": "برن",
    "leader": {
      "name": "فیلیپ اتر",
      "title": "رئیس‌جمهور کنفدراسیون",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Philipp_Etter_1938.jpg/480px-Philipp_Etter_1938.jpg"
    },
    "flag": "https://flagcdn.com/w160/ch.png",
    "desc": "دژ مستحکم آلپ با سیستم دفاع ملی ردویت و بانکداری بین‌المللی مصون از جنگ."
  },
  "SE": {
    "name_fa": "پادشاهی سوئد",
    "name_en": "Sweden",
    "code": "SE",
    "faction": "neutral",
    "ideology": "democracy",
    "capital": "استکهلم",
    "leader": {
      "name": "گوستاو پنجم",
      "title": "پادشاه سوئد",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Gustaf_V_of_Sweden_1930s.jpg/480px-Gustaf_V_of_Sweden_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/se.png",
    "desc": "تولیدکننده باکیفیت‌ترین سنگ‌آهن اروپا با دیپلماسی ماهرانه حفظ صلح در بالتیک."
  },
  "NO": {
    "name_fa": "پادشاهی نروژ",
    "name_en": "Norway",
    "code": "NO",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "اسلو",
    "leader": {
      "name": "هاکون هفتم",
      "title": "پادشاه نروژ",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Haakon_VII_1940.jpg/480px-Haakon_VII_1940.jpg"
    },
    "flag": "https://flagcdn.com/w160/no.png",
    "desc": "دارای بزرگ‌ترین ناوگان کشتیرانی تجاری جهان و آبراه‌های استراتژیک انتقال سنگ‌آهن."
  },
  "DK": {
    "name_fa": "پادشاهی دانمارک",
    "name_en": "Denmark",
    "code": "DK",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "کپنهاگ",
    "leader": {
      "name": "کریستیان دهم",
      "title": "پادشاه دانمارک",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Christian_X_1940.jpg/480px-Christian_X_1940.jpg"
    },
    "flag": "https://flagcdn.com/w160/dk.png",
    "desc": "کلیدور باریک ورود به دریای بالتیک با کنترل تنگه‌های استراتژیک اورسوند."
  },
  "FI": {
    "name_fa": "جمهوری فنلاند",
    "name_en": "Finland",
    "code": "FI",
    "faction": "neutral",
    "ideology": "democracy",
    "capital": "هلسینکی",
    "leader": {
      "name": "کارل گوستاو مانرهایم",
      "title": "مارشال فنلاند",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Mannerheim_1940.jpg/480px-Mannerheim_1940.jpg"
    },
    "flag": "https://flagcdn.com/w160/fi.png",
    "desc": "مردمان مقاوم شمالگان با خط دفاعی مستحکم مانرهایم که در جنگ زمستان حماسه‌ساز شدند."
  },
  "EE": {
    "name_fa": "جمهوری استونی",
    "name_en": "Estonia",
    "code": "EE",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "تالین",
    "leader": {
      "name": "کنستانتین پاتس",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Konstantin_P%C3%A4ts_1930s.jpg/480px-Konstantin_P%C3%A4ts_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/ee.png",
    "desc": "دولت ساحلی خلیج فنلاند با موقعیت مشرف بر خطوط دریایی لنینگراد."
  },
  "LV": {
    "name_fa": "جمهوری لتونی",
    "name_en": "Latvia",
    "code": "LV",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "ریگا",
    "leader": {
      "name": "کارلیس اولمانیس",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/K%C4%81rlis_Ulmanis_1934.jpg/480px-K%C4%81rlis_Ulmanis_1934.jpg"
    },
    "flag": "https://flagcdn.com/w160/lv.png",
    "desc": "بندر تجاری مهم بالتیک با موقعیت حائل میان قدرت‌های شرق و غرب."
  },
  "LT": {
    "name_fa": "جمهوری لیتوانی",
    "name_en": "Lithuania",
    "code": "LT",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "ویلنیوس",
    "leader": {
      "name": "آنتاناس اسمتونا",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Antanas_Smetona_1930s.jpg/480px-Antanas_Smetona_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/lt.png",
    "desc": "کشور تاریخی بالتیک هم‌مرز با پروس شرقی و ورشو."
  },
  "RO": {
    "name_fa": "پادشاهی رومانی",
    "name_en": "Romania",
    "code": "RO",
    "faction": "axis",
    "ideology": "fascism",
    "capital": "بخارست",
    "leader": {
      "name": "یون آنتونسکو",
      "title": "کوندوکاتور رومانی",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Ion_Antonescu_1941.jpg/480px-Ion_Antonescu_1941.jpg"
    },
    "flag": "https://flagcdn.com/w160/ro.png",
    "desc": "چاه‌های نفت استراتژیک پلویشتی که شریان حیاتی سوخت تانک‌ها و هواپیماهای محور محسوب می‌شد."
  },
  "HU": {
    "name_fa": "پادشاهی مجارستان",
    "name_en": "Hungary",
    "code": "HU",
    "faction": "axis",
    "ideology": "fascism",
    "capital": "بوداپست",
    "leader": {
      "name": "میکلوش هورتی",
      "title": "نایب‌السلطنه",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Mikl%C3%B3s_Horthy_1930s.jpg/480px-Mikl%C3%B3s_Horthy_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/hu.png",
    "desc": "پادشاهی بدون پادشاه به رهبری یک دریادار با ارتش مجار و صنایع تسلیحاتی کارپات."
  },
  "BG": {
    "name_fa": "پادشاهی بلغارستان",
    "name_en": "Bulgaria",
    "code": "BG",
    "faction": "axis",
    "ideology": "neutral",
    "capital": "صوفیه",
    "leader": {
      "name": "بوریس سوم",
      "title": "تزار بلغارستان",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Tsar_Boris_III_1930s.jpg/480px-Tsar_Boris_III_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/bg.png",
    "desc": "گرانیگاه شبه‌جزیره بالکان و پیونددهنده خطوط آهن اروپا با تنگه‌های ترکیه."
  },
  "YU": {
    "name_fa": "پادشاهی یوگسلاوی",
    "name_en": "Yugoslavia",
    "code": "YU",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "بلگراد",
    "leader": {
      "name": "شاهزاده پاول",
      "title": "نایب‌السلطنه",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Prince_Paul_of_Yugoslavia_1930s.jpg/480px-Prince_Paul_of_Yugoslavia_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/rs.png",
    "desc": "پادشاهی اسلاوهای جنوبی با کوهستان‌های سرسخت و هسته پارتیزان‌های آینده."
  },
  "GR": {
    "name_fa": "پادشاهی یونان",
    "name_en": "Greece",
    "code": "GR",
    "faction": "allies",
    "ideology": "neutral",
    "capital": "آتن",
    "leader": {
      "name": "یوانیس متاکساس",
      "title": "نخست‌وزیر",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Ioannis_Metaxas_1938.jpg/480px-Ioannis_Metaxas_1938.jpg"
    },
    "flag": "https://flagcdn.com/w160/gr.png",
    "desc": "دلاوران هلنی با ارتش سرسخت که تهاجم اولیه فاشیست‌های ایتالیا را در کوه‌های آلبانی درهم شکستند."
  },
  "AL": {
    "name_fa": "پادشاهی آلبانی",
    "name_en": "Albania",
    "code": "AL",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "تیرانا",
    "leader": {
      "name": "زوگ یکم",
      "title": "پادشاه آلبانی",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/King_Zog_I_of_Albania.jpg/480px-King_Zog_I_of_Albania.jpg"
    },
    "flag": "https://flagcdn.com/w160/al.png",
    "desc": "پادشاهی بالکان در سواحل آدریاتیک که در بهار ۱۹۳۹ تحت اشغال ارتش ایتالیا قرار گرفت."
  },
  "IE": {
    "name_fa": "جمهوری ایرلند",
    "name_en": "Ireland",
    "code": "IE",
    "faction": "neutral",
    "ideology": "democracy",
    "capital": "دوبلین",
    "leader": {
      "name": "ایمون دی والرا",
      "title": "نخست‌وزیر",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/%C3%89amon_de_Valera_1930s.jpg/480px-%C3%89amon_de_Valera_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/ie.png",
    "desc": "جزیره سبز با سیاست اعلامی اضطراری و بی‌طرفی رسمی در نبرد اقیانوس اطلس."
  },
  "IS": {
    "name_fa": "پادشاهی ایسلند",
    "name_en": "Iceland",
    "code": "IS",
    "faction": "neutral",
    "ideology": "democracy",
    "capital": "ریکیاویک",
    "leader": {
      "name": "کریستیان دهم",
      "title": "پادشاه",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Christian_X_1940.jpg/480px-Christian_X_1940.jpg"
    },
    "flag": "https://flagcdn.com/w160/is.png",
    "desc": "پایگاه راهبردی میانه اقیانوس اطلس و دیده‌بان کاروان‌های دریایی متفقین."
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
  "IR": {
    "name_fa": "شاهنشاهی ایران",
    "name_en": "Iran",
    "code": "IR",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "تهران",
    "leader": {
      "name": "رضاشاه پهلوی",
      "title": "شاهنشاه ایران",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Reza_Shah_Pahlavi_1930s.jpg/480px-Reza_Shah_Pahlavi_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/ir.png",
    "desc": "پل پیروزی با راه‌آهن سراسری نوساز، نفت آبادان، موقعیت ژئوپلیتیک بی‌نظیر و سیاست حفظ بی‌طرفی."
  },
  "TR": {
    "name_fa": "جمهوری ترکیه",
    "name_en": "Turkey",
    "code": "TR",
    "faction": "neutral",
    "ideology": "democracy",
    "capital": "آنکارا",
    "leader": {
      "name": "عصمت اینونو",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/%C4%B0smet_%C4%B0n%C3%B6n%C3%BC_1939.jpg/480px-%C4%B0smet_%C4%B0n%C3%B6n%C3%BC_1939.jpg"
    },
    "flag": "https://flagcdn.com/w160/tr.png",
    "desc": "وارث امپراتوری عثمانی با کنترل تنگه‌های استراتژیک بسفر و داردانل و منابع حیاتی کرومیت."
  },
  "IQ": {
    "name_fa": "پادشاهی عراق",
    "name_en": "Iraq",
    "code": "IQ",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "بغداد",
    "leader": {
      "name": "فیصل دوم",
      "title": "پادشاه عراق",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Faisal_II_of_Iraq_child.jpg/480px-Faisal_II_of_Iraq_child.jpg"
    },
    "flag": "https://flagcdn.com/w160/iq.png",
    "desc": "مرکز میادین نفتی کرکوک و بصره با گرایش‌های ملی‌گرایانه ضدانگلیسی به رهبری رشید عالی گیلانی."
  },
  "SA": {
    "name_fa": "پادشاهی عربستان سعودی",
    "name_en": "Saudi Arabia",
    "code": "SA",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "ریاض",
    "leader": {
      "name": "عبدالعزیز آل سعود",
      "title": "پادشاه",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Ibn_Saud_1930s.jpg/480px-Ibn_Saud_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/sa.png",
    "desc": "سرزمین حرمین شریفین با کشف نخستین فوران‌های عظیم نفتی در دهان در سال ۱۹۳۸."
  },
  "YE": {
    "name_fa": "پادشاهی متوکلی یمن",
    "name_en": "Yemen",
    "code": "YE",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "صنعا",
    "leader": {
      "name": "یحیی حمیدالدین",
      "title": "امام و پادشاه یمن",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Imam_Yahya_1930s.jpg/480px-Imam_Yahya_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/ye.png",
    "desc": "پادشاهی سنتی زیدی بر فراز بلندی‌های مشرف به آبراهه تنگه باب‌المندب و دریای سرخ."
  },
  "OM": {
    "name_fa": "سلطنت مسقط و عمان",
    "name_en": "Oman",
    "code": "OM",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "مسقط",
    "leader": {
      "name": "سعید بن تیمور",
      "title": "سلطان عمان",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Said_bin_Taimur_1940s.jpg/480px-Said_bin_Taimur_1940s.jpg"
    },
    "flag": "https://flagcdn.com/w160/om.png",
    "desc": "سلطنت ساحلی در خلیج عمان و اقیانوس هند با سواحل استراتژیک در دریای عرب."
  },
  "AF": {
    "name_fa": "پادشاهی افغانستان",
    "name_en": "Afghanistan",
    "code": "AF",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "کابل",
    "leader": {
      "name": "محمد ظاهرشاه",
      "title": "پادشاه افغانستان",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Zahir_Shah_1930s.jpg/480px-Zahir_Shah_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/af.png",
    "desc": "دولت حائل کوهستانی در چهارراه آسیای میانه و هندوستان با تعهد سرسختانه به بی‌طرفی کامل."
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
  "MN": {
    "name_fa": "جمهوری خلق مغولستان",
    "name_en": "Mongolia",
    "code": "MN",
    "faction": "comintern",
    "ideology": "communism",
    "capital": "اولان‌باتور",
    "leader": {
      "name": "خورلوگین چویبالسان",
      "title": "مارشال مغولستان",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Khorloogiin_Choibalsan_1939.jpg/480px-Khorloogiin_Choibalsan_1939.jpg"
    },
    "flag": "https://flagcdn.com/w160/mn.png",
    "desc": "متحد سرسخت ارتش سرخ که در نبرد خالخین‌گل ۱۹۳۹ شکست سنگینی به ارتش کوانتونگ ژاپن وارد کرد."
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
  "TH": {
    "name_fa": "پادشاهی تایلند (سیام)",
    "name_en": "Thailand",
    "code": "TH",
    "faction": "axis",
    "ideology": "fascism",
    "capital": "بانکوک",
    "leader": {
      "name": "پلاک فیبونسونگکرام",
      "title": "نخست‌وزیر",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Plaek_Phibunsongkhram_1940.jpg/480px-Plaek_Phibunsongkhram_1940.jpg"
    },
    "flag": "https://flagcdn.com/w160/th.png",
    "desc": "تنها کشور مستقل جنوب شرق آسیا با گرایش نظامی‌گری مدرن و همکاری استراتژیک با ژاپن."
  },
  "TB": {
    "name_fa": "تبت بزرگ",
    "name_en": "Tibet",
    "code": "TB",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "لهاسا",
    "leader": {
      "name": "تنزین گیاتسو (دالایی لاما)",
      "title": "رهبر مذهبی و سیاسی",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/14th_Dalai_Lama_as_a_child.jpg/480px-14th_Dalai_Lama_as_a_child.jpg"
    },
    "flag": "https://flagcdn.com/w160/cn.png",
    "desc": "سرزمین مقدس در بام جهان در هیمالیا با سنت‌های بودایی هزارساله و بی‌طرفی کوهستانی."
  },
  "NP": {
    "name_fa": "پادشاهی نپال",
    "name_en": "Nepal",
    "code": "NP",
    "faction": "allies",
    "ideology": "neutral",
    "capital": "کاتماندو",
    "leader": {
      "name": "جودا شومشر رانا",
      "title": "نخست‌وزیر مهاراجه",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Juddha_Shumsher_Jung_Bahadur_Rana.jpg/480px-Juddha_Shumsher_Jung_Bahadur_Rana.jpg"
    },
    "flag": "https://flagcdn.com/w160/np.png",
    "desc": "زادگاه جنگجویان افسانه‌ای گورخا که شجاعت آنان در جبهه‌های جنگ جهانی دوم زبانزد تاریخ شد."
  },
  "BT": {
    "name_fa": "پادشاهی بوتان",
    "name_en": "Bhutan",
    "code": "BT",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "تیمفو",
    "leader": {
      "name": "جیگمه وانگچوک",
      "title": "پادشاه بوتان",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Jigme_Wangchuck.jpg/480px-Jigme_Wangchuck.jpg"
    },
    "flag": "https://flagcdn.com/w160/bt.png",
    "desc": "پادشاهی اژدهای تندر در کوه‌های شرقی هیمالیا در آرامش و انزوای طبیعی."
  },
  "IN": {
    "name_fa": "راج بریتانیا (هند)",
    "name_en": "British India",
    "code": "IN",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "دهلی نو",
    "leader": {
      "name": "ویکتور هوپ (لینلیثگو)",
      "title": "فرماندار کل هند",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Lord_Linlithgow_1930s.jpg/480px-Lord_Linlithgow_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/in.png",
    "desc": "بزرگ‌ترین پایگاه انسانی و ارتش داوطلب امپراتوری بریتانیا با بیش از ۲.۵ میلیون سرباز در نبردها."
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
  },
  "PH": {
    "name_fa": "مشترک‌المنافع فیلیپین",
    "name_en": "Philippines",
    "code": "PH",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "مانیل",
    "leader": {
      "name": "مانوئل کوئزون",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Manuel_L_Quezon_1930s.jpg/480px-Manuel_L_Quezon_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/ph.png",
    "desc": "مجمع‌الجزایر استراتژیک در اقیانوس آرام تحت پیمان مشترک با آمریکا و فرماندهی ژنرال مک‌آرتور."
  },
  "CA": {
    "name_fa": "دومینیون کانادا",
    "name_en": "Canada",
    "code": "CA",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "اتاوا",
    "leader": {
      "name": "ویلیام لیون مکنزی کینگ",
      "title": "نخست‌وزیر",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Mackenzie_King_1930s.jpg/480px-Mackenzie_King_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/ca.png",
    "desc": "عظیم‌ترین تأمین‌کننده گندم، نیکل، آلومینیوم و کاروان‌های اسکورت کشتی‌ها در نبرد اطلس."
  },
  "MX": {
    "name_fa": "ایالات متحده مکزیک",
    "name_en": "Mexico",
    "code": "MX",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "مکزیکوسیتی",
    "leader": {
      "name": "لازارو کاردناس",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/L%C3%A1zaro_C%C3%A1rdenas_1938.jpg/480px-L%C3%A1zaro_C%C3%A1rdenas_1938.jpg"
    },
    "flag": "https://flagcdn.com/w160/mx.png",
    "desc": "دولت ملی‌گرا با ملی کردن صنعت نفت در ۱۹۳۸ و اسکادران هوایی مشهور ۲۰۱ آزتک در جنگ."
  },
  "BR": {
    "name_fa": "جمهوری برزیل (استادو نوو)",
    "name_en": "Brazil",
    "code": "BR",
    "faction": "allies",
    "ideology": "neutral",
    "capital": "ریودوژانیرو",
    "leader": {
      "name": "ژتولیو وارگاس",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Getulio_Vargas_1930.jpg/480px-Getulio_Vargas_1930.jpg"
    },
    "flag": "https://flagcdn.com/w160/br.png",
    "desc": "بزرگ‌ترین قدرت آمریکای جنوبی با اعزام نیروی اعزامی قهرمان برزیل (FEB) به کارزار ایتالیا."
  },
  "AR": {
    "name_fa": "جمهوری آرژانتین",
    "name_en": "Argentina",
    "code": "AR",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "بوئنوس آیرس",
    "leader": {
      "name": "روبرتو ماریا اورتیز",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Roberto_M_Ortiz_1938.jpg/480px-Roberto_M_Ortiz_1938.jpg"
    },
    "flag": "https://flagcdn.com/w160/ar.png",
    "desc": "انبار غله و گوشت قاره با نفوذ گسترده جوامع اروپایی و رویکرد دیپلماتیک مستقل."
  },
  "CL": {
    "name_fa": "جمهوری شیلی",
    "name_en": "Chile",
    "code": "CL",
    "faction": "neutral",
    "ideology": "democracy",
    "capital": "سانتیاگو",
    "leader": {
      "name": "پدرو آگیره سردا",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Pedro_Aguirre_Cerda_1938.jpg/480px-Pedro_Aguirre_Cerda_1938.jpg"
    },
    "flag": "https://flagcdn.com/w160/cl.png",
    "desc": "نوار ساحلی اقیانوس آرام با عظیم‌ترین معادن مس و نیترات حیاتی برای باروت جنگی."
  },
  "CO": {
    "name_fa": "جمهوری کلمبیا",
    "name_en": "Colombia",
    "code": "CO",
    "faction": "neutral",
    "ideology": "democracy",
    "capital": "بوگوتا",
    "leader": {
      "name": "ادواردو سانتوس",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Eduardo_Santos_1938.jpg/480px-Eduardo_Santos_1938.jpg"
    },
    "flag": "https://flagcdn.com/w160/co.png",
    "desc": "دروازه آمریکای جنوبی مشرف به هر دو اقیانوس آرام و اطلس در نزدیکی کانال پاناما."
  },
  "PE": {
    "name_fa": "جمهوری پرو",
    "name_en": "Peru",
    "code": "PE",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "لیما",
    "leader": {
      "name": "مانوئل پرادو اوگارتچه",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Manuel_Prado_Ugarteche_1939.jpg/480px-Manuel_Prado_Ugarteche_1939.jpg"
    },
    "flag": "https://flagcdn.com/w160/pe.png",
    "desc": "کشور باستانی اینکا در آند با بنادر راهبردی در کرانه اقیانوس کبیر."
  },
  "VE": {
    "name_fa": "ایالات متحده ونزوئلا",
    "name_en": "Venezuela",
    "code": "VE",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "کاراکاس",
    "leader": {
      "name": "الازار لوپز کنتراس",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Eleazar_L%C3%B3pez_Contreras_1936.jpg/480px-Eleazar_L%C3%B3pez_Contreras_1936.jpg"
    },
    "flag": "https://flagcdn.com/w160/ve.png",
    "desc": "برترین صادرکننده نفت در دریای کارائیب و سوخت‌رسان کلیدی ناوگان‌های دریایی متفقین."
  },
  "BO": {
    "name_fa": "جمهوری بولیوی",
    "name_en": "Bolivia",
    "code": "BO",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "لاپاز",
    "leader": {
      "name": "کارلوس کینتانیلا",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Carlos_Quintanilla_1939.jpg/480px-Carlos_Quintanilla_1939.jpg"
    },
    "flag": "https://flagcdn.com/w160/bo.png",
    "desc": "فلات مرتفع آند با معادن حیاتی قلع برای تولید ظروف آذوقه و قطعات نظامی."
  },
  "PY": {
    "name_fa": "جمهوری پاراگوئه",
    "name_en": "Paraguay",
    "code": "PY",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "آسونسیون",
    "leader": {
      "name": "خوزه فلیکس استیگاریبیا",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Jose_Felix_Estigarribia_1939.jpg/480px-Jose_Felix_Estigarribia_1939.jpg"
    },
    "flag": "https://flagcdn.com/w160/py.png",
    "desc": "قهرمان جنگ چاکو در قلب آمریکای جنوبی با ارتشی آموزش‌دیده و باانگیزه."
  },
  "UY": {
    "name_fa": "جمهوری اروگوئه",
    "name_en": "Uruguay",
    "code": "UY",
    "faction": "neutral",
    "ideology": "democracy",
    "capital": "مونته‌ویدئو",
    "leader": {
      "name": "آلفردو بالدومیر",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Alfredo_Baldomir_1938.jpg/480px-Alfredo_Baldomir_1938.jpg"
    },
    "flag": "https://flagcdn.com/w160/uy.png",
    "desc": "سواحل ریو د لا پلاتا و محل وقوع نخستین نبرد دریایی بزرگ جنگ جهانی دوم (رزم‌ناو گراف اشپی)."
  },
  "EC": {
    "name_fa": "جمهوری اکوادور",
    "name_en": "Ecuador",
    "code": "EC",
    "faction": "neutral",
    "ideology": "democracy",
    "capital": "کیتو",
    "leader": {
      "name": "آئورلیو موسکرا ناربائز",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Aurelio_Mosquera_1938.jpg/480px-Aurelio_Mosquera_1938.jpg"
    },
    "flag": "https://flagcdn.com/w160/ec.png",
    "desc": "نگهبان جزایر گالاپاگوس با موقعیت بی‌نظیر برای پایش مسیرهای دریایی کارائیب."
  },
  "CU": {
    "name_fa": "جمهوری کوبا",
    "name_en": "Cuba",
    "code": "CU",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "هاوانا",
    "leader": {
      "name": "فدریکو لاردو برو",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Federico_Laredo_Bru_1936.jpg/480px-Federico_Laredo_Bru_1936.jpg"
    },
    "flag": "https://flagcdn.com/w160/cu.png",
    "desc": "بزرگ‌ترین جزیره کارائیب و پایگاه کلیدی گشت‌زنی ضدزیردریایی در خلیج مکزیک."
  },
  "GT": {
    "name_fa": "جمهوری گواتمالا",
    "name_en": "Guatemala",
    "code": "GT",
    "faction": "neutral",
    "ideology": "fascism",
    "capital": "گواتمالاسیتی",
    "leader": {
      "name": "خورخه اوبیکو",
      "title": "رئیس‌جمهور دیکتاتور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Jorge_Ubico_1930s.jpg/480px-Jorge_Ubico_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/gt.png",
    "desc": "حکومت نظامی باثبات در آمریکای مرکزی با کنترل مزارع وسیع و فرودگاه‌های استراتژیک."
  },
  "HN": {
    "name_fa": "جمهوری هندوراس",
    "name_en": "Honduras",
    "code": "HN",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "تگوسیگالپا",
    "leader": {
      "name": "تیبورسیو کاریاس آندینو",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Tiburcio_Carias_1933.jpg/480px-Tiburcio_Carias_1933.jpg"
    },
    "flag": "https://flagcdn.com/w160/hn.png",
    "desc": "جمهوری ساحلی کارائیب با معادن نقره و تولید محصولات کشاورزی راهبردی."
  },
  "SV": {
    "name_fa": "جمهوری السالوادور",
    "name_en": "El Salvador",
    "code": "SV",
    "faction": "neutral",
    "ideology": "fascism",
    "capital": "سان سالوادور",
    "leader": {
      "name": "ماکسیمیلیانو هرناندز مارتینز",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Maximiliano_Hernandez_Martinez.jpg/480px-Maximiliano_Hernandez_Martinez.jpg"
    },
    "flag": "https://flagcdn.com/w160/sv.png",
    "desc": "حکومت اقتدارگرا با روابط نزدیک اولیه با نیروهای محور و سپس پیوستن به جبهه ضدنازی."
  },
  "NI": {
    "name_fa": "جمهوری نیکاراگوئه",
    "name_en": "Nicaragua",
    "code": "NI",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "ماناگوآ",
    "leader": {
      "name": "آناستاسیو سوموزا گارسیا",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Anastasio_Somoza_Garcia_1930s.jpg/480px-Anastasio_Somoza_Garcia_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/ni.png",
    "desc": "مسیر بالقوه کانال دوم میان‌اقیانوسی با گارد ملی وفادار به حکومت."
  },
  "CR": {
    "name_fa": "جمهوری کاستاریکا",
    "name_en": "Costa Rica",
    "code": "CR",
    "faction": "neutral",
    "ideology": "democracy",
    "capital": "سان خوزه",
    "leader": {
      "name": "لئون کورتس کاسترو",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Leon_Cortes_Castro_1936.jpg/480px-Leon_Cortes_Castro_1936.jpg"
    },
    "flag": "https://flagcdn.com/w160/cr.png",
    "desc": "دموکراسی صلح‌طلب با سنت دیرینه عدم مداخله نظامی در آمریکای مرکزی."
  },
  "PA": {
    "name_fa": "جمهوری پاناما",
    "name_en": "Panama",
    "code": "PA",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "پاناماسیتی",
    "leader": {
      "name": "آگوستو ساموئل بوید",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Augusto_Samuel_Boyd_1939.jpg/480px-Augusto_Samuel_Boyd_1939.jpg"
    },
    "flag": "https://flagcdn.com/w160/pa.png",
    "desc": "صاحب حیاتی‌ترین آبراهه نظامی جهان (کانال پاناما) که اتصال دو اقیانوس را تضمین می‌کرد."
  },
  "DO": {
    "name_fa": "جمهوری دومینیکن",
    "name_en": "Dominican Republic",
    "code": "DO",
    "faction": "neutral",
    "ideology": "fascism",
    "capital": "سانتو دومینگو",
    "leader": {
      "name": "رافائل تروخیو",
      "title": "دیکتاتور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Rafael_Trujillo_1930s.jpg/480px-Rafael_Trujillo_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/do.png",
    "desc": "دیکتاتوری جزیره‌ای با ارتش وفادار و پایگاه‌های دفاع ساحلی در کارائیب."
  },
  "HT": {
    "name_fa": "جمهوری هائیتی",
    "name_en": "Haiti",
    "code": "HT",
    "faction": "neutral",
    "ideology": "neutral",
    "capital": "پورتو پرنس",
    "leader": {
      "name": "استنیو ونسان",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Stenio_Vincent_1930s.jpg/480px-Stenio_Vincent_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/ht.png",
    "desc": "نخستین جمهوری سیاه‌پوستان در قاره آمریکا با موقعیت نگهبانی از گذرگاه ویند وارد."
  },
  "EG": {
    "name_fa": "پادشاهی مصر",
    "name_en": "Egypt",
    "code": "EG",
    "faction": "allies",
    "ideology": "neutral",
    "capital": "قاهره",
    "leader": {
      "name": "فاروق یکم",
      "title": "پادشاه مصر و سودان",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/King_Farouk_1937.jpg/480px-King_Farouk_1937.jpg"
    },
    "flag": "https://flagcdn.com/w160/eg.png",
    "desc": "کلید حیاتی کانال سوئز و سنگر اصلی دفاع از خاورمیانه در برابر سپاه آفریقای رومل."
  },
  "ET": {
    "name_fa": "امپراتوری اتیوپی",
    "name_en": "Ethiopia",
    "code": "ET",
    "faction": "allies",
    "ideology": "neutral",
    "capital": "آدیس آبابا",
    "leader": {
      "name": "هایله سلاسی",
      "title": "امپراتور اتیوپی",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Haile_Selassie_1930s.jpg/480px-Haile_Selassie_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/et.png",
    "desc": "نماد استقامت آفریقا در شاخ آفریقا با رزمندگان وطن‌پرست در کوهستان‌ها علیه اشغالگران."
  },
  "LR": {
    "name_fa": "جمهوری لیبریا",
    "name_en": "Liberia",
    "code": "LR",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "مونروویا",
    "leader": {
      "name": "ادوین بارکلی",
      "title": "رئیس‌جمهور",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Edwin_Barclay_1930s.jpg/480px-Edwin_Barclay_1930s.jpg"
    },
    "flag": "https://flagcdn.com/w160/lr.png",
    "desc": "تأمین‌کننده بلامنازع کائوچو و لاستیک طبیعی تایرهای هواپیماهای جنگی متفقین."
  },
  "ZA": {
    "name_fa": "اتحادیه آفریقای جنوبی",
    "name_en": "South Africa",
    "code": "ZA",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "پرتوریا",
    "leader": {
      "name": "یان اسموتس",
      "title": "نخست‌وزیر",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Jan_Smuts_1940.jpg/480px-Jan_Smuts_1940.jpg"
    },
    "flag": "https://flagcdn.com/w160/za.png",
    "desc": "بزرگ‌ترین تولیدکننده طلای جهان و پشتیبان ناوگان‌ها در گذرگاه دماغه امید نیک."
  },
  "AU": {
    "name_fa": "مشترک‌المنافع استرالیا",
    "name_en": "Australia",
    "code": "AU",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "کانبرا",
    "leader": {
      "name": "رابرت منزیس",
      "title": "نخست‌وزیر",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Robert_Menzies_1939.jpg/480px-Robert_Menzies_1939.jpg"
    },
    "flag": "https://flagcdn.com/w160/au.png",
    "desc": "دژ مستحکم اقیانوسیه و ارتش قهرمان آنزاک در جبهه‌های شمال آفریقا و نبرد گینه نو."
  },
  "NZ": {
    "name_fa": "دومینیون نیوزیلند",
    "name_en": "New Zealand",
    "code": "NZ",
    "faction": "allies",
    "ideology": "democracy",
    "capital": "ولینگتون",
    "leader": {
      "name": "مایکل جوزف ساویج",
      "title": "نخست‌وزیر",
      "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Michael_Joseph_Savage_1935.jpg/480px-Michael_Joseph_Savage_1935.jpg"
    },
    "flag": "https://flagcdn.com/w160/nz.png",
    "desc": "نخستین کشوری که دوشادوش بریتانیا اعلان جنگ داد با داوطلبان دلاور مائوری و لشکر دوم پیاده."
  }
}

COUNTRY_CODES = list(COUNTRIES.keys())

DEFAULT_MUSIC_URL = "https://upload.wikimedia.org/wikipedia/commons/4/4e/Holst_The_Planets_Mars_the_Bringer_of_War_USAF_Band.ogg"
