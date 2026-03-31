"""
Настройки картографических сервисов

Компонент отвечает за:
1. Настройку провайдеров карт (Google Maps, Yandex Maps, OpenStreetMap и др.)
2. Конфигурацию API ключей и параметров
3. Настройки отображения карт
4. Параметры геокодирования и маршрутизации
"""


# ------------------ ОСНОВНЫЕ НАСТРОЙКИ MAPS -------------------

# Включить поддержку карт
MAPS_ENABLED = True

# Провайдер карт по умолчанию
# Поддерживаемые значения:
# "google" - Google Maps
# "yandex" - Яндекс.Карты
# "osm" - OpenStreetMap
# "mapbox" - Mapbox
# "leaflet" - Leaflet (требует провайдера тайлов)
# "2gis" - 2GIS
MAPS_PROVIDER = "google"

# ------------------ НАСТРОЙКИ API КЛЮЧЕЙ -------------------

# API ключи для различных провайдеров карт
MAPS_API_KEYS = {
    "google": "",
    "yandex": "",
    "mapbox": "",
    "2gis": "",
}

# ------------------ НАСТРОЙКИ ОТОБРАЖЕНИЯ КАРТ -------------------

# Ширина карты по умолчанию (в пикселях или процентах)
MAPS_DEFAULT_WIDTH = "100%"

# Высота карты по умолчанию (в пикселях)
MAPS_DEFAULT_HEIGHT = "400px"

# Начальный уровень масштабирования
MAPS_DEFAULT_ZOOM = 13

# Максимальный уровень масштабирования
MAPS_MAX_ZOOM = 20

# Минимальный уровень масштабирования
MAPS_MIN_ZOOM = 1

# Центр карты по умолчанию (широта, долгота)
MAPS_DEFAULT_CENTER = {
    "latitude": 55.755826,  # Москва
    "longitude": 37.6173,
}

# Тип карты по умолчанию
# Для Google Maps: "roadmap", "satellite", "hybrid", "terrain"
# Для Яндекс.Карт: "map", "satellite", "hybrid"
MAPS_DEFAULT_TYPE = "roadmap"

# ------------------ НАСТРОЙКИ ЭЛЕМЕНТОВ УПРАВЛЕНИЯ -------------------

# Показывать элемент управления масштабированием
MAPS_SHOW_ZOOM_CONTROL = True

# Показывать элемент управления типом карты
MAPS_SHOW_MAP_TYPE_CONTROL = True

# Показывать элемент управления полноэкранным режимом
MAPS_SHOW_FULLSCREEN_CONTROL = True

# Показывать элемент управления местоположением пользователя
MAPS_SHOW_LOCATION_CONTROL = True

# Показывать элемент управления масштабом
MAPS_SHOW_SCALE_CONTROL = True

# Показывать элемент управления поворотом
MAPS_SHOW_ROTATE_CONTROL = True

# Показывать элемент управления обзором
MAPS_SHOW_OVERVIEW_CONTROL = True

# ------------------ НАСТРОЙКИ МАРКЕРОВ -------------------

# Разрешить добавление маркеров на карту
MAPS_ALLOW_MARKERS = True

# Использовать кластеризацию маркеров
MAPS_USE_MARKER_CLUSTERING = True

# Размер кластера маркеров (мин. количество маркеров для группировки)
MAPS_MARKER_CLUSTER_SIZE = 5

# URL для иконки маркера по умолчанию
MAPS_DEFAULT_MARKER_ICON = ""

# Размер маркера по умолчанию (ширина, высота в пикселях)
MAPS_DEFAULT_MARKER_SIZE = (32, 32)

# ------------------ НАСТРОЙКИ ГЕОКОДИРОВАНИЯ -------------------

# Включить геокодирование (преобразование адресов в координаты)
MAPS_ENABLE_GEOCODING = True

# Провайдер для геокодирования
# Поддерживаемые значения: "google", "yandex", "osm", "mapbox", "2gis"
MAPS_GEOCODING_PROVIDER = "google"

# Язык результатов геокодирования
MAPS_GEOCODING_LANGUAGE = "ru"

# Регион для предпочтительных результатов геокодирования
MAPS_GEOCODING_REGION = "RU"

