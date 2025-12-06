# data/themes_data.py
# Gamma API Theme'lar ma'lumotlari
# ✅ HAQIQIY ID'lar - lowercase, tire bilan
# Gamma API dan olingan: GET /v1.0/themes

THEMES = [
    {
        "id": "chisel",  # ✅ TO'G'RI
        "name": "Chisel",
        "emoji": "🤍",
        "description": "Oq, minimalist, professional. Biznes va korporativ prezentatsiyalar uchun ideal.",
        "file_id": "AgACAgIAAxkBAAKXbmk0WZ-6kjEbLwfjDqI-9PSmxMAaAAJ-EGsbzqGhSeFY-yoQFlzQAQADAgADbQADNgQ"
    },
    {
        "id": "coal",  # ✅ TO'G'RI (Vortex o'rniga)
        "name": "Coal",
        "emoji": "🖤",
        "description": "Qora, elegant, zamonaviy. Premium va tech loyihalar uchun.",
        "file_id": "AgACAgIAAxkBAAKXzWk0WclCQCnCuTpCQUVrIcJkwMGaAAKBEGsbzqGhSdLGB0P9TU2LAQADAgADbQADNgQ"
    },
    {
        "id": "blues",  # ✅ TO'G'RI (Stratos o'rniga)
        "name": "Blues",
        "emoji": "🔵",
        "description": "To'q ko'k, ishonchli, korporativ. Rasmiy taqdimotlar uchun.",
        "file_id": "AgACAgIAAxkBAAKYNmk0WfF5sUgnBkz9UolZ5yZeLu8mAAKDEGsbzqGhSfx12B4l1kqqAQADAgADbQADNgQ"
    },
    {
        "id": "elysia",  # ✅ TO'G'RI (Prism o'rniga)
        "name": "Elysia",
        "emoji": "💗",
        "description": "Och pushti, ijodiy, yengil. Marketing va ijodiy loyihalar uchun.",
        "file_id": "AgACAgIAAxkBAAKYRmk0Whmxdm2alcaNQFm9tgTxIsAyAAKFEGsbzqGhSR4KYtOEwRPNAQADAgADbQADNgQ"
    },
    {
        "id": "breeze",  # ✅ TO'G'RI (Seafoam o'rniga)
        "name": "Breeze",
        "emoji": "🌊",
        "description": "Moviy-yashil, tinch, tabiiy. Ekologiya va sog'liqni saqlash uchun.",
        "file_id": "AgACAgIAAxkBAAKYUGk0WjdzsPq0fUzNXYDcLqUO-oBDAAKIEGsbzqGhSWsiyRQBlsMUAQADAgADbQADNgQ"
    },
    {
        "id": "aurora",  # ✅ TO'G'RI (Night Sky o'rniga)
        "name": "Aurora",
        "emoji": "🌙",
        "description": "To'q binafsha, sirli, premium. Startup va innovatsion loyihalar uchun.",
        "file_id": "AgACAgIAAxkBAAKYX2k0Wl6VaSyQykACJ9mrF8SWJZkMAAKLEGsbzqGhSVCIyapaNnpfAQADAgADbQADNgQ"
    },
    {
        "id": "coral-glow",  # ✅ TO'G'RI
        "name": "Coral Glow",
        "emoji": "🌸",
        "description": "Pushti gradient, iliq, do'stona. Lifestyle va ijtimoiy loyihalar uchun.",
        "file_id": "AgACAgIAAxkBAAKYb2k0WotTBV46gnJwPBI1BMg-PdVbAAKMEGsbzqGhSYtdze2k92WhAQADAgADbQADNgQ"
    },
    {
        "id": "gamma",  # ✅ TO'G'RI (Spectrum o'rniga)
        "name": "Gamma",
        "emoji": "🌈",
        "description": "Rang-barang, quvnoq, ijodiy. Ta'lim va bolalar loyihalari uchun.",
        "file_id": "AgACAgIAAxkBAAKY4mk0Wq5HdVo2seUAARpl1UdI2JGVUgACjRBrG86hoUniONcZN6A4CwEAAwIAA20AAzYE"
    },
    {
        "id": "creme",  # ✅ TO'G'RI
        "name": "Creme",
        "emoji": "☕",
        "description": "Krem, iliq, klassik. Restoran, qahvaxona va lifestyle uchun.",
        "file_id": "AgACAgIAAxkBAAKY_Wk0W0DzWeNq_vYgUDQqe8L7qr8xAAKTEGsbzqGhSa9TUbdjFzQwAQADAgADbQADNgQ"
    },
    {
        "id": "gamma-dark",  # ✅ TO'G'RI (Nebulae o'rniga)
        "name": "Gamma Dark",
        "emoji": "✨",
        "description": "Kosmik, qorong'i, effektli. Tech va futuristik loyihalar uchun.",
        "file_id": "AgACAgIAAxkBAAKY-2k0Wx7eZX0o8oRqPwYi0GsdsISbAAKREGsbzqGhSR1XydQDLyI2AQADAgADbQADNgQ"
    }
]


def get_theme_by_id(theme_id: str) -> dict:
    """Theme ID bo'yicha olish"""
    if not theme_id:
        return None
    # Case-insensitive search
    theme_id_lower = theme_id.lower()
    for theme in THEMES:
        if theme['id'].lower() == theme_id_lower:
            return theme
    return None


def get_theme_by_index(index: int) -> dict:
    """Index bo'yicha theme olish"""
    if 0 <= index < len(THEMES):
        return THEMES[index]
    return None


def get_all_themes() -> list:
    """Barcha theme'larni olish"""
    return THEMES


def get_themes_count() -> int:
    """Theme'lar sonini olish"""
    return len(THEMES)


def get_theme_name(theme_id: str) -> str:
    """Theme nomini olish"""
    theme = get_theme_by_id(theme_id)
    if theme:
        return theme['name']
    return "Standart"


def get_theme_emoji(theme_id: str) -> str:
    """Theme emoji'sini olish"""
    theme = get_theme_by_id(theme_id)
    if theme:
        return theme['emoji']
    return "🎨"