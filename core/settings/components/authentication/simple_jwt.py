from datetime import timedelta

"""
Настройки Simple JWT для аутентификации на основе JWT

Компонент отвечает за:
1. Настройку JWT токенов для аутентификации
2. Конфигурацию времени жизни и алгоритмов шифрования
3. Настройки обработчиков для JWT
4. Параметры верификации и обновления токенов
"""

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ SIMPLE JWT -------------------

SIMPLE_JWT = {
    # ------------------ НАСТРОЙКИ ВРЕМЕНИ ЖИЗНИ ТОКЕНОВ -------------------
    # Время жизни токена доступа
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    # Время жизни токена обновления
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    # Ротация токенов обновления
    "ROTATE_REFRESH_TOKENS": False,
    # Добавление токенов в черный список после ротации
    "BLACKLIST_AFTER_ROTATION": True,
    # ------------------ НАСТРОЙКИ АЛГОРИТМОВ -------------------
    # Алгоритм шифрования для подписи токена
    "ALGORITHM": "HS256",
    # Ключ для подписи токена
    "SIGNING_KEY": None,
    # Ключ для проверки токена (для асимметричных алгоритмов)
    "VERIFYING_KEY": None,
    # ------------------ НАСТРОЙКИ ЗАГОЛОВКОВ ТОКЕНА -------------------
    # Целевая аудитория токена
    "AUDIENCE": None,
    # Идентификатор издателя токена
    "ISSUER": None,
    # Типы заголовка авторизации
    "AUTH_HEADER_TYPES": ("JWT",),
    # Имя заголовка авторизации
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    # ------------------ НАСТРОЙКИ ПОЛЬЗОВАТЕЛЬСКИХ ПОЛЕЙ -------------------
    # Поле идентификатора пользователя в модели
    "USER_ID_FIELD": "id",
    # Поле идентификатора пользователя в токене
    "USER_ID_CLAIM": "user_id",
    # ------------------ НАСТРОЙКИ КЛАССОВ ТОКЕНОВ -------------------
    # Классы токенов аутентификации
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    # Название типа токена в полезной нагрузке
    "TOKEN_TYPE_CLAIM": "token_type",
    # Идентификатор JWT в полезной нагрузке
    "JTI_CLAIM": "jti",
    # ------------------ НАСТРОЙКИ СКОЛЬЗЯЩИХ ТОКЕНОВ -------------------
    # Поле времени истечения срока действия скользящего токена
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    # Время жизни скользящего токена
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    # Время жизни скользящего токена обновления
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    # ------------------ НАСТРОЙКИ ОБРАБОТЧИКОВ ТОКЕНОВ -------------------
    # Списки разрешенных символов для различных типов токенов
    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

# ------------------ ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ SIMPLE JWT -------------------

# Включить черный список токенов
SIMPLE_JWT_USE_BLACKLIST = True

# Модель для черного списка токенов
SIMPLE_JWT_BLACKLIST_MODEL = "token_blacklist.OutstandingToken"

# ------------------ НАСТРОЙКИ ОБРАБОТКИ ЗАПРОСОВ -------------------

# Пользовательская функция для получения объекта пользователя из токена
SIMPLE_JWT_USER_GETTER = "rest_framework_simplejwt.authentication.default_user_authentication_rule"

# Пользовательская функция для проверки токена
SIMPLE_JWT_TOKEN_VERIFIER = "rest_framework_simplejwt.token_blacklist.check_if_token_in_blacklist"

# Аутентификация на основе объекта, а не ID
SIMPLE_JWT_AUTHENTICATE_BY_OBJECT = False

# ------------------ НАСТРОЙКИ COOKIE -------------------

# Использовать JWT в cookie вместо заголовка
SIMPLE_JWT_USE_COOKIE = False

# Имя cookie для токена доступа
SIMPLE_JWT_ACCESS_TOKEN_COOKIE_NAME = "access_token"

# Имя cookie для токена обновления
SIMPLE_JWT_REFRESH_TOKEN_COOKIE_NAME = "refresh_token"

# Безопасные cookie (только HTTPS)
SIMPLE_JWT_COOKIE_SECURE = True

# Доступ к cookie только через HTTP
SIMPLE_JWT_COOKIE_HTTPONLY = True

# Политика cookie SameSite
SIMPLE_JWT_COOKIE_SAMESITE = "Lax"

# ------------------ НАСТРОЙКИ БЕЗОПАСНОСТИ -------------------

# Проверять токен на основе Leeway (допустимое отклонение времени в секундах)
SIMPLE_JWT_LEEWAY = 0

# Проверять токен на основе времени создания
SIMPLE_JWT_CHECK_IAT = True

# Использовать CSRFTOKEN с JWT
SIMPLE_JWT_USE_CSRF = False

# ------------------ НАСТРОЙКИ ОБНОВЛЕНИЯ ТОКЕНОВ -------------------

# Обновление токена с помощью токена обновления без повторной аутентификации
SIMPLE_JWT_REFRESH_WITHOUT_REAUTHENTICATION = True

# Максимальное количество обновлений токена до повторной аутентификации
SIMPLE_JWT_MAX_REFRESH_TIMES = 5

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование событий Simple JWT
SIMPLE_JWT_ENABLE_LOGGING = True

# Уровень логирования
SIMPLE_JWT_LOGGING_LEVEL = "INFO"

# Формат сообщений журнала
SIMPLE_JWT_LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
