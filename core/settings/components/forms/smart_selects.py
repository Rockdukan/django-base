"""
Настройки django-smart-selects для зависимых выпадающих списков

Компонент отвечает за:
1. Настройку зависимых выпадающих списков
2. Конфигурацию AJAX-запросов
3. Настройки фильтрации и отображения списков
4. Параметры кэширования результатов
"""


# ------------------ ОСНОВНЫЕ НАСТРОЙКИ SMART_SELECTS -------------------

# Включить smart_selects
SMART_SELECTS_ENABLED = True

# ------------------ НАСТРОЙКИ ОТОБРАЖЕНИЯ -------------------

# Использовать jQuery UI для улучшения отображения
USE_DJANGO_JQUERY = True

# URL для jQuery, если не используется стандартная версия Django
JQUERY_URL = "https://code.jquery.com/jquery-3.6.0.min.js"

# Использовать select2 для выпадающих списков
USE_SELECT2 = True

# URL для select2, если USE_SELECT2 = True
SELECT2_URL = "https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/js/select2.min.js"

# URL для CSS select2, если USE_SELECT2 = True
SELECT2_CSS_URL = "https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/css/select2.min.css"

# ------------------ НАСТРОЙКИ AJAX ЗАПРОСОВ -------------------

# URL для AJAX запросов
SMART_SELECTS_AJAX_URL = "chained-selects/"

# Включить CSRF защиту для AJAX запросов
SMART_SELECTS_CSRF_PROTECTION = True

# Максимальное количество результатов для загрузки
SMART_SELECTS_MAX_RESULTS = 500

# Задержка перед отправкой AJAX запроса (мс)
SMART_SELECTS_AJAX_DELAY = 300

# ------------------ НАСТРОЙКИ ФИЛЬТРАЦИИ -------------------

# Фильтровать результаты на стороне клиента
SMART_SELECTS_CLIENT_SIDE_FILTERING = True

# Если True, то результаты будут загружены однократно и отфильтрованы на стороне клиента
SMART_SELECTS_PREFETCH_RESULTS = True

# ------------------ НАСТРОЙКИ КЭШИРОВАНИЯ -------------------

# Включить кэширование результатов запросов
SMART_SELECTS_CACHE_RESULTS = True

# Время жизни кэша (в секундах)
SMART_SELECTS_CACHE_TIMEOUT = 60 * 15  # 15 минут

# Ключ кэша
SMART_SELECTS_CACHE_KEY_PREFIX = "smart_selects"

# ------------------ НАСТРОЙКИ ПОВЕДЕНИЯ -------------------

# Автоматически заполнять зависимые поля при изменении родительского поля
SMART_SELECTS_AUTO_POPULATE = True

# Отображать заполнитель для пустого значения
SMART_SELECTS_SHOW_PLACEHOLDER = True

# Текст заполнителя
SMART_SELECTS_PLACEHOLDER_TEXT = "Выберите значение"

# Скрывать пустое значение, если это единственный вариант
SMART_SELECTS_HIDE_EMPTY_OPTION = True

# ------------------ НАСТРОЙКИ БЕЗОПАСНОСТИ -------------------

# Разрешенные IP-адреса для AJAX запросов
SMART_SELECTS_ALLOWED_IPS = []

# Включить защиту от CSRF для AJAX запросов
SMART_SELECTS_CSRF_PROTECT = True

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование запросов smart_selects
SMART_SELECTS_ENABLE_LOGGING = True

# Уровень логирования
SMART_SELECTS_LOGGING_LEVEL = "INFO"
