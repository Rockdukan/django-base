"""
Настройки django-floppyforms для улучшенных HTML5 форм

Компонент отвечает за:
1. Настройку рендеринга форм с использованием HTML5
2. Конфигурацию виджетов для разных типов полей
3. Настройки шаблонов для форм и виджетов
4. Параметры валидации на стороне клиента
"""


# ------------------ ОСНОВНЫЕ НАСТРОЙКИ FLOPPYFORMS -------------------

# Включить floppyforms
FLOPPYFORMS_ENABLED = True

# ------------------ НАСТРОЙКИ РЕНДЕРИНГА -------------------

# Использовать HTML5 атрибуты для валидации
FLOPPYFORMS_USE_HTML5_VALIDATION = True

# Использовать нативные виджеты для моб. устройств
FLOPPYFORMS_USE_NATIVE_WIDGETS = True

# ------------------ НАСТРОЙКИ ШАБЛОНОВ -------------------

# Директория для пользовательских шаблонов виджетов
FLOPPYFORMS_TEMPLATES_DIR = "floppyforms/"

# Шаблоны для разных виджетов
FLOPPYFORMS_WIDGET_TEMPLATES = {
    "default": "floppyforms/input.html",
    "text": "floppyforms/text.html",
    "password": "floppyforms/password.html",
    "email": "floppyforms/email.html",
    "url": "floppyforms/url.html",
    "number": "floppyforms/number.html",
    "range": "floppyforms/range.html",
    "date": "floppyforms/date.html",
    "datetime": "floppyforms/datetime.html",
    "time": "floppyforms/time.html",
    "checkbox": "floppyforms/checkbox.html",
    "radio": "floppyforms/radio.html",
    "select": "floppyforms/select.html",
    "multiselect": "floppyforms/multiselect.html",
    "textarea": "floppyforms/textarea.html",
    "file": "floppyforms/file.html",
    "clearable_file": "floppyforms/clearable_file.html",
    "date_select": "floppyforms/date_select.html",
    "time_select": "floppyforms/time_select.html",
    "datetime_select": "floppyforms/datetime_select.html",
}

# ------------------ НАСТРОЙКИ CSS КЛАССОВ -------------------

# CSS классы по умолчанию для виджетов
FLOPPYFORMS_DEFAULT_CLASSES = {
    "text": "form-control",
    "password": "form-control",
    "email": "form-control",
    "url": "form-control",
    "number": "form-control",
    "range": "form-range",
    "date": "form-control",
    "datetime": "form-control",
    "time": "form-control",
    "checkbox": "form-check-input",
    "radio": "form-check-input",
    "select": "form-select",
    "multiselect": "form-select",
    "textarea": "form-control",
    "file": "form-control",
}

# CSS классы для состояний ошибок
FLOPPYFORMS_ERROR_CLASSES = {
    "default": "is-invalid",
}

# CSS классы для состояний предупреждений
FLOPPYFORMS_WARNING_CLASSES = {
    "default": "is-warning",
}

# CSS классы для состояний успеха
FLOPPYFORMS_SUCCESS_CLASSES = {
    "default": "is-valid",
}

# ------------------ НАСТРОЙКИ HTML5 АТРИБУТОВ -------------------

# Дополнительные HTML5 атрибуты для виджетов
FLOPPYFORMS_DEFAULT_ATTRS = {
    "text": {"autocomplete": "off"},
    "password": {"autocomplete": "new-password"},
    "email": {"autocomplete": "email"},
    "number": {"step": "any"},
    "date": {"autocomplete": "off"},
    "time": {"autocomplete": "off"},
    "url": {"autocomplete": "off"},
}

# ------------------ НАСТРОЙКИ МАКЕТОВ ФОРМ -------------------

# Типы макетов для форм
FLOPPYFORMS_LAYOUTS = {
    "default": "floppyforms/layouts/default.html",
    "inline": "floppyforms/layouts/inline.html",
    "horizontal": "floppyforms/layouts/horizontal.html",
}

# Макет формы по умолчанию
FLOPPYFORMS_DEFAULT_LAYOUT = "default"

# ------------------ НАСТРОЙКИ ГРУППИРОВКИ ПОЛЕЙ -------------------

# Шаблоны для группировки полей
FLOPPYFORMS_FIELDSET_TEMPLATES = {
    "default": "floppyforms/fieldset.html",
}

# ------------------ НАСТРОЙКИ ИНТЕГРАЦИИ С BOOTSTRAP -------------------

# Включить интеграцию с Bootstrap
FLOPPYFORMS_USE_BOOTSTRAP = True

# Версия Bootstrap для интеграции
FLOPPYFORMS_BOOTSTRAP_VERSION = 5

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование для floppyforms
FLOPPYFORMS_ENABLE_LOGGING = True

# Уровень логирования
FLOPPYFORMS_LOGGING_LEVEL = "INFO"

# ------------------ НАСТРОЙКИ КЭШИРОВАНИЯ -------------------

# Включить кэширование шаблонов
FLOPPYFORMS_CACHE_TEMPLATES = True

# Время кэширования в секундах
FLOPPYFORMS_CACHE_TIMEOUT = 60 * 60  # 1 час
