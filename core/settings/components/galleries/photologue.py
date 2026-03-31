"""
Настройки photologue для фотогалерей

Компонент отвечает за:
1. Настройку фотогалерей и альбомов
2. Конфигурацию хранения и обработки изображений
3. Настройки миниатюр и эффектов
4. Параметры отображения и интеграции
"""

import os

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ PHOTOLOGUE -------------------

# Директория для хранения фотографий
PHOTOLOGUE_DIR = "photologue"

# ------------------ НАСТРОЙКИ ГАЛЕРЕЙ -------------------

# Лимит последних галерей (None - без ограничения)
PHOTOLOGUE_GALLERY_LATEST_LIMIT = None

# Размер выборки для галерей
PHOTOLOGUE_GALLERY_SAMPLE_SIZE = 5

# ------------------ НАСТРОЙКИ ИЗОБРАЖЕНИЙ -------------------

# Максимальная длина поля изображения
PHOTOLOGUE_IMAGE_FIELD_MAX_LENGTH = 100

# Максимальный размер блока для обработки изображений
PHOTOLOGUE_MAXBLOCK = 256 * 2**10  # 256 КБ

# ------------------ НАСТРОЙКИ МУЛЬТИСАЙТОВОСТИ -------------------

# Поддержка мультисайтовости
PHOTOLOGUE_MULTISITE = False

# ------------------ НАСТРОЙКИ ПУТЕЙ -------------------

# Путь для изображений (None - использовать PHOTOLOGUE_DIR)
PHOTOLOGUE_PATH = None

# Путь к изображению-образцу
PHOTOLOGUE_SAMPLE_IMAGE_PATH = os.path.join(os.path.dirname(__file__), "res", "sample.jpg")

# ------------------ ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ PHOTOLOGUE -------------------

# Настройки качества изображений
PHOTOLOGUE_QUALITY = {
    "thumbnail": 70,
    "display": 80,
    "original": 100,
}

# Размеры миниатюр по умолчанию
PHOTOLOGUE_THUMBNAIL_SIZES = {
    "small": (100, 100),
    "medium": (240, 240),
    "large": (600, 600),
}

# Настройки качества JPEG
PHOTOLOGUE_JPEG_QUALITY = 85

# Включить автоматическое создание миниатюр при загрузке
PHOTOLOGUE_CREATE_THUMBNAILS_ON_UPLOAD = True

# Использовать имя файла в качестве заголовка по умолчанию
PHOTOLOGUE_USE_FILENAME_AS_TITLE = True

# ------------------ НАСТРОЙКИ WATERMARK -------------------

# Включить водяные знаки
PHOTOLOGUE_WATERMARK_ENABLED = False

# Путь к изображению водяного знака
PHOTOLOGUE_WATERMARK_IMAGE = None

# Непрозрачность водяного знака (0-1)
PHOTOLOGUE_WATERMARK_OPACITY = 0.5

# Позиция водяного знака (center, top-left, top-right, bottom-left, bottom-right)
PHOTOLOGUE_WATERMARK_POSITION = "bottom-right"

# ------------------ НАСТРОЙКИ ADMIN PANEL -------------------

# Использовать sortedm2m для сортировки в админке
PHOTOLOGUE_ADMIN_USE_SORTEDM2M = True

# Количество изображений на страницу в админке
PHOTOLOGUE_ADMIN_THUMBNAIL_PER_PAGE = 20

# ------------------ НАСТРОЙКИ БЕЗОПАСНОСТИ -------------------

# Разрешенные расширения файлов
PHOTOLOGUE_ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png", "gif"]

# Максимальный размер загружаемого файла (в байтах)
PHOTOLOGUE_MAX_UPLOAD_SIZE = 5 * 1024 * 1024  # 5 MB

# ------------------ НАСТРОЙКИ КЭШИРОВАНИЯ -------------------

# Включить кэширование галерей и фотографий
PHOTOLOGUE_CACHE_ENABLED = True

# Время жизни кэша (в секундах)
PHOTOLOGUE_CACHE_TIMEOUT = 60 * 60 * 24  # 24 часа

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование операций с photologue
PHOTOLOGUE_ENABLE_LOGGING = True

# Уровень логирования
PHOTOLOGUE_LOGGING_LEVEL = "INFO"
