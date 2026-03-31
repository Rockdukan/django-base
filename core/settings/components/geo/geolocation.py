"""
Настройки геолокации для определения местоположения пользователей

Компонент отвечает за:
1. Настройку сервисов геолокации
2. Конфигурацию провайдеров данных
3. Настройки кэширования результатов
4. Параметры точности и фильтрации
"""


# ------------------ ОСНОВНЫЕ НАСТРОЙКИ ГЕОЛОКАЦИИ -------------------

# Включить геолокацию
GEOLOCATION_ENABLED = True

# ------------------ НАСТРОЙКИ ПРОВАЙДЕРОВ -------------------

# Провайдер геолокации по умолчанию
# Поддерживаемые значения:
# "ipstack" - https://ipstack.com/
# "maxmind" - https://www.maxmind.com/
# "geoip2" - https://dev.maxmind.com/geoip/geoip2/
# "ipwhois" - https://ipwhois.io/
# "ipapi" - https://ipapi.co/
# "ipgeolocation" - https://ipgeolocation.io/
# "google" - https://developers.google.com/maps/documentation/geolocation
# "browser" - использование Geolocation API браузера
GEOLOCATION_PROVIDER = "maxmind"

# ------------------ НАСТРОЙКИ КЛЮЧЕЙ API -------------------

# API ключи для различных провайдеров
GEOLOCATION_API_KEYS = {
    "ipstack": "",
    "maxmind": "",
    "ipwhois": "",
    "ipapi": "",
    "ipgeolocation": "",
    "google": "",
}

# ------------------ НАСТРОЙКИ ОПРЕДЕЛЕНИЯ МЕСТОПОЛОЖЕНИЯ -------------------

# Использовать определение местоположения по IP
GEOLOCATION_USE_IP = True

# Использовать определение местоположения через браузер (HTML5 Geolocation API)
GEOLOCATION_USE_BROWSER = False

# Использовать определение местоположения по GPS (для мобильных устройств)
GEOLOCATION_USE_GPS = False

# Запрашивать разрешение на определение местоположения
GEOLOCATION_ASK_PERMISSION = True

# ------------------ НАСТРОЙКИ КЭШИРОВАНИЯ -------------------

# Включить кэширование результатов геолокации
GEOLOCATION_CACHE_ENABLED = True

# Время жизни кэша (в секундах)
GEOLOCATION_CACHE_TIMEOUT = 60 * 60 * 24 * 7  # 7 дней

# Ключ кэша
GEOLOCATION_CACHE_KEY_PREFIX = "geolocation"

# ------------------ НАСТРОЙКИ ТОЧНОСТИ -------------------

# Минимальная точность для результатов геолокации (в метрах)
GEOLOCATION_MIN_ACCURACY = 100

# Таймаут для запросов геолокации (в секундах)
GEOLOCATION_TIMEOUT = 5

# Максимальное возраст данных о местоположении (в секундах)
GEOLOCATION_MAX_AGE = 60 * 60  # 1 час

# ------------------ НАСТРОЙКИ БЕЗОПАСНОСТИ -------------------

# Разрешить определение местоположения в небезопасном контексте (не HTTPS)
GEOLOCATION_ALLOW_INSECURE = False

# Скрывать точные координаты для приватности (округлять)
GEOLOCATION_PRIVACY_ROUNDING = True

# Точность округления для приватности (количество десятичных знаков)
GEOLOCATION_PRIVACY_PRECISION = 2

# ------------------ НАСТРОЙКИ ФОЛЛБЕКА -------------------

# Координаты по умолчанию, если не удалось определить местоположение
GEOLOCATION_DEFAULT_POSITION = {
    "latitude": 55.755826,  # Москва
    "longitude": 37.6173,
}

# ------------------ НАСТРОЙКИ ИНТЕГРАЦИИ -------------------

# Включать информацию о местоположении в контекст запроса
GEOLOCATION_INCLUDE_IN_REQUEST = True

# Добавлять данные о геолокации в контекст шаблонов
GEOLOCATION_TEMPLATE_CONTEXT = True

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование операций геолокации
GEOLOCATION_ENABLE_LOGGING = True

# Уровень логирования
GEOLOCATION_LOGGING_LEVEL = "INFO"
