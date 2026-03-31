"""
Настройки starcross_gallery для фотогалерей

Компонент отвечает за:
1. Настройку фотогалерей и альбомов
2. Конфигурацию отображения галерей
3. Настройки обработки изображений и миниатюр
4. Параметры интерфейса и персонализации
"""


# ------------------ ОСНОВНЫЕ НАСТРОЙКИ STARCROSS_GALLERY -------------------

# Путь к логотипу галереи
GALLERY_LOGO_PATH = "gallery/images/starcross.png"

# Заголовок галереи
GALLERY_TITLE = "Gallery"

# Информация в футере галереи
GALLERY_FOOTER_INFO = "Starcross Gallery"

# Email в футере галереи
GALLERY_FOOTER_EMAIL = "gallery@starcross.dev"

# ------------------ НАСТРОЙКИ ВНЕШНЕГО ВИДА -------------------

# Основной цвет темы
GALLERY_THEME_COLOR = "black"

# ------------------ НАСТРОЙКИ ИЗОБРАЖЕНИЙ -------------------

# Размер миниатюр (в пикселях)
GALLERY_THUMBNAIL_SIZE = 200

# Размер изображения для предпросмотра (в пикселях)
GALLERY_PREVIEW_SIZE = 1000

# Качество изображений при изменении размера (1-100)
GALLERY_RESIZE_QUALITY = 80

# Коэффициент для экранов высокого разрешения (HDPI)
GALLERY_HDPI_FACTOR = 2

# Отступ между изображениями (в пикселях)
GALLERY_IMAGE_MARGIN = 6

# ------------------ ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ STARCROSS_GALLERY -------------------

# Настройки альбомов
GALLERY_ALBUMS = {
    # Включить группировку по альбомам
    "ENABLED": True,
    # Сортировка альбомов (name, date, custom)
    "SORT_BY": "name",
    # Порядок сортировки (asc, desc)
    "SORT_ORDER": "asc",
    # Показывать обложку альбома
    "SHOW_COVER": True,
    # Показывать количество изображений в альбоме
    "SHOW_COUNT": True,
}

# Настройки сеток
GALLERY_GRID = {
    # Тип сетки (flex, masonry, justified)
    "TYPE": "flex",
    # Максимальная ширина сетки (в пикселях)
    "MAX_WIDTH": 1200,
    # Высота строки для justified сетки (в пикселях)
    "ROW_HEIGHT": 320,
    # Отступы в сетке (в пикселях)
    "GUTTER": 10,
}

# Настройки изображений
GALLERY_IMAGES = {
    # Сортировка изображений (name, date, order)
    "SORT_BY": "date",
    # Порядок сортировки (asc, desc)
    "SORT_ORDER": "desc",
    # Показывать оригинальное изображение
    "SHOW_ORIGINAL": True,
    # Показывать EXIF данные
    "SHOW_EXIF": True,
    # Автоматическое воспроизведение слайдшоу
    "SLIDESHOW_AUTOPLAY": False,
    # Интервал слайдшоу (в миллисекундах)
    "SLIDESHOW_INTERVAL": 5000,
}

# Настройки интерфейса
GALLERY_UI = {
    # Показывать навигацию
    "SHOW_NAVIGATION": True,
    # Показывать хлебные крошки
    "SHOW_BREADCRUMBS": True,
    # Показывать счетчик изображений
    "SHOW_COUNTER": True,
    # Показывать кнопки соц. сетей
    "SHOW_SOCIAL_BUTTONS": False,
    # Показывать кнопку загрузки
    "SHOW_DOWNLOAD_BUTTON": True,
    # Показывать кнопку полного экрана
    "SHOW_FULLSCREEN_BUTTON": True,
    # Показывать кнопку слайдшоу
    "SHOW_SLIDESHOW_BUTTON": True,
}

# Настройки анимации
GALLERY_ANIMATION = {
    # Тип анимации (fade, slide, zoom)
    "TYPE": "fade",
    # Длительность анимации (в миллисекундах)
    "DURATION": 300,
    # Тип кривой анимации
    "EASING": "ease-in-out",
}

# Настройки лайтбокса
GALLERY_LIGHTBOX = {
    # Показывать заголовок изображения
    "SHOW_TITLE": True,
    # Показывать описание изображения
    "SHOW_DESCRIPTION": True,
    # Показывать миниатюры в лайтбоксе
    "SHOW_THUMBNAILS": True,
    # Включить зум изображения
    "ENABLE_ZOOM": True,
    # Включить свайп на мобильных
    "ENABLE_SWIPE": True,
}

# ------------------ НАСТРОЙКИ БЕЗОПАСНОСТИ -------------------

# Максимальный размер загружаемого файла (в байтах)
GALLERY_MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10 MB

# Разрешенные типы файлов
GALLERY_ALLOWED_FILE_TYPES = ["image/jpeg", "image/png", "image/gif"]

# ------------------ НАСТРОЙКИ КЭШИРОВАНИЯ -------------------

# Включить кэширование
GALLERY_CACHE_ENABLED = True

# Время жизни кэша (в секундах)
GALLERY_CACHE_TIMEOUT = 60 * 60 * 24  # 24 часа

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование
GALLERY_ENABLE_LOGGING = True

# Уровень логирования
GALLERY_LOGGING_LEVEL = "INFO"
