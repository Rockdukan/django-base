"""
Настройки Djoser для REST API аутентификации

Компонент отвечает за:
1. Настройку API для регистрации, авторизации и управления пользователями
2. Конфигурацию токенов аутентификации
3. Настройки подтверждения регистрации и сброса пароля
4. Кастомизацию сериализаторов и представлений
"""


# ------------------ ОСНОВНЫЕ НАСТРОЙКИ DJOSER -------------------

DJOSER = {
    # ------------------ НАСТРОЙКИ ПОДТВЕРЖДЕНИЯ EMAIL -------------------
    # Активация пользователя при регистрации
    "SEND_ACTIVATION_EMAIL": True,
    # Повторная отправка активационного письма
    "SEND_CONFIRMATION_EMAIL": True,
    # URL для активации аккаунта (относительный путь в приложении)
    "ACTIVATION_URL": "activate/{uid}/{token}/",
    # ------------------ НАСТРОЙКИ СБРОСА ПАРОЛЯ -------------------
    # Отправка письма для сброса пароля
    "PASSWORD_RESET_CONFIRM_EMAIL": True,
    # URL для подтверждения сброса пароля (относительный путь в приложении)
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}/",
    # Период действия токена сброса пароля (в днях)
    "PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND": False,
    # ------------------ НАСТРОЙКИ СБРОСА ИМЕНИ ПОЛЬЗОВАТЕЛЯ -------------------
    # URL для подтверждения сброса имени пользователя (относительный путь в приложении)
    "USERNAME_RESET_CONFIRM_URL": "username/reset/confirm/{uid}/{token}/",
    # Отправлять письмо при сбросе имени пользователя
    "USERNAME_RESET_CONFIRM_EMAIL": True,
    # ------------------ НАСТРОЙКИ СЕРИАЛИЗАТОРОВ -------------------
    # Пользовательские сериализаторы для различных операций
    "SERIALIZERS": {
        # Сериализатор для активации пользователя
        "activation": "djoser.serializers.ActivationSerializer",
        # Сериализатор для отображения информации о пользователе
        "user": "djoser.serializers.UserSerializer",
        # Сериализатор для создания пользователя
        "user_create": "djoser.serializers.UserCreateSerializer",
        # Сериализатор для удаления пользователя
        "user_delete": "djoser.serializers.UserDeleteSerializer",
        # Сериализатор для сброса пароля
        "password_reset": "djoser.serializers.SendEmailResetSerializer",
        # Сериализатор для подтверждения сброса пароля
        "password_reset_confirm": "djoser.serializers.PasswordResetConfirmSerializer",
        # Сериализатор для запроса сброса имени пользователя
        "username_reset": "djoser.serializers.SendEmailResetSerializer",
        # Сериализатор для подтверждения сброса имени пользователя
        "username_reset_confirm": "djoser.serializers.UsernameResetConfirmSerializer",
        # Сериализатор для установки нового пароля
        "set_password": "djoser.serializers.SetPasswordSerializer",
        # Сериализатор для установки нового имени пользователя
        "set_username": "djoser.serializers.SetUsernameSerializer",
        # Сериализатор для токена входа
        "token": "djoser.serializers.TokenSerializer",
        # Сериализатор для создания токена
        "token_create": "djoser.serializers.TokenCreateSerializer",
    },
    # ------------------ НАСТРОЙКИ ПРЕДСТАВЛЕНИЙ (VIEWS) -------------------
    # Кастомные представления для различных операций
    "PERMISSIONS": {
        # Разрешения для получения информации о пользователе
        "user": ["rest_framework.permissions.IsAuthenticated"],
        # Разрешения для обновления информации о пользователе
        "user_list": ["rest_framework.permissions.IsAdminUser"],
        # Разрешения для создания пользователя
        "user_create": ["rest_framework.permissions.AllowAny"],
        # Разрешения для удаления пользователя
        "user_delete": ["rest_framework.permissions.IsAuthenticated"],
        # Разрешения для активации пользователя
        "activation": ["rest_framework.permissions.AllowAny"],
        # Разрешения для запроса сброса пароля
        "password_reset": ["rest_framework.permissions.AllowAny"],
        # Разрешения для подтверждения сброса пароля
        "password_reset_confirm": ["rest_framework.permissions.AllowAny"],
        # Разрешения для установки нового пароля
        "set_password": ["rest_framework.permissions.IsAuthenticated"],
        # Разрешения для запроса сброса имени пользователя
        "username_reset": ["rest_framework.permissions.AllowAny"],
        # Разрешения для подтверждения сброса имени пользователя
        "username_reset_confirm": ["rest_framework.permissions.AllowAny"],
        # Разрешения для установки нового имени пользователя
        "set_username": ["rest_framework.permissions.IsAuthenticated"],
        # Разрешения для создания токена
        "token_create": ["rest_framework.permissions.AllowAny"],
        # Разрешения для действия с токеном
        "token_destroy": ["rest_framework.permissions.IsAuthenticated"],
    },
    # ------------------ НАСТРОЙКИ АУТЕНТИФИКАЦИИ -------------------
    # Поддержка токенов
    "TOKEN_MODEL": "rest_framework.authtoken.models.Token",
    # Модель пользователя
    "USER_MODEL": "auth.User",
    # Создание токена при активации пользователя
    "CREATE_TOKEN_ON_ACTIVATION": True,
    # ------------------ НАСТРОЙКИ ПРОВЕРОК БЕЗОПАСНОСТИ -------------------
    # Проверять сложность пароля при создании пользователя
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    # Отправлять письмо при изменении пароля
    "SEND_PASSWORD_CHANGED_EMAIL": True,
    # Отправлять письмо при изменении имени пользователя
    "SEND_USERNAME_CHANGED_EMAIL": True,
    # ------------------ НАСТРОЙКИ EMAIL -------------------
    # Домен сайта для писем
    "DOMAIN": "example.com",
    # Имя сайта для писем
    "SITE_NAME": "Example",
    # Протокол сайта для писем
    "PROTOCOL": "https",
    # ------------------ НАСТРОЙКИ СОЦИАЛЬНОЙ АУТЕНТИФИКАЦИИ -------------------
    # Включить социальную аутентификацию
    "SOCIAL_AUTH_ENABLED": False,
    # Токен для социальной сети при успешной авторизации
    "SOCIAL_AUTH_TOKEN_STRATEGY": "djoser.social.token.jwt.TokenStrategy",
    # Разрешения для операций социальной аутентификации
    "SOCIAL_AUTH_PERMISSIONS": ["rest_framework.permissions.AllowAny"],
}