# Ограничить результаты геокодирования определенной страной
MAPS_GEOCODING_COUNTRY_RESTRICTION = "RU"

# ------------------ НАСТРОЙКИ МАРШРУТИЗАЦИИ -------------------

# Включить маршрутизацию (построение маршрутов)
MAPS_ENABLE_ROUTING = True

# Провайдер для маршрутизации
# Поддерживаемые значения: "google", "yandex", "osm", "mapbox", "2gis"
MAPS_ROUTING_PROVIDER = "google"

# Тип маршрутизации по умолчанию
# Для Google Maps: "driving", "walking", "bicycling", "transit"
# Для Яндекс.Карт: "auto", "masstransit", "pedestrian", "bicycle"
MAPS_ROUTING_DEFAULT_MODE = "driving"

# Цвет маршрута по умолчанию
MAPS_ROUTING_DEFAULT_COLOR = "#0088ff"

# Ширина линии маршрута (в пикселях)
MAPS_ROUTING_LINE_WIDTH = 5

# ------------------ НАСТРОЙКИ ЯЗЫКА И ЛОКАЛИЗАЦИИ -------------------

# Язык интерфейса карт
MAPS_LANGUAGE = "ru"

# Регион для отображения карт
MAPS_REGION = "RU"

# ------------------ НАСТРОЙКИ LEAFLET -------------------

# Настройки для Leaflet (если MAPS_PROVIDER = "leaflet")
MAPS_LEAFLET = {
    # URL провайдера тайлов
    "TILES_URL": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    # Атрибуция для тайлов
    "ATTRIBUTION": "© OpenStreetMap contributors",
    # Поддомены для тайлов (если используются)
    "SUBDOMAINS": "abc",
    # Стиль для тайлов mapbox (если используется mapbox)
    "MAPBOX_STYLE": "mapbox/streets-v11",
}

# ------------------ НАСТРОЙКИ ОТРИСОВКИ -------------------

# Включить отрисовку фигур на карте
MAPS_ENABLE_DRAWING = True

# Типы фигур, доступные для рисования
MAPS_DRAWING_TOOLS = ["marker", "polyline", "polygon", "rectangle", "circle"]

# Цвет фигур по умолчанию
MAPS_DRAWING_DEFAULT_COLOR = "#ff0000"

# Прозрачность заливки фигур (0-1)
MAPS_DRAWING_FILL_OPACITY = 0.2

# Ширина линий фигур (в пикселях)
MAPS_DRAWING_LINE_WIDTH = 2

# ------------------ НАСТРОЙКИ ИНТЕГРАЦИИ С ВИДЖЕТАМИ ФОРМ -------------------

# Виджет для выбора координат в формах
MAPS_FORM_WIDGET = "maps.widgets.MapWidget"

# Виджет для выбора области в формах
MAPS_AREA_WIDGET = "maps.widgets.AreaWidget"

# Виджет для выбора маршрута в формах
MAPS_ROUTE_WIDGET = "maps.widgets.RouteWidget"

# ------------------ НАСТРОЙКИ КЭШИРОВАНИЯ -------------------

# Включить кэширование тайлов карт
MAPS_CACHE_TILES = True

# Время жизни кэша тайлов (в секундах)
MAPS_CACHE_TILES_TIMEOUT = 60 * 60 * 24 * 7  # 7 дней

# Включить кэширование результатов геокодирования
MAPS_CACHE_GEOCODING = True

# Время жизни кэша геокодирования (в секундах)
MAPS_CACHE_GEOCODING_TIMEOUT = 60 * 60 * 24  # 24 часа

# ------------------ НАСТРОЙКИ БЕЗОПАСНОСТИ -------------------

# Ограничение домена для API ключей
MAPS_API_KEY_DOMAIN_RESTRICTION = ""

# Ограничение IP для API ключей
MAPS_API_KEY_IP_RESTRICTION = []

# Ограничение запросов к API
MAPS_API_RATE_LIMIT = "1000/day"

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование операций с картами
MAPS_ENABLE_LOGGING = True

# Уровень логирования
MAPS_LOGGING_LEVEL = "INFO"

# Логировать все запросы к API карт
MAPS_LOG_API_REQUESTS = False
