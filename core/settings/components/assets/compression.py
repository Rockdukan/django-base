"""
Настройки сжатия статических файлов для Django

Компонент отвечает за:
1. Минификацию CSS и JavaScript файлов
2. Оптимизацию изображений
3. Настройки HTTP-сжатия
"""

from core.settings import STATIC_URL

# ------------------ ОБЩИЕ НАСТРОЙКИ СЖАТИЯ -------------------

# Включить сжатие статических файлов
COMPRESS_ENABLED = True

# URL для сжатых файлов
COMPRESS_URL = STATIC_URL

# Суффикс для сжатых файлов
COMPRESS_OUTPUT_DIR = "compressed"

# ------------------ НАСТРОЙКИ CSS -------------------

# Включить сжатие CSS
COMPRESS_CSS_ENABLED = True

# Фильтры для обработки CSS
COMPRESS_CSS_FILTERS = [
    "compressor.filters.css_default.CssAbsoluteFilter",
    "compressor.filters.cssmin.rCSSMinFilter",
]

# ------------------ НАСТРОЙКИ JAVASCRIPT -------------------

# Включить сжатие JavaScript
COMPRESS_JS_ENABLED = True

# Фильтры для обработки JavaScript
COMPRESS_JS_FILTERS = [
    "compressor.filters.jsmin.JSMinFilter",
]

# ------------------ НАСТРОЙКИ КЭШИРОВАНИЯ -------------------

# Время жизни кэша (в секундах)
COMPRESS_CACHE_TIMEOUT = 60 * 60 * 24 * 30  # 30 дней

# ------------------ НАСТРОЙКИ ОПТИМИЗАЦИИ ИЗОБРАЖЕНИЙ -------------------

# Включить автоматическую оптимизацию изображений
IMAGE_COMPRESSION_ENABLED = False

# Качество JPEG при оптимизации (1-100)
IMAGE_JPEG_QUALITY = 85

# Уровень оптимизации PNG (0-9)
IMAGE_PNG_OPTIMIZATION = 9

# Использовать webp для изображений, если браузер поддерживает
IMAGE_WEBP_ENABLED = False

# ------------------ НАСТРОЙКИ HTTP-СЖАТИЯ (GZIP, BROTLI) -------------------

# Минимальный размер ответа для сжатия (в байтах)
GZIP_MIN_LENGTH = 200

# Уровень сжатия Brotli (от 0 до 11, где 11 - максимальное сжатие)
BROTLI_LEVEL = 6

# Уровень сжатия Deflate (от 1 до 9, где 9 - максимальное сжатие)
DEFLATE_LEVEL = 6
