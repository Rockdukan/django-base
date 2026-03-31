"""
Настройки Content Delivery Network (CDN) для Django

Компонент отвечает за:
1. Настройку CDN для статических файлов
2. Конфигурацию URL для статических и медиа-ресурсов
3. Настройки кэширования CDN
"""

import os

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ CDN -------------------

# Включить CDN для статических файлов
USE_CDN = False

# Базовый URL CDN для статических файлов
CDN_STATIC_URL = ""

# Базовый URL CDN для медиа-файлов
CDN_MEDIA_URL = ""

# Если CDN включен, переопределяем URL для статических и медиа-файлов
if USE_CDN:
    if CDN_STATIC_URL:
        STATIC_URL = CDN_STATIC_URL

    if CDN_MEDIA_URL:
        MEDIA_URL = CDN_MEDIA_URL

# ------------------ НАСТРОЙКИ КЭШИРОВАНИЯ CDN -------------------

# TTL (время жизни) для статических файлов в CDN (в секундах)
CDN_STATIC_TTL = 60 * 60 * 24 * 30  # 30 дней

# TTL для медиа-файлов в CDN (в секундах)
CDN_MEDIA_TTL = 60 * 60 * 24 * 7  # 7 дней

# Заголовок Cache-Control для статических файлов
CDN_STATIC_CACHE_CONTROL = f"public, max-age={CDN_STATIC_TTL}"

# Заголовок Cache-Control для медиа-файлов
CDN_MEDIA_CACHE_CONTROL = f"public, max-age={CDN_MEDIA_TTL}"

# ------------------ НАСТРОЙКИ БЕЗОПАСНОСТИ CDN -------------------

# Включить подписи URL для защиты контента
CDN_URL_SIGNING = False

# Секретный ключ для подписи URL (критическая информация)
CDN_URL_SIGNING_KEY = os.environ.get("CDN_URL_SIGNING_KEY", "")

# Срок действия подписанных URL (в секундах)
CDN_URL_SIGNING_EXPIRY = 60 * 60  # 1 час
