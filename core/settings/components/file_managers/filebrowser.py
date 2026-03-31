"""
Настройки django-filebrowser для управления файлами

Компонент отвечает за:
1. Настройку менеджера файлов для админ-панели
2. Конфигурацию каталогов для хранения файлов
3. Настройки обработки изображений и миниатюр
4. Параметры фильтрации и отображения файлов
"""

from django.conf import settings
from django.utils.translation import gettext_lazy as _

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ FILEBROWSER -------------------

# Корневая директория для файлового браузера
FILEBROWSER_DIRECTORY = ""
DIRECTORY = ""

# ------------------ НАСТРОЙКИ ТИПОВ ФАЙЛОВ -------------------

# Допустимые расширения файлов по категориям
EXTENSIONS = getattr(
    settings,
    "FILEBROWSER_EXTENSIONS",
    {
        "Image": [".jpg", ".jpeg", ".gif", ".png", ".tif", ".tiff"],
        "Document": [".pdf", ".doc", ".rtf", ".txt", ".xls", ".csv", ".docx"],
        "Video": [".mov", ".mp4", ".m4v", ".webm", ".wmv", ".mpeg", ".mpg", ".avi", ".rm"],
        "Audio": [".mp3", ".wav", ".aiff", ".midi", ".m4p"],
    },
)

# Форматы, доступные для выбора в различных контекстах
SELECT_FORMATS = getattr(
    settings,
    "FILEBROWSER_SELECT_FORMATS",
    {
        "file": ["Image", "Document", "Video", "Audio"],
        "image": ["Image"],
        "document": ["Document"],
        "media": ["Video", "Audio"],
    },
)

# ------------------ НАСТРОЙКИ МИНИАТЮР И ВЕРСИЙ -------------------

# Базовый каталог для хранения версий
VERSIONS_BASEDIR = getattr(settings, "FILEBROWSER_VERSIONS_BASEDIR", "_versions")

# Конфигурация версий изображений
VERSIONS = getattr(
    settings,
    "FILEBROWSER_VERSIONS",
    {
        "admin_thumbnail": {"verbose_name": "Admin Thumbnail", "width": 60, "height": 60, "opts": "crop"},
        "thumbnail": {"verbose_name": "Thumbnail (1 col)", "width": 60, "height": 60, "opts": "crop"},
        "small": {"verbose_name": "Small (2 col)", "width": 140, "height": "", "opts": ""},
        "medium": {"verbose_name": "Medium (4col )", "width": 300, "height": "", "opts": ""},
        "big": {"verbose_name": "Big (6 col)", "width": 460, "height": "", "opts": ""},
        "large": {"verbose_name": "Large (8 col)", "width": 680, "height": "", "opts": ""},
    },
)

# Качество версий изображений (1-100)
VERSION_QUALITY = getattr(settings, "FILEBROWSER_VERSION_QUALITY", 90)

# Версии, отображаемые в админ-панели
ADMIN_VERSIONS = getattr(settings, "FILEBROWSER_ADMIN_VERSIONS", ["thumbnail", "small", "medium", "big", "large"])

# Миниатюра, используемая в админ-панели
ADMIN_THUMBNAIL = getattr(settings, "FILEBROWSER_ADMIN_THUMBNAIL", "admin_thumbnail")

# Процессоры для обработки версий
VERSION_PROCESSORS = getattr(
    settings,
    "FILEBROWSER_VERSION_PROCESSORS",
    [
        "filebrowser.utils.scale_and_crop",
    ],
)

# Класс для именования версий
VERSION_NAMER = getattr(settings, "FILEBROWSER_VERSION_NAMER", "filebrowser.namers.VersionNamer")

# ------------------ НАСТРОЙКИ ЗАПОЛНИТЕЛЕЙ -------------------

# Изображение-заполнитель, если отсутствует оригинал
PLACEHOLDER = getattr(settings, "FILEBROWSER_PLACEHOLDER", "")

# Показывать заполнитель
SHOW_PLACEHOLDER = getattr(settings, "FILEBROWSER_SHOW_PLACEHOLDER", False)

# Принудительно использовать заполнитель
FORCE_PLACEHOLDER = getattr(settings, "FILEBROWSER_FORCE_PLACEHOLDER", False)

# ------------------ НАСТРОЙКИ ОБРАБОТКИ ИЗОБРАЖЕНИЙ -------------------

# Требовать строгую совместимость с PIL
STRICT_PIL = getattr(settings, "FILEBROWSER_STRICT_PIL", False)

# Максимальный размер блока данных при обработке изображений
IMAGE_MAXBLOCK = getattr(settings, "FILEBROWSER_IMAGE_MAXBLOCK", 1024 * 1024)

# ------------------ НАСТРОЙКИ ФИЛЬТРАЦИИ ФАЙЛОВ -------------------

# Список всех допустимых расширений файлов
EXTENSION_LIST = []
for exts in EXTENSIONS.values():
    EXTENSION_LIST += exts

# Регулярное выражение для исключения файлов
EXCLUDE = getattr(
    settings, "FILEBROWSER_EXCLUDE", (r"_({exts})_.*_q\d{{1,3}}\.({exts})".format(exts="|".join(EXTENSION_LIST)),)
)

# ------------------ НАСТРОЙКИ ЗАГРУЗКИ ФАЙЛОВ -------------------

# Максимальный размер загружаемого файла (в байтах)
MAX_UPLOAD_SIZE = getattr(settings, "FILEBROWSER_MAX_UPLOAD_SIZE", 10485760)

# Нормализовать имена файлов
NORMALIZE_FILENAME = getattr(settings, "FILEBROWSER_NORMALIZE_FILENAME", False)

# Конвертировать имена файлов
CONVERT_FILENAME = getattr(settings, "FILEBROWSER_CONVERT_FILENAME", True)

# ------------------ НАСТРОЙКИ ОТОБРАЖЕНИЯ -------------------

# Количество элементов на странице
LIST_PER_PAGE = getattr(settings, "FILEBROWSER_LIST_PER_PAGE", 50)

# Поле для сортировки по умолчанию
DEFAULT_SORTING_BY = getattr(settings, "FILEBROWSER_DEFAULT_SORTING_BY", "date")

# Порядок сортировки по умолчанию
DEFAULT_SORTING_ORDER = getattr(settings, "FILEBROWSER_DEFAULT_SORTING_ORDER", "desc")

# Регулярное выражение для проверки имен папок
FOLDER_REGEX = getattr(settings, "FILEBROWSER_FOLDER_REGEX", r"^[\w._\ /-]+$")

# Разрешить поиск по вложенным папкам
SEARCH_TRAVERSE = getattr(settings, "FILEBROWSER_SEARCH_TRAVERSE", False)

# ------------------ НАСТРОЙКИ ПРАВ ДОСТУПА -------------------

# Права доступа к файлам по умолчанию
DEFAULT_PERMISSIONS = getattr(settings, "FILEBROWSER_DEFAULT_PERMISSIONS", 0o755)

# Перезаписывать существующие файлы
OVERWRITE_EXISTING = getattr(settings, "FILEBROWSER_OVERWRITE_EXISTING", True)

# Временная директория для загрузок
UPLOAD_TEMPDIR = getattr(settings, "FILEBROWSER_UPLOAD_TEMPDIR", "_temp")

# ------------------ ПЕРЕВОДЫ ИНТЕРФЕЙСА -------------------

# Перевод строковых констант для интерфейса
_("Folder")
_("Image")
_("Video")
_("Document")
_("Audio")
