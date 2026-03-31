"""
Настройки django-guardian для разрешений на уровне объектов

Компонент отвечает за:
1. Настройку системы разрешений для конкретных объектов
2. Конфигурацию анонимного пользователя
3. Настройки кэширования разрешений
4. Интеграцию с панелью администратора Django
"""

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ GUARDIAN -------------------

# Включить guardian
GUARDIAN_ENABLED = True

# ------------------ НАСТРОЙКИ АУТЕНТИФИКАЦИИ -------------------

# Добавить бэкенд guardian в список бэкендов аутентификации
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",  # Стандартный бэкенд Django
    "guardian.backends.ObjectPermissionBackend",  # Бэкенд guardian
)

# ------------------ НАСТРОЙКИ АНОНИМНОГО ПОЛЬЗОВАТЕЛЯ -------------------

# Создавать анонимного пользователя при инициализации
GUARDIAN_CREATE_ANONYMOUS_USER = True

# Имя пользователя для анонимного пользователя
GUARDIAN_GET_INIT_ANONYMOUS_USER = "guardian.management.get_init_anonymous_user"

# ID пользователя для анонимного пользователя
GUARDIAN_ANONYMOUS_USER_ID = -1

# ------------------ НАСТРОЙКИ РАЗРЕШЕНИЙ -------------------

# Включить проверку разрешений объектов для пользователей суперпользователей
GUARDIAN_SUPERUSERS_HAVE_ALL_PERMISSIONS = True

# Включить кэширование разрешений
GUARDIAN_CACHE_ENABLED = True

# Имя кэша, используемого для хранения разрешений
GUARDIAN_CACHE_BACKEND = "default"

# Время хранения разрешений в кэше (в секундах)
GUARDIAN_CACHE_TIMEOUT = 3600  # 1 час

# ------------------ НАСТРОЙКИ ФУНКЦИОНАЛЬНОСТИ -------------------

# Автоматическое обнаружение моделей для разрешений
GUARDIAN_AUTO_DISCOVER = True

# Модели, исключенные из системы разрешений guardian
GUARDIAN_EXCLUDE_MODELS = []

# Модели, включенные в систему разрешений guardian (если указано, игнорирует GUARDIAN_EXCLUDE_MODELS)
GUARDIAN_INCLUDE_MODELS = []

# ------------------ НАСТРОЙКИ АДМИНИСТРАТОРА -------------------

# Включить интеграцию с администратором Django
GUARDIAN_ADMIN_INTEGRATION = True

# Показывать разрешения объектов на странице администратора пользователей
GUARDIAN_SHOW_PERMISSIONS_USERS_ADMIN = True

# Показывать разрешения объектов на странице администратора групп
GUARDIAN_SHOW_PERMISSIONS_GROUPS_ADMIN = True

# ------------------ НАСТРОЙКИ ПРОИЗВОДИТЕЛЬНОСТИ -------------------

# Использовать массовую загрузку объектов при проверке разрешений
GUARDIAN_BULK_LOAD_OBJECTS = True

# Размер пакета для массовой загрузки
GUARDIAN_BULK_BATCH_SIZE = 100

# Использовать предварительную загрузку связанных объектов
GUARDIAN_PREFETCH_RELATED = True

# ------------------ НАСТРОЙКИ ПРЕДСТАВЛЕНИЙ (VIEWS) -------------------

# Путь перенаправления при отсутствии разрешений
GUARDIAN_RAISE_403 = True

# Шаблон страницы 403 (доступ запрещен)
GUARDIAN_TEMPLATE_403 = "guardian/403.html"

# Функция для обработки запросов с отсутствием прав доступа
GUARDIAN_RENDER_403 = "guardian.utils.render_403"

# ------------------ НАСТРОЙКИ ШАБЛОНОВ -------------------

# Использовать контекстный процессор для добавления разрешений в контекст шаблона
GUARDIAN_TEMPLATE_CONTEXT_PROCESSOR = "guardian.context_processors.has_obj_perms"

# ------------------ НАСТРОЙКИ МИГРАЦИЙ -------------------

# Использовать миграции guardian
GUARDIAN_USE_MIGRATIONS = True

# ------------------ НАСТРОЙКИ СОВМЕСТИМОСТИ -------------------

# Использовать традиционную модель разрешений Django вместе с guardian
GUARDIAN_USE_DJANGO_PERMISSIONS = True

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование событий guardian
GUARDIAN_ENABLE_LOGGING = True

# Уровень логирования
GUARDIAN_LOGGING_LEVEL = "INFO"

# Формат сообщений журнала
GUARDIAN_LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
