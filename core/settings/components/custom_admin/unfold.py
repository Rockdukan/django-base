from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

"""
Настройки интерфейса администратора для Django Unfold

Компонент отвечает за:
1. Конфигурацию заголовков и иконок
2. Управление отображением элементов интерфейса
3. Настройку цветовой схемы и оформления
4. Расширенные возможности навигации
5. Подключение пользовательских стилей и скриптов
"""

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ -------------------

UNFOLD = {
    # Заголовок страницы (отображается в <title>)
    "SITE_TITLE": "Панель администратора",
    # Заголовок в боковой панели
    "SITE_HEADER": "Административная панель",
    # Подзаголовок под SITE_HEADER
    "SITE_SUBHEADER": "Добро пожаловать в систему управления",
    # Главный URL панели администратора
    "SITE_URL": "/admin/",
    # Выпадающее меню в заголовке
    "SITE_DROPDOWN": [
        {
            "icon": "diamond",  # Иконка пункта меню
            "title": _("Главная страница"),  # Название пункта
            "link": reverse_lazy("admin:index"),  # Ссылка на раздел
        },
    ],
    # Иконка сайта (разные версии для светлой и тёмной тем)
    "SITE_ICON": {
        "light": lambda request: static("icon-light.svg"),
        "dark": lambda request: static("icon-dark.svg"),
    },
    # Логотип (разные версии для светлой и тёмной тем)
    "SITE_LOGO": {
        "light": lambda request: static("logo-light.svg"),
        "dark": lambda request: static("logo-dark.svg"),
    },
    # Показывать кнопку "История"
    "SHOW_HISTORY": True,
    # Показывать кнопку "Просмотр на сайте"
    "SHOW_VIEW_ON_SITE": True,
    # Показывать кнопку "Назад" в формах редактирования
    "SHOW_BACK_BUTTON": False,
    # Тема
    "THEME": "dark",
    # Настройки страницы входа
    "LOGIN": {
        # Фоновое изображение страницы входа
        "image": lambda request: static("images/login-bg.jpg"),
        # Перенаправление после входа
        "redirect_after": lambda request: reverse_lazy("admin:auth_user_changelist"),
    },
    # Подключение пользовательских CSS-стилей
    "STYLES": [
        lambda request: static("css/custom-style.css"),
    ],
    # Подключение пользовательских JS-скриптов
    "SCRIPTS": [
        lambda request: static("js/custom-script.js"),
    ],
    # Скругление углов элементов интерфейса
    "BORDER_RADIUS": "6px",
    # Цветовая схема
    "COLORS": {
        # Основной цвет
        "primary": {
            "500": "168 85 247",
        },
        "font": {
            # Основной цвет текста (светлая тема)
            "default-light": "var(--color-base-600)",
            # Основной цвет текста (тёмная тема)
            "default-dark": "var(--color-base-300)",
        },
    },
    # Настройки локализации (например, флаги для языков)
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "ru": "🇷🇺",  # Русский
                "en": "🇬🇧",  # Английский
            },
        },
    },
    # Боковая панель навигации
    "SIDEBAR": {
        # Показывать строку поиска в боковой панели
        "show_search": False,
        # Показывать список всех приложений
        "show_all_applications": False,
        "navigation": [
            {
                # Название раздела
                "title": _("Навигация"),
                # Разделительная линия сверху
                "separator": True,
                # Возможность сворачивания раздела
                "collapsible": True,
                "items": [
                    {
                        # Название пункта меню
                        "title": _("Пользователи"),
                        # Иконка
                        "icon": "people",
                        # Ссылка на список пользователей
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                ],
            },
        ],
    },
}

# ------------------ CALLBACK-ФУНКЦИИ -------------------


def dashboard_callback(request, context):
    """
    Подготавливает переменные для отображения на главной
    странице панели администратора.
    """
    context.update(
        {
            "custom_dashboard_data": "Данные для панели управления",
        }
    )
    return context


def environment_callback(request):
    """
    Возвращает информацию о среде
    например, Production, Staging и т. д.).
    """
    # Цветовая метка среды (info, warning, danger, success)
    return ["Production", "danger"]


def permission_callback(request):
    """Проверка прав доступа для пользователей."""
    return request.user.has_perm("auth.view_user")