# ------------------ ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ DJOSER -------------------

# Настройки для JWT токенов
DJOSER_JWT_AUTH = {
    # Время жизни токена доступа (в секундах)
    "JWT_ACCESS_TOKEN_LIFETIME": 60 * 5,  # 5 минут
    # Время жизни токена обновления (в секундах)
    "JWT_REFRESH_TOKEN_LIFETIME": 60 * 60 * 24 * 7,  # 7 дней
    # Длина токена в символах
    "JWT_TOKEN_LENGTH": 40,
}

# ------------------ НАСТРОЙКИ ШАБЛОНОВ EMAIL -------------------

# Путь к шаблонам email сообщений
DJOSER_EMAIL_TEMPLATES_DIR = "djoser/email"

# Префикс темы для email сообщений
DJOSER_EMAIL_SUBJECT_PREFIX = "[Example Site] "

# ------------------ НАСТРОЙКИ АКТИВАЦИИ АККАУНТА -------------------

# Время действия активационной ссылки (в секундах)
DJOSER_ACTIVATION_TOKEN_LIFETIME = 60 * 60 * 24 * 7  # 7 дней

# Деактивировать учетную запись при смене email
DJOSER_USER_EMAIL_DEACTIVATION = True

# ------------------ НАСТРОЙКИ ОГРАНИЧЕНИЙ -------------------

# Максимальное количество попыток неправильного ввода пароля
DJOSER_PASSWORD_RETRY_LIMIT = 5

# Период блокировки после превышения лимита попыток (в секундах)
DJOSER_PASSWORD_RETRY_COOLDOWN = 60 * 10  # 10 минут

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование событий djoser
DJOSER_ENABLE_LOGGING = True

# Уровень логирования
DJOSER_LOGGING_LEVEL = "INFO"
