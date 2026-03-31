"""
Настройки django-grappelli для Django

Компонент отвечает за:
1. Улучшенный интерфейс административной панели Django
2. Настройку дашборда и пользовательских модулей
3. Кастомизацию меню, тем и иконок
4. Расширение функциональности административного интерфейса
"""

from django.utils.translation import gettext_lazy as _

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ -------------------

# Заголовок административного сайта (переводится при смене языка)
_ADMIN_HEADER = _("Администрирование сайта")
GRAPPELLI_ADMIN_TITLE = _ADMIN_HEADER
GRAPPELLI_ADMIN_HEADLINE = _ADMIN_HEADER

# Лимит для автодополнения в выпадающих списках
GRAPPELLI_AUTOCOMPLETE_LIMIT = 10

# Поля поиска для автодополнения для моделей, которые нельзя изменить
GRAPPELLI_AUTOCOMPLETE_SEARCH_FIELDS = {
    "auth": {
        "user": ("id__iexact", "username__icontains", "email__icontains"),
        "group": ("id__iexact", "name__icontains"),
    }
}

# ------------------ НАСТРОЙКИ ПОЛЬЗОВАТЕЛЕЙ -------------------

# Включить функцию переключения между пользователями
GRAPPELLI_SWITCH_USER = True

# Функция для определения, может ли пользователь переключаться на других
# По умолчанию: все суперпользователи
# GRAPPELLI_SWITCH_USER_ORIGINAL = lambda user: user.is_superuser

# Функция для определения, на кого можно переключиться
# По умолчанию: все пользователи со staff=True, кроме суперпользователей
# GRAPPELLI_SWITCH_USER_TARGET = (
#     lambda user: user.is_staff and not user.is_superuser
# )

# ------------------ НАСТРОЙКИ ИНТЕРФЕЙСА -------------------

# Замена HTML5 типов ввода на text для совместимости
GRAPPELLI_CLEAN_INPUT_TYPES = True

# ------------------ НАСТРОЙКИ ДАШБОРДА -------------------

# Путь к классу дашборда для индексной страницы админки
GRAPPELLI_INDEX_DASHBOARD = "core.dashboard.CustomIndexDashboard"

# Или для нескольких административных сайтов
# GRAPPELLI_INDEX_DASHBOARD = {
#     "django.contrib.admin.site": (
#         "myproject.dashboard.CustomIndexDashboard"
#     ),
#     "myproject.admin.custom_admin_site": (
#         "myproject.custom_dashboard.CustomDashboard"
#     ),
# }

# ------------------ ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ -------------------

"""
# Пример 1: Создание сворачиваемой секции в админке модели

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)


class MyModelAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Основная информация", {
            "fields": ("title", "description", "published_date",),
        }),
        ("Дополнительно", {
            # Секция будет свернута по умолчанию
            "classes": ("grp-collapse grp-closed",),
            "fields": ("meta_keywords", "meta_description", "tags",),
        }),
        ("Настройки", {
            # Секция будет развернута по умолчанию
            "classes": ("grp-collapse grp-open",),
            "fields": ("status", "featured", "allow_comments",),
        }),
    )


# Пример 2: Настройка сортировки для вложенных инлайнов

from django.db import models


class MyModel(models.Model):
    title = models.CharField(max_length=200)


class MyInlineModel(models.Model):
    parent = models.ForeignKey(MyModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    position = models.PositiveSmallIntegerField("Позиция", null=True)
    
    class Meta:
        ordering = ["position"]


class MyInlineModelAdmin(admin.StackedInline):
    model = MyInlineModel
    fields = ("title", "position",)
    sortable_field_name = "position"  # Указывает поле для сортировки
    
    # Для скрытия поля position можно использовать
    # GrappelliSortableHiddenMixin
    # from grappelli.forms import GrappelliSortableHiddenMixin
    # class MyInlineModelAdmin(
    #     GrappelliSortableHiddenMixin,
    #     admin.StackedInline):
    #     fields = ("title",)  # position будет скрыто


# Пример 3: Использование related lookups

@admin.register(MyModel)


class MyModelAdmin(admin.ModelAdmin):
    raw_id_fields = ("related_fk", "related_m2m",)
    
    # Для foreign keys
    related_lookup_fields = {
        "fk": ["related_fk"],
        "m2m": ["related_m2m"],
    }
    
    # Для generic relations
    # related_lookup_fields = {
    #     "generic": [
              ["content_type", "object_id"],
              ["relation_type", "relation_id"]],
    # }


# Пример 4: Использование autocomplete lookups


class Author(models.Model):
    name = models.CharField(max_length=100)
    
    @staticmethod

    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains",)

@admin.register(Book)


class BookAdmin(admin.ModelAdmin):
    raw_id_fields = ("author",)
    autocomplete_lookup_fields = {
        "fk": ["author"],
    }


# Пример 5: Настройка пользовательского дашборда (dashboard.py)

from django.utils.translation import gettext_lazy as _
from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):

    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)
        
        # Добавляем модуль списка приложений "Приложения"
        self.children.append(modules.AppList(
            title=_("Приложения"),
            column=1,
            collapsible=True,
            exclude=("django.contrib.*",),
        ))
        
        # Добавляем модуль списка приложений "Администрирование"
        self.children.append(modules.AppList(
            title=_("Администрирование"),
            column=1,
            collapsible=True,
            models=("django.contrib.*",),
        ))
        
        # Добавляем модуль недавних действий
        self.children.append(modules.RecentActions(
            title=_("Последние действия"),
            column=2,
            collapsible=False,
            limit=5,
        ))
        
        # Добавляем модуль списка ссылок
        self.children.append(modules.LinkList(
            title=_("Поддержка"),
            column=2,
            collapsible=False,
            children=[
                {
                    "title": _("Документация Django"),
                    "url": "https://docs.djangoproject.com/",
                    "external": True,
                    "description": _("Официальная документация Django"),
                    "target": "_blank",
                },
                {
                    "title": _("Документация Grappelli"),
                    "url": "https://django-grappelli.readthedocs.io/",
                    "external": True,
                    "target": "_blank",
                },
            ]
        ))


# Пример 6: Настройка альтернативного шаблона для списка изменений

@admin.register(MyModel)


class MyModelAdmin(admin.ModelAdmin):
    # Фильтры в виде выпадающего списка с кнопкой "Применить"
    change_list_template = "admin/change_list_filter_confirm.html"
    
    # Или фильтры в боковой панели с автоматическим применением
    # change_list_template = "admin/change_list_filter_sidebar.html"
    
    # Настройка отображения фильтров
    change_list_filter_template = "admin/filter_listing.html"
"""
