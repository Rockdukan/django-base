"""
Настройки карты сайта (sitemap) для Django

Компонент отвечает за:
1. Генерацию XML-карты сайта
2. Настройку частоты обновления и приоритета страниц
3. Интеграцию с поисковыми системами
4. Поддержку динамического создания карты сайта
"""

import os

getenv = os.getenv

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ SITEMAP -------------------

# Базовый URL для sitemap (если не указан, будет использоваться
# SITE_ID из django.contrib.sites)
SITEMAP_BASE_URL = getenv("SITEMAP_BASE_URL", "")

# Включить автоматическую отправку sitemap в поисковые системы при изменении
SITEMAP_AUTO_PING = getenv("SITEMAP_AUTO_PING", "True") == "True"

# Список поисковых систем для отправки sitemap
SITEMAP_PING_SEARCH_ENGINES = [
    "https://www.google.com/webmasters/tools/ping?sitemap=%s",
    "https://search.yahoo.com/ping?sitemap=%s",
    "https://www.bing.com/ping?sitemap=%s",
]

# Частота кэширования sitemap (в секундах)
SITEMAP_CACHE_TIMEOUT = int(getenv("SITEMAP_CACHE_TIMEOUT", 86400))

# ---------------- НАСТРОЙКИ ПРИОРИТЕТОВ И ЧАСТОТЫ ОБНОВЛЕНИЯ -----------------

# Настройки по умолчанию для сущностей в sitemap
SITEMAP_DEFAULT_CHANGEFREQ = getenv("SITEMAP_DEFAULT_CHANGEFREQ", "weekly")
SITEMAP_DEFAULT_PRIORITY = float(getenv("SITEMAP_DEFAULT_PRIORITY", 0.5))

# Настройки для разных типов страниц
SITEMAP_PRIORITIES = {
    "main": float(getenv("SITEMAP_PRIORITY_MAIN", 1.0)),
    "category": float(getenv("SITEMAP_PRIORITY_CATEGORY", 0.8)),
    "product": float(getenv("SITEMAP_PRIORITY_PRODUCT", 0.6)),
    "article": float(getenv("SITEMAP_PRIORITY_ARTICLE", 0.7)),
    "page": float(getenv("SITEMAP_PRIORITY_PAGE", 0.5)),
}

SITEMAP_CHANGEFREQS = {
    "main": getenv("SITEMAP_CHANGEFREQ_MAIN", "daily"),
    "category": getenv("SITEMAP_CHANGEFREQ_CATEGORY", "weekly"),
    "product": getenv("SITEMAP_CHANGEFREQ_PRODUCT", "daily"),
    "article": getenv("SITEMAP_CHANGEFREQ_ARTICLE", "weekly"),
    "page": getenv("SITEMAP_CHANGEFREQ_PAGE", "monthly"),
}

# ------------------ НАСТРОЙКИ ЛОКАЛИЗАЦИИ -------------------

# Включить поддержку нескольких языков в sitemap
SITEMAP_I18N_ENABLED = getenv("SITEMAP_I18N_ENABLED", "False") == "True"

# ------------------ НАСТРОЙКИ DJANGO-SITEMAP-EXTENSION -------------------

# Включить django-sitemap-extension для расширенных возможностей
SITEMAP_EXTENSION_ENABLED = getenv("SITEMAP_EXTENSION_ENABLED", "False") == "True"

# Путь к карте сайта
SITEMAP_URL = getenv("SITEMAP_URL", "/sitemap.xml")

# Включить поддержку изображений в sitemap
SITEMAP_INCLUDE_IMAGES = getenv("SITEMAP_INCLUDE_IMAGES", "True") == "True"

# Включить поддержку видео в sitemap
SITEMAP_INCLUDE_VIDEOS = getenv("SITEMAP_INCLUDE_VIDEOS", "False") == "True"

# Включить поддержку новостей в sitemap (Google News Sitemap)
SITEMAP_INCLUDE_NEWS = getenv("SITEMAP_INCLUDE_NEWS", "False") == "True"

# ------------------ НАСТРОЙКИ ПАГИНАЦИИ -------------------

# Максимальное количество URL в одном sitemap-файле
SITEMAP_LIMIT = int(getenv("SITEMAP_LIMIT", 50000))

# ------------------ ИНТЕГРАЦИЯ С DJANGO -------------------

# Настройки для django.contrib.sitemaps
INSTALLED_APPS_SITEMAP = ["django.contrib.sitemaps"]
