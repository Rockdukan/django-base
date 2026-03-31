"""
Настройки django-crispy-forms для Django проекта

Компонент отвечает за:
1. Улучшенный рендеринг форм в Django
2. Конфигурацию темплейтов и пакетов форм
3. Настройку шаблонов для различных CSS-фреймворков
"""

from core.settings import DEBUG

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ CRISPY FORMS -------------------

# Темплейт-пак по умолчанию для crispy-forms
# Варианты: 'bootstrap', 'bootstrap3', 'bootstrap4', 'bootstrap5', 'uni_form'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# ------------------ НАСТРОЙКИ МАКЕТОВ ФОРМЫ -------------------

# Проверять наличие тега {% crispy %} при рендеринге форм
CRISPY_FAIL_SILENTLY = not DEBUG  # Зависит от настройки DEBUG

# Использовать шаблоны с ошибками-текст вместо списков
CRISPY_ERROR_TEXT_INLINE = True

# Включить класс 'error' для полей с ошибками
CRISPY_ERROR_CLASS = "is-invalid"  # Класс ошибки для Bootstrap 4

# ------------------ НАСТРОЙКИ ПОЛЕЙ ФОРМЫ -------------------

# Класс по умолчанию для полей ввода
CRISPY_FIELD_CLASS = "form-control"  # Класс для Bootstrap 4

# ------------------ НАСТРОЙКИ ШАБЛОНОВ -------------------

# Использовать ли строгую валидацию HTML
CRISPY_STRICT_FORM_VALIDATION = True

# Название класса для обёртки поля формы
CRISPY_FORM_FIELD_WRAPPER_CLASS = "form-group"

# ------------------ НАСТРОЙКИ КНОПОК -------------------

# Классы по умолчанию для кнопок
CRISPY_BUTTON_CLASSES = {
    "submit": "btn btn-primary",  # Класс для кнопки отправки формы
    "reset": "btn btn-secondary",  # Класс для кнопки сброса формы
    "cancel": "btn btn-danger",  # Класс для кнопки отмены
}

# ------------------ НАСТРОЙКИ МАКЕТА ФОРМЫ -------------------

# Классы для различных типов макетов
CRISPY_LAYOUT_CLASSES = {
    "div": "form-row",  # Класс для div-макета
    "fieldset": "",  # Класс для fieldset-макета
    "buttonholder": "form-group",  # Класс для держателя кнопок
}
