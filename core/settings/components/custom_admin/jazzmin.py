"""
Настройки django-jazzmin для Django

Компонент отвечает за:
1. Модернизацию внешнего вида административной панели Django
2. Настройку меню, тем и пользовательского интерфейса
3. Улучшение пользовательского опыта в админке
4. Расширенную кастомизацию элементов интерфейса
"""

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ -------------------

JAZZMIN_SETTINGS = {
    # Заголовок окна браузера (по умолчанию берется из current_admin_site.site_title)
    "site_title": "Админ-панель",
    # Заголовок на странице входа (макс. 19 символов)
    "site_header": "Админ-панель",
    # Заголовок бренда в левом верхнем углу
    "site_brand": "Админка",
    # Логотип сайта, должен быть в статических файлах
    "site_logo": "images/logo.png",
    # Логотип для формы входа (по умолчанию совпадает с site_logo)
    "login_logo": None,
    # Логотип для формы входа в темном режиме
    "login_logo_dark": None,
    # CSS классы, применяемые к логотипу
    "site_logo_classes": "img-circle",
    # Относительный путь к favicon (по умолчанию совпадает с site_logo)
    "site_icon": None,
    # Приветственное сообщение на странице входа
    "welcome_sign": "Добро пожаловать в Админ-панель",
    # Копирайт в футере
    "copyright": "Acme Ltd",
    # Список моделей для поиска из поисковой строки
    # Для одной модели можно использовать просто строку, а не список
    "search_model": ["auth.User", "auth.Group"],
    # Поле в модели пользователя, содержащее аватар
    "user_avatar": None,
    ############
    # Верхнее меню #
    ############
    # Ссылки для верхнего меню
    "topmenu_links": [
        # URL, который будет реверсирован (можно добавить права)
        {"name": "Главная", "url": "admin:index", "permissions": ["auth.view_user"]},
        # Внешний URL, открывающийся в новом окне
        {"name": "GitHub", "url": "https://github.com/farridav/django-jazzmin", "new_window": True},
        # Ссылка на админку модели (права проверяются для модели)
        {"model": "auth.User"},
        # Приложение с выпадающим меню ко всем его моделям
        {"app": "books"},
    ],
    #############
    # Меню пользователя #
    #############
    # Дополнительные ссылки для меню пользователя в правом верхнем углу
    "usermenu_links": [
        {"name": "Документация", "url": "https://django-jazzmin.readthedocs.io/", "new_window": True},
        {"model": "auth.user"},
    ],
    #############
    # Боковое меню #
    #############
    # Отображать ли боковое меню
    "show_sidebar": True,
    # Автоматически раскрывать меню
    "navigation_expanded": True,
    # Скрывать эти приложения при создании бокового меню
    "hide_apps": [],
    # Скрывать эти модели при создании бокового меню
    "hide_models": [],
    # Список приложений/моделей для определения порядка бокового меню
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    # Пользовательские ссылки для добавления к группам приложений
    "custom_links": {
        "books": [
            {
                "name": "Сгенерировать отчет",
                "url": "generate_report",
                "icon": "fas fa-chart-bar",
                "permissions": ["books.view_book"],
            }
        ]
    },
    # Пользовательские иконки для приложений/моделей бокового меню
    # Полный список классов иконок: https://fontawesome.com/icons?d=gallery&m=free
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "books": "fas fa-book",
        "books.author": "fas fa-user-edit",
        "books.book": "fas fa-book-open",
    },
    # Иконки, используемые по умолчанию
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Связанное модальное окно #
    #################
    # Использовать модальные окна вместо всплывающих окон
    "related_modal_active": False,
    #############
    # Настройки UI #
    #############
    # Относительные пути к пользовательским CSS/JS скриптам
    "custom_css": None,
    "custom_js": None,
    # Загружать шрифты с fonts.googleapis.com
    "use_google_fonts_cdn": True,
    # Показывать настройщик UI в боковой панели
    "show_ui_builder": False,
    ###############
    # Вид страницы изменения #
    ###############
    # Варианты отображения страницы изменения:
    # - single (одна форма)
    # - horizontal_tabs (горизонтальные вкладки, по умолчанию)
    # - vertical_tabs (вертикальные вкладки)
    # - collapsible (раскрывающиеся секции)
    # - carousel (карусель)
    "changeform_format": "horizontal_tabs",
    # Переопределение формата для конкретных моделей
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Добавить выбор языка в админку
    "language_chooser": True,
}

