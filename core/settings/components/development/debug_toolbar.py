"""
Настройки Debug Toolbar для Django проекта.

Компонент задаёт INTERNAL_IPS, панели и конфиг.
DebugToolbarMiddleware добавляется в MIDDLEWARE в development.py.
"""

# ------------------ НАСТРОЙКИ ДОСТУПА -------------------

# IP-адреса, для которых будет доступна панель отладки
INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ -------------------


# Показывать DjDT везде при DEBUG, кроме ответов для Summernote (чтобы не светился в окне/iframe редактора).


def show_toolbar(request):
    from django.conf import settings

    if not settings.DEBUG:
        return False

    if request.path.startswith("/summernote/"):
        return False
    return True


# Конфигурация панели инструментов
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": "core.settings.components.development.debug_toolbar.show_toolbar",
    # Требование самого debug_toolbar: при тестах DEBUG принудительно False.
    "IS_RUNNING_TESTS": False,
    # Не перехватывать редиректы — админка и сайт работают как обычно
    "INTERCEPT_REDIRECTS": False,
    # Размер кэша результатов запросов
    "RESULTS_CACHE_SIZE": 3,
    # Показывать панель в свернутом виде при загрузке страницы
    "SHOW_COLLAPSED": True,
    # Порог времени выполнения SQL-запроса для выделения предупреждением
    "SQL_WARNING_THRESHOLD": 100,  # миллисекунды
    # Автоскрытие панели при движении мыши
    "HIDE_ON_MOUSE_LEAVE": False,
    # Максимальная глубина для inspect() в консоли
    "MAX_DEPTH": 5,
    # Отключить возможность скрывать инструментальную панель
    "DISABLE_PANELS": [],
}

# ------------------ НАСТРОЙКИ ПАНЕЛЕЙ -------------------

# Список активных панелей отладки и их порядок
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",  # История запросов
    "debug_toolbar.panels.versions.VersionsPanel",  # Версии установленных пакетов
    "debug_toolbar.panels.timer.TimerPanel",  # Таймер загрузки страницы
    "debug_toolbar.panels.settings.SettingsPanel",  # Настройки Django
    "debug_toolbar.panels.headers.HeadersPanel",  # HTTP-заголовки
    "debug_toolbar.panels.request.RequestPanel",  # Данные запроса
    "debug_toolbar.panels.sql.SQLPanel",  # SQL-запросы
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",  # Статические файлы
    "debug_toolbar.panels.templates.TemplatesPanel",  # Шаблоны
    "debug_toolbar.panels.cache.CachePanel",  # Кэширование
    "debug_toolbar.panels.signals.SignalsPanel",  # Сигналы Django
    "debug_toolbar.panels.logging.LoggingPanel",  # Логи
    # ProfilingPanel отключён: конфликт с cProfile — «Another profiling tool is already active» на /news/ и др.
    # "debug_toolbar.panels.profiling.ProfilingPanel",
]
