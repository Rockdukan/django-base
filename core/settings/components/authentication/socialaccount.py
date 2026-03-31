"""
Настройки django-allauth для социальной аутентификации

Компонент отвечает за:
1. Настройку провайдеров социальной авторизации
2. Конфигурацию процесса подключения аккаунтов
3. Настройки верификации email
4. Обработку регистрации через социальные сети
"""


# ------------------ ОСНОВНЫЕ НАСТРОЙКИ SOCIALACCOUNT -------------------

# Класс адаптера социальных аккаунтов
SOCIALACCOUNT_ADAPTER = "allauth.socialaccount.adapter.DefaultSocialAccountAdapter"

# ------------------ НАСТРОЙКИ РЕГИСТРАЦИИ -------------------

# Автоматически создавать пользователя при успешной социальной аутентификации
SOCIALACCOUNT_AUTO_SIGNUP = True

# Форма для настройки данных пользователя перед регистрацией (если не автоматическая)
SOCIALACCOUNT_SIGNUP_FORM_CLASS = None

# ------------------ НАСТРОЙКИ EMAIL -------------------

# Тип проверки email при регистрации через социальную сеть
# Опции: "none", "optional", "mandatory"
SOCIALACCOUNT_EMAIL_VERIFICATION = "none"

# Требовать email при регистрации через социальную сеть
SOCIALACCOUNT_EMAIL_REQUIRED = False

# ------------------ НАСТРОЙКИ ПОДКЛЮЧЕНИЯ АККАУНТОВ -------------------

# Форма для установки имени пользователя при подключении социального аккаунта
SOCIALACCOUNT_USERNAME_FORM_CLASS = None

# Пользовательские формы для социальных аккаунтов
SOCIALACCOUNT_FORMS = {}

# ------------------ НАСТРОЙКИ ДАННЫХ ПРОФИЛЯ -------------------

# Запрашивать email у социального провайдера
SOCIALACCOUNT_QUERY_EMAIL = False

# Хранить токены доступа к API социальных сетей
SOCIALACCOUNT_STORE_TOKENS = True

# ------------------ НАСТРОЙКИ АВАТАРОВ -------------------

# Получать аватары из социальных сетей
SOCIALACCOUNT_AVATAR_SUPPORT = True

# ------------------ НАСТРОЙКИ ПРОВАЙДЕРОВ -------------------

# Список провайдеров социальной аутентификации
SOCIALACCOUNT_PROVIDERS = {
    # Настройки для Google
    "google": {
        # OAuth тип авторизации
        "OAUTH_TYPE": 2,
        # Запрашиваемые права доступа
        "SCOPE": [
            "profile",
            "email",
        ],
        # Дополнительные параметры авторизации
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        # Какие поля извлекать из профиля
        "FIELDS": [
            "id",
            "email",
            "name",
            "first_name",
            "last_name",
            "verified",
            "locale",
            "timezone",
            "link",
            "gender",
            "updated_time",
        ],
        # Соответствие полей социальной сети с полями Django User
        "FIELD_MAPPING": {
            "email": "email",
            "first_name": "first_name",
            "last_name": "last_name",
        },
        # URL-адреса для авторизации
        "URLS": {
            "access_token": "https://accounts.google.com/o/oauth2/token",
            "authorize": "https://accounts.google.com/o/oauth2/auth",
            "profile": "https://www.googleapis.com/oauth2/v1/userinfo",
        },
        # Задержка между запросами к API (в секундах)
        "THROTTLE_RATE": "100/hour",
    },
    # Настройки для Facebook
    "facebook": {
        "SCOPE": ["email", "public_profile"],
        "AUTH_PARAMS": {"auth_type": "reauthenticate"},
        "INIT_PARAMS": {"cookie": True},
        "FIELDS": [
            "id",
            "email",
            "name",
            "first_name",
            "last_name",
            "verified",
            "locale",
            "timezone",
            "link",
            "gender",
            "updated_time",
        ],
        "EXCHANGE_TOKEN": True,
        "VERIFIED_EMAIL": False,
        "VERSION": "v13.0",
    },
    # Настройки для Twitter
    "twitter": {
        "SCOPE": ["email"],
        "API_VERSION": "2",
    },
    # Настройки для GitHub
    "github": {
        "SCOPE": ["user", "repo"],
        "AUTH_PARAMS": {"auth_type": "login"},
        "FIELDS": [
            "id",
            "email",
            "name",
            "login",
        ],
    },
    # Настройки для VK
    "vk": {
        "SCOPE": ["email"],
        "API_VERSION": "5.131",
        "FIELDS": [
            "id",
            "email",
            "first_name",
            "last_name",
            "screen_name",
            "photo",
        ],
    },
    # Настройки для Яндекс
    "yandex": {
        "SCOPE": ["login:email", "login:info", "login:avatar"],
    },
}

# ------------------ НАСТРОЙКИ ОТКЛЮЧЕНИЯ АККАУНТОВ -------------------

# Форма для отключения социального аккаунта
SOCIALACCOUNT_DISCONNECT_FORM_CLASS = None

# Автоматически удалять социальные аккаунты при удалении пользователя
SOCIALACCOUNT_AUTO_DELETE = True

# ------------------ НАСТРОЙКИ ПЕРЕНАПРАВЛЕНИЙ -------------------

# URL для перенаправления после успешного входа
SOCIALACCOUNT_LOGIN_REDIRECT_URL = "/"

# URL для перенаправления после выхода
SOCIALACCOUNT_LOGOUT_REDIRECT_URL = "/"

# URL для перенаправления после успешного подключения аккаунта
SOCIALACCOUNT_CONNECTION_REDIRECT_URL = "/"

# ------------------ НАСТРОЙКИ ПОДТВЕРЖДЕНИЯ АККАУНТА -------------------

# Шаблон для подтверждения подключения аккаунта
SOCIALACCOUNT_CONFIRM_TEMPLATE = "socialaccount/confirm.html"

# Шаблон для подтверждения отключения аккаунта
SOCIALACCOUNT_DISCONNECT_CONFIRM_TEMPLATE = "socialaccount/disconnect_confirm.html"

# ------------------ НАСТРОЙКИ ОГРАНИЧЕНИЙ -------------------

# Максимальное количество социальных аккаунтов для одного пользователя
SOCIALACCOUNT_MAX_ACCOUNTS = 10

# Ограничение количества попыток соединения в единицу времени
SOCIALACCOUNT_RATE_LIMITS = {
    # Количество попыток / период времени
    "connection": "3/min",
    "login_failed": "5/min",
}

# ------------------ НАСТРОЙКИ БЕЗОПАСНОСТИ -------------------

# Проверять совпадение email пользователя с email из социальной сети
SOCIALACCOUNT_EMAIL_MATCHING = True

# Запрещать подключение аккаунтов с другими email
SOCIALACCOUNT_PREVENT_CONNECT_DIFFERENT_EMAIL = True

# Требовать подтверждение для подключения социального аккаунта
SOCIALACCOUNT_CONNECT_REQUIRE_CONFIRMATION = True

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование событий социальной аутентификации
SOCIALACCOUNT_ENABLE_LOGGING = True

# Уровень логирования
SOCIALACCOUNT_LOGGING_LEVEL = "INFO"

# Формат сообщений журнала
SOCIALACCOUNT_LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
