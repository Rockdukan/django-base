"""
Настройки Django REST Framework

Компонент отвечает за:
1. Настройку конфигурации API
2. Аутентификацию и разрешения
3. Управление сериализацией и валидацией данных
4. Пагинацию, фильтрацию и сортировку
"""

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ REST FRAMEWORK -------------------

REST_FRAMEWORK = {
    # ------------------ НАСТРОЙКИ АУТЕНТИФИКАЦИИ -------------------
    # Классы аутентификации по умолчанию
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # Аутентификация по токену
        "rest_framework.authentication.TokenAuthentication",
        # Аутентификация по JWT-токену
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        # Аутентификация по сессии
        # "rest_framework.authentication.SessionAuthentication",
        # Базовая HTTP-аутентификация
        # "rest_framework.authentication.BasicAuthentication",
        # Аутентификация OAuth2
        # "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    ),
    # ------------------ НАСТРОЙКИ РАЗРЕШЕНИЙ -------------------
    # Классы разрешений по умолчанию
    "DEFAULT_PERMISSION_CLASSES": [
        # Требуется аутентификация
        # "rest_framework.permissions.IsAuthenticated",
        # Без аутентификации
        "rest_framework.permissions.AllowAny",
    ],
    # ------------------ НАСТРОЙКИ РЕНДЕРИНГА -------------------
    # Классы рендереров по умолчанию
    "DEFAULT_RENDERER_CLASSES": [
        # "rest_framework_orjson.renderers.ORJSONRenderer",
        # JSON-рендерер
        "rest_framework.renderers.JSONRenderer",
        # Рендерер для формы API
        # "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    # ------------------ НАСТРОЙКИ ПАРСЕРОВ -------------------
    # Классы парсеров по умолчанию
    "DEFAULT_PARSER_CLASSES": [
        # JSON-парсер
        "rest_framework.parsers.JSONParser",
        # Парсер данных формы
        "rest_framework.parsers.FormParser",
        # Парсер данных мультиформы
        "rest_framework.parsers.MultiPartParser",
    ],
    # ------------------ НАСТРОЙКИ ФИЛЬТРАЦИИ -------------------
    # Классы фильтров по умолчанию
    "DEFAULT_FILTER_BACKENDS": (
        # Фильтрация с использованием django-filter
        "django_filters.rest_framework.DjangoFilterBackend",
        # Поиск по полям
        # "rest_framework.filters.SearchFilter",
        # Сортировка по полям
        # "rest_framework.filters.OrderingFilter",
    ),
    # ------------------ НАСТРОЙКИ ПАГИНАЦИИ -------------------
    # Класс пагинации по умолчанию
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # Размер страницы по умолчанию
    "PAGE_SIZE": 10,
    # ------------------ НАСТРОЙКИ ОГРАНИЧЕНИЙ -------------------
    # Классы ограничений скорости по умолчанию
    "DEFAULT_THROTTLE_CLASSES": (
        # Ограничение для анонимных пользователей
        "rest_framework.throttling.AnonRateThrottle",
        # Ограничение для аутентифицированных пользователей
        "rest_framework.throttling.UserRateThrottle",
    ),
    # Настройки ограничений скорости
    "DEFAULT_THROTTLE_RATES": {
        # Ограничение для анонимных пользователей (запросов в день)
        "anon": "100/day",
        # Ограничение для аутентифицированных пользователей (запросов в день)
        "user": "1000/day",
    },
    # ------------------ НАСТРОЙКИ ВАЛИДАЦИИ -------------------
    # Режим строгой валидации
    "STRICT_JSON": True,
    # ------------------ НАСТРОЙКИ МЕТАДАННЫХ -------------------
    # Класс метаданных по умолчанию
    "DEFAULT_METADATA_CLASS": "rest_framework.metadata.SimpleMetadata",
    # ------------------ НАСТРОЙКИ ИСКЛЮЧЕНИЙ -------------------
    # Класс обработчика исключений по умолчанию
    "EXCEPTION_HANDLER": "rest_framework.views.exception_handler",
    # ------------------ НАСТРОЙКИ КЭШИРОВАНИЯ -------------------
    # Включить кэширование на основе ETag
    "USE_ETAGS": False,
    # ------------------ НАСТРОЙКИ СХЕМЫ API -------------------
    # Класс генератора схемы по умолчанию
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    # ------------------ НАСТРОЙКИ ФОРМАТИРОВАНИЯ -------------------
    # Формат даты по умолчанию
    "DATE_FORMAT": "%Y-%m-%d",
    # Формат даты и времени по умолчанию
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
    # Формат времени по умолчанию
    "TIME_FORMAT": "%H:%M:%S",
    # ------------------ НАСТРОЙКИ БЕЗОПАСНОСТИ -------------------
    # Типы контента, разрешенные для не-формных запросов
    "NON_FORM_CONTENT_TYPES": ["application/json", "application/x-www-form-urlencoded", "multipart/form-data"],
    # ------------------ НАСТРОЙКИ ВЕРСИОНИРОВАНИЯ -------------------
    # Схема версионирования API
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
    # Параметр версии
    "DEFAULT_VERSION": "v1",
    # Допустимые версии
    "ALLOWED_VERSIONS": ["v1", "v2"],
    # Версия при отсутствии указания версии
    "VERSION_PARAM": "version",
}

# ------------------ DRF SPECTACULAR -------------------

SPECTACULAR_SETTINGS = {
    "TITLE": "API Documentation",
    "DESCRIPTION": "API документация для проекта",
    "VERSION": "v1",
    "SERVE_INCLUDE_SCHEMA": False,
}

# ------------------ ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ REST FRAMEWORK -------------------

# URL для входа/выхода в систему.
# Не используем /api-auth/*, т.к. в проекте нет include("rest_framework.urls").
LOGIN_URL = "/accounts/login/"
LOGOUT_URL = "/accounts/logout/"

# ------------------ НАСТРОЙКИ ДОКУМЕНТАЦИИ -------------------

# Включить документацию API
API_DOCUMENTATION_ENABLED = True

# Заголовок документации API
API_TITLE = "API Documentation"

# Описание документации API
API_DESCRIPTION = "API документация для проекта"

# Версия API
API_VERSION = "1.0.0"

# ------------------ НАСТРОЙКИ ФОРМАТА ДАТЫ И ВРЕМЕНИ -------------------

# Использовать ISO 8601 для форматирования даты и времени
REST_FRAMEWORK_USE_ISO_8601_DATES = True

# ------------------ НАСТРОЙКИ КЭШИРОВАНИЯ -------------------

# Время кэширования схемы API (в секундах)
API_SCHEMA_CACHE_TIMEOUT = 60 * 60  # 1 час

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование API-запросов
API_LOGGING_ENABLED = True

# Уровень логирования API-запросов
API_LOGGING_LEVEL = "INFO"
