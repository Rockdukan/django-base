"""
Настройки django-filer для управления медиа-файлами.

При использовании filer раскомментируйте компонент в settings и задайте
пути относительно корня проекта или через переменные окружения.
"""

from pathlib import Path

# Корень проекта (при подключении компонента base уже загружен, используем путь)
_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent
_FILER_MEDIA = _PROJECT_ROOT / "media" / "filer"
_FILER_THUMBS = _PROJECT_ROOT / "media" / "filer_thumbnails"

FILER_CANONICAL_URL = "sharing/"

FILER_STORAGES = {
    "public": {
        "main": {
            "ENGINE": "filer.storage.PublicFileSystemStorage",
            "OPTIONS": {
                "location": str(_FILER_MEDIA),
                "base_url": "/media/filer/",
            },
            "UPLOAD_TO": "filer.utils.generate_filename.randomized",
            "UPLOAD_TO_PREFIX": "filer_public",
        },
        "thumbnails": {
            "ENGINE": "filer.storage.PublicFileSystemStorage",
            "OPTIONS": {
                "location": str(_FILER_THUMBS),
                "base_url": "/media/filer_thumbnails/",
            },
        },
    },
    "private": {
        "main": {
            "ENGINE": "filer.storage.PrivateFileSystemStorage",
            "OPTIONS": {
                "location": str(_PROJECT_ROOT / "smedia" / "filer"),
                "base_url": "/smedia/filer/",
            },
            "UPLOAD_TO": "filer.utils.generate_filename.randomized",
            "UPLOAD_TO_PREFIX": "filer_public",
        },
        "thumbnails": {
            "ENGINE": "filer.storage.PrivateFileSystemStorage",
            "OPTIONS": {
                "location": str(_PROJECT_ROOT / "smedia" / "filer_thumbnails"),
                "base_url": "/smedia/filer_thumbnails/",
            },
        },
    },
}

# ------------------ НАСТРОЙКИ МИНИАТЮР -------------------

# Включить поддержку высокого разрешения для миниатюр
THUMBNAIL_HIGH_RESOLUTION = True

# Процессоры для обработки миниатюр
THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

# ------------------ ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ FILER -------------------

# Включить стирание EXIF данных при загрузке изображений
FILER_STRIP_EXIF_DATA = False

# Включить автоматическое определение основного цвета изображения
FILER_ENABLE_PERMISSIONS = True

# Использовать собственный движок для обработки миниатюр
FILER_CUSTOM_THUMBNAIL_ENGINE = None

# Разрешить загрузку SVG файлов
FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS = True

# ------------------ НАСТРОЙКИ ПРЕДСТАВЛЕНИЯ В АДМИНКЕ -------------------

# Включить представление в виде сетки в админке
FILER_ENABLE_ADMIN_GRID_VIEW = True

# Стиль админки по умолчанию (grid или list)
FILER_ADMIN_DEFAULT_VIEW = "list"

# Размер пагинации в админке
FILER_PAGINATE_BY = 20

# Включить поиск в админке
FILER_ENABLE_ADMIN_SEARCH = True

# ------------------ НАСТРОЙКИ ЗАГРУЗКИ -------------------

# Максимальный размер загружаемого файла (в байтах)
FILER_MAX_UPLOAD_SIZE = 100 * 1024 * 1024  # 100 MB

# Валидаторы для проверки загружаемых файлов
FILER_FILE_VALIDATORS = []

# Включить поддержку разрешений django-guardian
FILER_GUARDIAN_SUPPORT = False

# ------------------ НАСТРОЙКИ БЕЗОПАСНОСТИ -------------------

# Включить проверку типа файла по содержимому (magic)
FILER_CHECK_CONTENT_TYPE = True

# Включить сканирование на вирусы
FILER_VIRUS_SCAN_ENABLED = False

# Включить водяные знаки
FILER_WATERMARK_ENABLED = False

# ------------------ НАСТРОЙКИ КЭШИРОВАНИЯ -------------------

# Включить кэширование
FILER_CACHE_ENABLED = True

# Время жизни кэша (в секундах)
FILER_CACHE_TIMEOUT = 60 * 60 * 24  # 24 часа

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование операций
FILER_ENABLE_LOGGING = True

# Уровень логирования
FILER_LOGGING_LEVEL = "INFO"
