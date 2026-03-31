"""
Настройки sorl-thumbnail для работы с миниатюрами изображений

Компонент отвечает за:
1. Настройку создания и хранения миниатюр
2. Конфигурацию форматов и качества изображений
3. Настройки кэширования миниатюр
4. Параметры обработки изображений
"""


# ------------------ ОСНОВНЫЕ НАСТРОЙКИ SORL-THUMBNAIL -------------------

# Путь к ImageMagick convert (если используется)
THUMBNAIL_CONVERT = "/path/to/gm convert"

# Путь к ImageMagick identify (если используется)
THUMBNAIL_IDENTIFY = "/path/to/gm identify"

# ------------------ НАСТРОЙКИ ХРАНЕНИЯ МИНИАТЮР -------------------

# Директория для хранения миниатюр
THUMBNAIL_PREFIX = "thumbs/"

# Базовая директория для хранения миниатюр
THUMBNAIL_BASEDIR = ""

# Суффикс для имени миниатюры
THUMBNAIL_SUFFIX = ""

# Класс хранилища для миниатюр
THUMBNAIL_STORAGE = "django.core.files.storage.FileSystemStorage"

# ------------------ НАСТРОЙКИ ФОРМАТА И КАЧЕСТВА -------------------

# Формат миниатюр по умолчанию (JPEG, PNG, WEBP)
THUMBNAIL_FORMAT = "JPEG"

# Качество JPEG-миниатюр (1-100)
THUMBNAIL_QUALITY = 85

# Использовать прогрессивный JPEG
THUMBNAIL_PROGRESSIVE = True

# Ориентация миниатюры
THUMBNAIL_ORIENTATION = True

# Оптимизация PNG
THUMBNAIL_OPTIMIZE = True

# Уровень сжатия PNG (1-9)
THUMBNAIL_PNG_COMPRESSION_LEVEL = 6

# ------------------ НАСТРОЙКИ РАЗМЕРОВ И ПРОПОРЦИЙ -------------------

# Сохранять пропорции изображения по умолчанию
THUMBNAIL_PRESERVE_RATIO = True

# Использовать точные размеры для миниатюр
THUMBNAIL_FORCE_DIMENSIONS = True

# Автоматически поворачивать изображения согласно EXIF
THUMBNAIL_EXIF_ORIENTATION = True

# Использовать высокое разрешение для миниатюр (для retina-дисплеев)
THUMBNAIL_HIGH_RESOLUTION = True

# Суффикс для миниатюр высокого разрешения
THUMBNAIL_HIGH_RESOLUTION_SUFFIX = "@2x"

# ------------------ НАСТРОЙКИ КЭШИРОВАНИЯ -------------------

# Включить кэширование
THUMBNAIL_CACHE = True

# Время жизни кэша (в секундах)
THUMBNAIL_CACHE_TIMEOUT = 60 * 60 * 24 * 30  # 30 дней

# Имя кэш-бэкенда
THUMBNAIL_CACHE_BACKEND = "default"

# Очищать кэш при изменении исходного изображения
THUMBNAIL_CACHE_INVALIDATE_ON_SOURCE_CHANGE = True

# ------------------ НАСТРОЙКИ DEBUG И ЛОГИРОВАНИЯ -------------------

# Режим отладки
THUMBNAIL_DEBUG = False

# Включить логирование
THUMBNAIL_ENABLE_LOGGING = True

# Уровень логирования
THUMBNAIL_LOGGING_LEVEL = "INFO"

# ------------------ НАСТРОЙКИ WATERMARK -------------------

# Использовать водяной знак
THUMBNAIL_WATERMARK = False

# Изображение для водяного знака
THUMBNAIL_WATERMARK_IMAGE = "watermark.png"

# Позиция водяного знака
THUMBNAIL_WATERMARK_POSITION = "center"

# Прозрачность водяного знака (0-1)
THUMBNAIL_WATERMARK_OPACITY = 0.5

# ------------------ НАСТРОЙКИ ОБРАБОТЧИКОВ -------------------

# Процессоры для обработки миниатюр
THUMBNAIL_PROCESSORS = (
    "sorl.thumbnail.processors.colorspace",
    "sorl.thumbnail.processors.autocrop",
    "sorl.thumbnail.processors.scale_and_crop",
    "sorl.thumbnail.processors.filters",
    "sorl.thumbnail.processors.background",
)

# Классы движка для генерации миниатюр
THUMBNAIL_ENGINE = "sorl.thumbnail.engines.pil_engine.Engine"

# Класс-помощник для генерации KV-пар
THUMBNAIL_KVSTORE = "sorl.thumbnail.kvstores.cached_db_kvstore.KVStore"

# ------------------ НАСТРОЙКИ АЛЬТЕРНАТИВНЫХ ИСТОЧНИКОВ -------------------

# Альтернативное изображение при ошибке
THUMBNAIL_ALTERNATIVE_RESOLUTIONS = [1, 2]

# Заполнитель, если изображение недоступно
THUMBNAIL_DUMMY = False

# Цвет заполнителя
THUMBNAIL_DUMMY_COLOR = "#FFFFFF"

# Соотношение заполнителя
THUMBNAIL_DUMMY_RATIO = 1.5
