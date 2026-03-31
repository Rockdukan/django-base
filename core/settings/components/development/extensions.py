"""
Настройки django-extensions для Django проекта

Компонент отвечает за:
1. Конфигурацию django-extensions для улучшения разработки
2. Настройку дополнительных команд management
3. Инструменты для генерации кода и документации
"""

# ------------------ НАСТРОЙКИ SHELL_PLUS -------------------

# Автоматический импорт моделей и других классов в shell_plus
SHELL_PLUS = "ipython"

# Дополнительные пакеты для автоимпорта в shell_plus
SHELL_PLUS_IMPORTS = [
    "from datetime import datetime, date, timedelta",
    "import json",
    "import os",
    "import sys",
    "import time",
    "import pytz",
]

# Настройки печати при запуске shell_plus
SHELL_PLUS_PRINT_SQL = True  # Печать выполняемых SQL-запросов
SHELL_PLUS_PRINT_SQL_TRUNCATE = 1000  # Обрезать SQL-запросы при печати

# ------------------ НАСТРОЙКИ GRAPH MODELS -------------------

# Настройки для команды graph_models (генерация диаграмм моделей)
GRAPH_MODELS = {
    "all_applications": False,  # Не включать все приложения по умолчанию
    "group_models": True,  # Группировать модели по приложениям
    "exclude_models": [
        "LogEntry",
        "Session",
        "ContentType",
        "Permission",
    ],
    "output": "models_diagram.png",  # Имя файла по умолчанию
    "include_models": [],  # Какие модели включать (пусто = все)
}

# ------------------ НАСТРОЙКИ RUNSERVER_PLUS -------------------

# Использовать Werkzeug для запуска сервера разработки
RUNSERVER_PLUS = True

# Файл для хранения логов runserver_plus
RUNSERVERPLUS_SERVER_ADDRESS_PORT = "0.0.0.0:8000"

# ------------------ НАСТРОЙКИ NOTEBOOK -------------------

# Дополнительные настройки для команды notebook
NOTEBOOK_ARGUMENTS = [
    "--ip",
    "0.0.0.0",
    "--port",
    "8888",
    "--no-browser",
    "--allow-root",
]

# ------------------ НАСТРОЙКИ ДЛЯ ГЕНЕРАЦИИ КОДА -------------------

# Шаблоны для генерации скриптов и моделей
EXTENSIONS_TEMPLATES_DIR = "templates/extensions"

# ------------------ НАСТРОЙКИ ОТЛАДКИ И ПРОФИЛИРОВАНИЯ -------------------

# URL-паттерны для автоматического профилирования
EXTENSIONS_PROFILING_URLS = []

# ------------------ НАСТРОЙКИ ДОКУМЕНТАЦИИ -------------------

# Настройки для автоматической генерации документации
EXTENSIONS_DOC_TITLE = "Django Project Documentation"
EXTENSIONS_DOC_DESCRIPTION = "Автоматически сгенерированная документация"
