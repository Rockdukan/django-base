"""
Настройки Django OAuth Toolkit для поддержки протокола OAuth2

Компонент отвечает за:
1. Настройку сервера авторизации OAuth2
2. Конфигурацию типов токенов и их времени жизни
3. Настройки клиентов OAuth2
4. Параметры безопасности и скоупов
"""

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ OAUTH2 TOOLKIT -------------------

# Включить OAuth2 Toolkit
OAUTH2_PROVIDER_ENABLED = True

# ------------------ НАСТРОЙКИ ТОКЕНОВ -------------------

# Время жизни токена доступа (в секундах)
OAUTH2_PROVIDER = {
    # Время жизни токена доступа (в секундах)
    "ACCESS_TOKEN_EXPIRE_SECONDS": 60 * 60,  # 1 час
    # Время жизни токена обновления (в секундах)
    "REFRESH_TOKEN_EXPIRE_SECONDS": 60 * 60 * 24 * 30,  # 30 дней
    # Обязательный параметр state в запросах авторизации
    "REQUIRE_STATE": True,
    # Размер кода авторизации (в байтах)
    "AUTHORIZATION_CODE_BYTES": 32,
    # Размер токена доступа (в байтах)
    "ACCESS_TOKEN_BYTES": 32,
    # Размер токена обновления (в байтах)
    "REFRESH_TOKEN_BYTES": 32,
    # Обязательное перенаправление URI в запросах авторизации
    "REQUIRE_REDIRECT_URI": True,
    # Использовать токены JWT
    "USE_JWT": False,
    # Время жизни кода авторизации (в секундах)
    "AUTHORIZATION_CODE_EXPIRE_SECONDS": 60,  # 1 минута
    # Генератор токенов
    "TOKEN_GENERATOR_CLASS": "oauth2_provider.generators.BaseGenerator",
    # ------------------ НАСТРОЙКИ ПРИЛОЖЕНИЙ (КЛИЕНТОВ) -------------------
    # Модель для хранения приложений OAuth2
    "APPLICATION_MODEL": "oauth2_provider.Application",
    # Модель для хранения токенов доступа
    "ACCESS_TOKEN_MODEL": "oauth2_provider.AccessToken",
    # Модель для хранения токенов обновления
    "REFRESH_TOKEN_MODEL": "oauth2_provider.RefreshToken",
    # Модель для хранения кодов авторизации
    "AUTHORIZATION_CODE_MODEL": "oauth2_provider.AuthorizationCode",
    # ------------------ НАСТРОЙКИ СКОУПОВ -------------------
    # Модель для хранения допустимых скоупов
    "SCOPES_BACKEND_CLASS": "oauth2_provider.scopes.SettingsScopes",
    # Список доступных скоупов
    "SCOPES": {
        "read": "Read scope",
        "write": "Write scope",
        "introspection": "Introspect token scope",
    },
    # Скоупы по умолчанию
    "DEFAULT_SCOPES": ["read"],
    # ------------------ НАСТРОЙКИ ПОСРЕДНИКОВ (MIDDLEWARE) -------------------
    # Класс для проверки токенов OAuth2
    "OAUTH2_VALIDATOR_CLASS": "oauth2_provider.oauth2_validators.OAuth2Validator",
    # Класс для провайдера сервера OAuth2
    "OAUTH2_SERVER_CLASS": "oauthlib.oauth2.Server",
    # Класс для бэкенда проверки токенов
    "OAUTH2_BACKEND_CLASS": "oauth2_provider.oauth2_backends.OAuthLibCore",
    # ------------------ НАСТРОЙКИ БЕЗОПАСНОСТИ -------------------
    # Ротация токенов обновления
    "ROTATE_REFRESH_TOKEN": True,
    # Повторное использование токенов обновления
    "REUSE_REFRESH_TOKEN": False,
    # Режим отладки для исключений OAuth2
    "ERROR_RESPONSE_WITH_SCOPES": True,
    # Проверять IP-адрес при использовании токенов
    "VERIFY_CLIENT_IP": True,
    # Разделитель скоупов в запросах
    "SCOPES_SEPARATOR": " ",
    # ------------------ НАСТРОЙКИ ИНТЕРФЕЙСА -------------------
    # URL для страницы авторизации
    "AUTHORIZATION_URL": "oauth2_provider:authorize",
    # URL для страницы токенов
    "TOKEN_URL": "oauth2_provider:token",
    # URL для страницы отзыва токенов
    "REVOCATION_URL": "oauth2_provider:revoke-token",
    # URL для страницы информации о токене
    "INTROSPECTION_URL": "oauth2_provider:introspect",
    # URL-пространство имен для OAuth2 Toolkit
    "BASE_URL": "oauth2/",
    # ------------------ НАСТРОЙКИ ШАБЛОНОВ -------------------
    # Список шаблонов для страницы авторизации
    "AUTHORIZATION_TEMPLATES": {
        "authorization": "oauth2_provider/authorize.html",
        "error": "oauth2_provider/error.html",
    },
    # ------------------ НАСТРОЙКИ ПАРСЕРОВ -------------------
    # Классы парсеров для запросов OAuth2
    "PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
    # ------------------ НАСТРОЙКИ РЕНДЕРЕРОВ -------------------
    # Классы рендереров для ответов OAuth2
    "RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}

# ------------------ ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ OAUTH2 TOOLKIT -------------------

# Управление пространством имен URL
OAUTH2_PROVIDER_URL_NAMESPACE = "oauth2_provider"

# Использовать PKCE (Proof Key for Code Exchange) для публичных клиентов
OAUTH2_PROVIDER_PKCE_REQUIRED = True

# ------------------ НАСТРОЙКИ JWT -------------------

# Настройки для токенов JWT (если используются)
OAUTH2_PROVIDER_JWT = {
    # Ключ для подписи JWT токенов
    "JWT_PRIVATE_KEY": None,
    # Открытый ключ для проверки JWT токенов
    "JWT_PUBLIC_KEY": None,
    # Алгоритм для подписи JWT токенов
    "JWT_ALGORITHM": "RS256",
    # Информация о клиенте в JWT
    "JWT_INCLUDE_CLIENT_ID": True,
    # Дополнительные поля в JWT
    "JWT_EXTRA_CLAIMS": {},
    # Путь к закрытому ключу
    "JWT_PRIVATE_KEY_FILEPATH": None,
    # Путь к открытому ключу
    "JWT_PUBLIC_KEY_FILEPATH": None,
}

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование событий OAuth2
OAUTH2_PROVIDER_ENABLE_LOGGING = True

# Уровень логирования
OAUTH2_PROVIDER_LOGGING_LEVEL = "INFO"

# Формат сообщений журнала
OAUTH2_PROVIDER_LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
