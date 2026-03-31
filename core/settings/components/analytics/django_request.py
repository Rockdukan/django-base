"""
Настройки django-request для Django

Компонент отвечает за:
1. Отслеживание и статистику запросов пользователей
2. Мониторинг активных пользователей
3. Анализ информации о посетителях сайта
4. Сбор данных для административной панели
"""

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ -------------------

# Игнорировать AJAX запросы
REQUEST_IGNORE_AJAX = False

# IP-адреса, которые будут игнорироваться (список)
REQUEST_IGNORE_IP = None

# Логировать IP-адреса
REQUEST_LOG_IP = True

# IP-адрес для замены при REQUEST_LOG_IP = False
REQUEST_IP_DUMMY = "1.1.1.1"

# Анонимизировать IP-адреса (последний октет заменяется на 1)
REQUEST_ANONYMOUS_IP = False

# Логировать пользователей
REQUEST_LOG_USER = True

# Пользователи, которые будут игнорироваться (список имен пользователей)
REQUEST_IGNORE_USERNAME = None

# Пути, которые будут игнорироваться (кортеж регулярных выражений)
REQUEST_IGNORE_PATHS = (
    r"^admin/",  # Игнорировать админку
    r"^media/",  # Игнорировать медиа-файлы
    r"^static/",  # Игнорировать статические файлы
    r"^__debug__/",  # Игнорировать django-debug-toolbar
)

# User-агенты, которые будут игнорироваться (кортеж регулярных выражений)
REQUEST_IGNORE_USER_AGENTS = (
    r"^$",  # Игнорировать запросы без user-agent
    r"Googlebot",  # Игнорировать Google бота
    r"Baiduspider",  # Игнорировать Baidu бота
    r"YandexBot",  # Игнорировать Yandex бота
)

# Модули трафика для отображения на странице обзора
REQUEST_TRAFFIC_MODULES = (
    "request.traffic.UniqueVisitor",  # Уникальные посетители по IP
    "request.traffic.UniqueVisit",  # Визиты на основе внешних реферралов
    "request.traffic.Hit",  # Общее количество запросов
    "request.traffic.Error",  # Ошибки (500 и 404)
    "request.traffic.Search",  # Запросы из поисковых систем
    "request.traffic.User",  # Запросы от авторизованных пользователей
)

# Плагины для отображения на странице обзора
REQUEST_PLUGINS = (
    "request.plugins.TrafficInformation",  # Таблица с информацией о трафике
    "request.plugins.LatestRequests",  # Последние 5 запросов
    "request.plugins.TopPaths",  # Популярные пути
    "request.plugins.TopErrorPaths",  # Пути с ошибками
    "request.plugins.TopReferrers",  # Популярные реферреры
    "request.plugins.TopSearchPhrases",  # Поисковые фразы
    "request.plugins.TopBrowsers",  # Популярные браузеры
    # 'request.plugins.ActiveUsers',       # Активные пользователи (может быть тяжелым для больших сайтов)
)

# Базовый URL для обнаружения реферралов с того же сайта
# По умолчанию используется домен из django.contrib.sites
REQUEST_BASE_URL = None  # 'https://example.com'

# Хранить только ошибки (игнорировать успешные запросы)
REQUEST_ONLY_ERRORS = False

# Допустимые HTTP методы (запросы с другими методами будут игнорироваться)
REQUEST_VALID_METHOD_NAMES = ("get", "post", "put", "delete", "head", "options", "trace")

# ------------------ ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ -------------------

"""
# Пример 1: Шаблонный тег active_users для отображения активных пользователей

{% load request_tag %}

{# Вывод всех активных пользователей за последние 15 минут (стандартный период) #}
{% active_users as active_user_list %}
<h3>Сейчас на сайте:</h3>
<ul>
    {% for user in active_user_list %}
        <li>{{ user.username }} ({{ user.get_full_name }})</li>
    {% empty %}
        <li>Нет активных пользователей</li>
    {% endfor %}
</ul>

{# Вывод активных пользователей за последние 30 минут #}
{% active_users in 30 minutes as half_hour_active_users %}
<h3>Активны в последние 30 минут:</h3>
<ul>
    {% for user in half_hour_active_users %}
        <li>{{ user.username }}</li>
    {% endfor %}
</ul>

{# Вывод активных пользователей за последние 2 часа #}
{% active_users in 2 hours as recent_users %}


# Пример 2: Использование менеджера для получения активных пользователей в представлении

from django.shortcuts import render
from request.models import Request


def active_users_page(request):
    # Получаем активных пользователей за последние 10 минут
    active_users = Request.objects.active_users(minutes=10)
    
    return render(request, 'active_users.html', {
        'active_users': active_users,
    })


# Пример 3: Настройка команды управления для автоматической очистки старых запросов

# В crontab:
# 0 0 * * * cd /path/to/project && python manage.py purgerequests 1 month --noinput

# Или в settings.py настроить django-crontab:
CRONJOBS = [
    ('0 0 * * *', 'django.core.management.call_command', ['purgerequests', '1', 'month', '--noinput']),
]
"""