# Настройки внешнего вида (темы, цвета и т.д.)
JAZZMIN_UI_TWEAKS = {
    # Тема для светлого режима (доступные темы: https://bootswatch.com/)
    "theme": "flatly",
    # Тема для темного режима (применяется, если у пользователя включен темный режим)
    "dark_mode_theme": "darkly",
    # Настройки навигационной панели
    "navbar_small_text": False,
    "navbar_fixed": True,
    "navbar_light": False,
    "navbar_color": "primary",
    # Настройки бокового меню
    "sidebar_fixed": True,
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    # Общие настройки
    "accent": "accent-primary",
    "brand_colour": "navbar-primary",
    "brand_small_text": False,
    "body_small_text": False,
    # Настройки футера
    "footer_fixed": False,
    "footer_small_text": False,
}

# ------------------ ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ -------------------
# Пример 1: Настройка пользовательского формата страницы изменения для модели

from django.contrib import admin
from myapp.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Основная информация",
            {
                "fields": ("title", "author", "published_date"),
            },
        ),
        (
            "Дополнительно",
            {
                "fields": ("isbn", "pages", "language"),
            },
        ),
        (
            "Метаданные",
            {
                "fields": ("created_at", "updated_at"),
            },
        ),
    )

    # Порядок отображения секций на странице
    jazzmin_section_order = ("Основная информация", "Дополнительно", "Метаданные")


# Пример 2: Настройка производительности фильтров


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ("author", "genre", "language")

    # Рендерить отфильтрованные опции только после ввода минимального количества символов
    filter_input_length = {
        "author": 3,  # Отображать варианты автора только после ввода 3 символов
        "genre": 2,  # Отображать варианты жанра только после ввода 2 символов
    }


# Пример 3: Добавление дополнительных действий в форму модели
# Создайте шаблон в каталоге templates/admin/myapp/book/submit_line.html

EXAMPLE_SUBMIT_LINE_TEMPLATE = """
{% extends "admin/submit_line.html" %}

{% block extra-actions %}
{# Простая ссылка #}
<div class="form-group">
    <a href="/admin/export-book-list/" class="btn btn-outline-info form-control">Экспорт списка</a>
</div>

{# Кнопка для обработки с формой #}
<div class="form-group">
    <input type="submit" class="btn btn-outline-warning form-control" value="Опубликовать" name="_publish">
</div>
{% endblock %}
"""


# И добавьте обработку в классе админки:
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # ... другие настройки ...

    def response_change(self, request, obj):
        ret = super().response_change(request, obj)

        if "_publish" in request.POST:
            obj.status = "published"
            obj.save()
            self.message_user(request, "Книга опубликована успешно")
            return ret
        return ret


# Пример 4: Пользовательский дашборд с Jazzmin
# Создайте файл dashboard.py в корне вашего проекта

from django.utils.translation import gettext_lazy as _
from jazzmin.dashboard import Dashboard, modules


class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
        # Приложения
        self.children.append(
            modules.AppList(
                _("Каталог"),
                models=("myapp.book", "myapp.author", "myapp.genre"),
                column=0,
            )
        )

        # Пользователи и группы
        self.children.append(
            modules.AppList(
                _("Пользователи"),
                models=("django.contrib.auth.*",),
                column=1,
            )
        )

        # Последние действия
        self.children.append(
            modules.RecentActions(
                _("Последние действия"),
                limit=10,
                column=2,
            )
        )

        # Внешние ссылки
        self.children.append(
            modules.LinkList(
                _("Внешние ресурсы"),
                children=[
                    {
                        "title": _("Документация Django"),
                        "url": "https://docs.djangoproject.com/",
                        "external": True,
                    },
                    {
                        "title": _("Документация Jazzmin"),
                        "url": "https://django-jazzmin.readthedocs.io/",
                        "external": True,
                    },
                ],
                column=2,
            )
        )


# И настройте его в settings.py:
# JAZZMIN_SETTINGS = {
#     ...
#     "custom_dashboard": "myproject.dashboard.CustomIndexDashboard",
# }
