"""
Настройки django-widget-tweaks для Django проекта

Компонент отвечает за:
1. Дополнительную конфигурацию для модификации виджетов форм в шаблонах
2. Глобальные атрибуты для автоматического добавления к виджетам форм
"""

# ------------------ НАСТРОЙКИ WIDGET TWEAKS -------------------

# Настройка глобальных классов для стандартных виджетов
# Эти классы будут применены ко всем виджетам указанного типа
WIDGET_TWEAKS_GLOBAL_CLASSES = {
    "TextInput": "form-control",
    "NumberInput": "form-control",
    "EmailInput": "form-control",
    "URLInput": "form-control",
    "PasswordInput": "form-control",
    "Textarea": "form-control",
    "DateInput": "form-control datepicker",
    "DateTimeInput": "form-control datetimepicker",
    "TimeInput": "form-control timepicker",
    "Select": "form-control select2",
    "SelectMultiple": "form-control select2-multiple",
    "CheckboxInput": "form-check-input",
    "RadioSelect": "form-check-input",
    "CheckboxSelectMultiple": "form-check-input",
    "FileInput": "form-control-file",
}

# ------------------ ДОПОЛНИТЕЛЬНЫЕ АТРИБУТЫ -------------------

# Глобальные атрибуты для добавления к виджетам
WIDGET_TWEAKS_GLOBAL_ATTRS = {
    "TextInput": {"autocomplete": "off"},
    "PasswordInput": {"autocomplete": "new-password"},
    "DateInput": {"data-provide": "datepicker"},
    "EmailInput": {"autocomplete": "email"},
    "NumberInput": {"step": "any"},
}

# ------------------ КЛАССЫ ДЛЯ СОСТОЯНИЙ ОШИБОК -------------------

# Классы стилей для полей с ошибками
WIDGET_TWEAKS_ERROR_CLASS = "is-invalid"

# Классы стилей для полей с предупреждениями
WIDGET_TWEAKS_WARNING_CLASS = "is-warning"

# Классы стилей для успешно заполненных полей
WIDGET_TWEAKS_SUCCESS_CLASS = "is-valid"

# ------------------ ДОПОЛНИТЕЛЬНЫЕ ШАБЛОНЫ -------------------

# Переопределение шаблонов рендеринга для специфических полей
WIDGET_TWEAKS_TEMPLATE_OVERRIDES = {
    # Именя файлов шаблонов для переопределения стандартного рендеринга
}
