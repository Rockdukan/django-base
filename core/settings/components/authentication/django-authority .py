"""
Настройки django-authority для гибкой системы разрешений

Компонент отвечает за:
1. Настройку системы разрешений на уровне объектов
2. Конфигурацию проверок разрешений
3. Настройки интеграции с панелью администратора
4. Регистрацию и управление пользовательскими разрешениями
"""


# ------------------ ОСНОВНЫЕ НАСТРОЙКИ AUTHORITY -------------------

# Включить django-authority
AUTHORITY_ENABLED = True

# ------------------ НАСТРОЙКИ ОБНАРУЖЕНИЯ РАЗРЕШЕНИЙ -------------------

# Автоматическое обнаружение разрешений из приложений
AUTHORITY_AUTO_DISCOVER = True

# Путь для поиска разрешений в приложениях
AUTHORITY_PERMISSION_MODELS_MODULE = "permissions"

# ------------------ НАСТРОЙКИ ПРОВЕРКИ РАЗРЕШЕНИЙ -------------------

# Включить проверку по умолчанию
AUTHORITY_USE_SMART_CACHE = True

# Время кэширования разрешений (в секундах)
AUTHORITY_CACHE_TIMEOUT = 60 * 60  # 1 час

# ------------------ НАСТРОЙКИ ПУТЕЙ -------------------

# URL-префикс для функций authority
AUTHORITY_URL_PREFIX = "authority/"

# ------------------ НАСТРОЙКИ ШАБЛОНОВ -------------------

# Корневой каталог шаблонов
AUTHORITY_TEMPLATE_DIR = "authority/"

# Шаблон для добавления разрешений
AUTHORITY_TEMPLATE_ADD_FORM = "authority/permission_form.html"

# Шаблон для удаления разрешений
AUTHORITY_TEMPLATE_DELETE_FORM = "authority/permission_delete_form.html"

# ------------------ НАСТРОЙКИ ИНТЕРФЕЙСА АДМИНИСТРАТОРА -------------------

# Включить интеграцию с админкой Django
AUTHORITY_ADMIN_INTEGRATION = True

# Интеграция с шаблонами админки
AUTHORITY_ADMIN_TEMPLATE_DIR = "authority/admin/"

# ------------------ НАСТРОЙКИ ИНТЕРФЕЙСА ПОЛЬЗОВАТЕЛЯ -------------------

# Настройки для выбора пользователей при назначении разрешений
AUTHORITY_USER_SEARCH_FIELD = "username"

# Поля для отображения при выборе пользователей
AUTHORITY_USER_DISPLAY_FIELDS = ["username", "email", "first_name", "last_name"]

# Отображать пользователей по группам
AUTHORITY_DISPLAY_USERS_BY_GROUPS = True

# ------------------ НАСТРОЙКИ РАЗРЕШЕНИЙ ПО УМОЛЧАНИЮ -------------------

# Разрешения по умолчанию, которые могут назначать администраторы
AUTHORITY_DEFAULT_PERMISSIONS = (
    "add",
    "change",
    "delete",
    "view",
)

# Настраиваемые разрешения для каждой модели
AUTHORITY_PER_MODEL_PERMISSIONS = {
    # "app_label.model_name": ["permission1", "permission2"],
}

# ------------------ НАСТРОЙКИ УВЕДОМЛЕНИЙ -------------------

# Отправлять уведомления при изменении разрешений
AUTHORITY_SEND_NOTIFICATIONS = True

# Отправлять уведомления администраторам
AUTHORITY_NOTIFY_ADMINS = True

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование изменений разрешений
AUTHORITY_ENABLE_LOGGING = True

# Уровень детализации логов
AUTHORITY_LOGGING_LEVEL = "INFO"

# ------------------ НАСТРОЙКИ ПРОИЗВОДИТЕЛЬНОСТИ -------------------

# Использовать агрегированные запросы для проверки разрешений
AUTHORITY_USE_AGGREGATED_QUERIES = True

# Лимит для количества объектов при массовой проверке разрешений
AUTHORITY_BULK_CHECK_LIMIT = 100

# ------------------ НАСТРОЙКИ ОГРАНИЧЕНИЙ -------------------

# Максимальное количество пользовательских разрешений на объект
AUTHORITY_MAX_PERMISSIONS_PER_OBJECT = 25

# Максимальное количество ролей для одного пользователя
AUTHORITY_MAX_ROLES_PER_USER = 10

# ------------------ НАСТРОЙКИ СОВМЕСТИМОСТИ -------------------

# Использовать встроенную систему разрешений Django вместе с authority
AUTHORITY_USE_DJANGO_PERMISSIONS = True

# Приоритет разрешений при конфликте (authority или django)
AUTHORITY_PRIORITY_OVER_DJANGO = True
