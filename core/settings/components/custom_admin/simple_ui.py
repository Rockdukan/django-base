"""
Настройки django-simpleui для Django

Компонент отвечает за:
1. Настройку современного интерфейса администратора Django
2. Конфигурацию меню, тем и иконок
3. Кастомизацию домашней страницы администратора
4. Определение параметров пользовательского интерфейса
"""

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ -------------------

# Включить/отключить анимацию частиц на странице входа в систему
SIMPLEUI_LOGIN_PARTICLES = True

# Изменить заголовок и иконку домашней страницы
SIMPLEUI_HOME_TITLE = "Панель управления"
SIMPLEUI_HOME_ICON = "fa fa-home"

# Настроить LOGO (URL или относительный путь)
SIMPLEUI_LOGO = "https://example.com/logo.png"

# Настройка для перехода при клике на лого на домашней странице
SIMPLEUI_INDEX = "/"

# ------------------ НАСТРОЙКИ ТЕМЫ -------------------

# Установка темы по умолчанию
# Возможные значения: simpleui.css, element.css, layui.css, ant.design.css, admin.lte.css и др.
SIMPLEUI_DEFAULT_THEME = "admin.lte.css"

# ------------------ НАСТРОЙКИ ИКОНОК -------------------

# Включить/отключить иконки по умолчанию
SIMPLEUI_DEFAULT_ICON = True

# Настройка иконок для конкретных модулей
SIMPLEUI_ICON = {
    "系统管理": "fas fa-cog",
    "用户管理": "fas fa-user",
    "Аутентификация и авторизация": "fas fa-users-cog",
    "Пользователи и группы": "fas fa-users",
}

# ------------------ НАСТРОЙКИ ДОМАШНЕЙ СТРАНИЦЫ -------------------

# Показывать/скрывать информацию о сервере
SIMPLEUI_HOME_INFO = True

# Показывать/скрывать блок быстрых действий
SIMPLEUI_HOME_QUICK = True

# Показывать/скрывать блок последних действий
SIMPLEUI_HOME_ACTION = True

# ------------------ ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ -------------------

# Сбор аналитических данных (для улучшения simpleui)
SIMPLEUI_ANALYSIS = False

# Режим офлайн (загрузка статических ресурсов локально)
SIMPLEUI_STATIC_OFFLINE = False

# Показывать/скрывать загрузочный экран
SIMPLEUI_LOADING = True

# ------------------ НАСТРОЙКИ МЕНЮ -------------------

# Пример конфигурации меню
SIMPLEUI_CONFIG = {
    # Сохранять системные меню
    "system_keep": False,
    # Отображаемые меню и порядок (пустой список - не отображать ничего)
    "menu_display": ["Администрирование", "Пользователи", "Контент"],
    # Динамическое обновление меню при каждом входе
    "dynamic": False,
    # Настройка меню (можно включить до 3 уровней)
    "menus": [
        {"name": "Панель управления", "icon": "fas fa-tachometer-alt", "url": "/admin/"},
        {
            "app": "auth",
            "name": "Пользователи",
            "icon": "fas fa-user-shield",
            "models": [
                {"name": "Пользователи", "icon": "fas fa-user", "url": "auth/user/"},
                {"name": "Группы", "icon": "fas fa-users", "url": "auth/group/"},
            ],
        },
        {
            "name": "Внешние ресурсы",
            "icon": "fas fa-external-link-alt",
            "models": [
                {
                    "name": "Документация",
                    "url": "https://docs.djangoproject.com/",
                    "icon": "fas fa-book",
                    "newTab": True,
                },
                {"name": "GitHub", "url": "https://github.com/", "icon": "fab fa-github", "newTab": True},
            ],
        },
        # Пример многоуровневого меню
        {
            "name": "Контент",
            "icon": "far fa-file-alt",
            "models": [
                {
                    "name": "Статьи",
                    "icon": "fas fa-newspaper",
                    # Третий уровень меню
                    "models": [
                        {"name": "Опубликованные", "url": "/admin/content/article/?status=published"},
                        {"name": "Черновики", "url": "/admin/content/article/?status=draft"},
                    ],
                },
                {"name": "Медиа", "icon": "far fa-images", "url": "/admin/content/media/"},
            ],
        },
    ],
}

# ------------------ ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ -------------------

"""
# Пример 1: Добавление собственной кнопки действия в админке

from django.contrib import admin
from myapp.models import Article

@admin.register(Article)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created_at", "status")
    
    # Добавление кастомных действий
    actions = ["publish_selected", "custom_action"]
    
    def publish_selected(self, request, queryset):
        queryset.update(status="published")
    
    # Отображаемый текст для действия
    publish_selected.short_description = "Опубликовать выбранные статьи"
    
    # Иконка для кнопки (Font Awesome или Element UI)
    publish_selected.icon = "fas fa-check-circle"
    
    # Тип кнопки (Element UI: primary, success, warning, danger, info)
    publish_selected.type = "success"
    
    def custom_action(self, request, queryset):
        pass
    
    custom_action.short_description = "Особое действие"
    custom_action.icon = "el-icon-star-on"
    custom_action.type = "warning"
    
    # Добавление подтверждения
    custom_action.confirm = "Вы уверены, что хотите выполнить это действие?"


# Пример 2: Создание кнопки с переходом по ссылке


def link_button(self, request, queryset):
    pass

link_button.short_description = "Перейти на сайт"
link_button.icon = "fas fa-external-link-alt"
link_button.type = "primary"

# action_type: 0 - открыть на текущей странице, 1 - открыть в новой вкладке, 2 - открыть в новом окне
link_button.action_type = 1
link_button.action_url = "https://example.com"


# Пример 3: Добавление кнопки с диалоговым окном Layer (требуется AjaxAdmin)

from simpleui.admin import AjaxAdmin


class ArticleAdmin(AjaxAdmin):
    actions = ["layer_action"]
    
    def layer_action(self, request, queryset):
        # Получение данных из POST запроса
        post = request.POST
        
        # Проверка выбора элементов

        if not post.get("_selected"):
            return JsonResponse(data={
                "status": "error",
                "msg": "Пожалуйста, выберите элементы!"
            })
        
        # Бизнес-логика
        # ...
        
        return JsonResponse(data={
            "status": "success",
            "msg": "Операция выполнена успешно!"
        })
    
    layer_action.short_description = "Действие с диалогом"
    layer_action.icon = "fas fa-edit"
    layer_action.type = "success"
    
    # Настройка диалогового окна
    layer_action.layer = {
        "title": "Редактирование параметров",
        "tips": "Введите необходимые данные",
        "confirm_button": "Подтвердить",
        "cancel_button": "Отмена",
        "width": "50%",
        "labelWidth": "120px",
        "params": [
            {
                "type": "input",
                "key": "title",
                "label": "Заголовок",
                "require": True
            },
            {
                "type": "select",
                "key": "status",
                "label": "Статус",
                "value": "draft",
                "options": [
                    {"key": "published", "label": "Опубликовано"},
                    {"key": "draft", "label": "Черновик"},
                    {"key": "archived", "label": "В архиве"}
                ]
            },
            {
                "type": "date",
                "key": "publish_date",
                "label": "Дата публикации"
            }
        ]
    }
"""
