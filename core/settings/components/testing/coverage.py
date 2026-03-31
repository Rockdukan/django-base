"""
Настройки Coverage.py для измерения покрытия кода тестами

Компонент отвечает за:
1. Настройку измерения покрытия кода тестами
2. Конфигурацию отчетов о покрытии
3. Настройки включения/исключения файлов и директорий
4. Параметры интеграции с CI/CD
"""

import os

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ COVERAGE -------------------

# Включить измерение покрытия кода
COVERAGE_ENABLED = True

# ------------------ НАСТРОЙКИ ЗАПУСКА -------------------

# Команда для запуска измерения покрытия
COVERAGE_COMMAND = "coverage run"

# Опции для запуска
COVERAGE_RUN_OPTIONS = "--source=."

# Где искать файлы конфигурации coverage
COVERAGE_RCFILE = ".coveragerc"

# ------------------ НАСТРОЙКИ ОТЧЕТОВ -------------------

# Форматы отчетов покрытия
COVERAGE_REPORT_FORMATS = [
    "html",
    "xml",
    "term",
    "json",
]

# Директория для HTML-отчета
COVERAGE_HTML_REPORT_DIR = "htmlcov"

# Имя файла для XML-отчета
COVERAGE_XML_REPORT_FILE = "coverage.xml"

# Имя файла для JSON-отчета
COVERAGE_JSON_REPORT_FILE = "coverage.json"

# Минимальный процент покрытия для успешного прохождения
COVERAGE_MINIMUM_PERCENTAGE = 80

# ------------------ НАСТРОЙКИ ИСТОЧНИКОВ -------------------

# Список источников кода для анализа покрытия
COVERAGE_SOURCE = [
    "apps",
    "config",
]

# Шаблоны включения файлов
COVERAGE_INCLUDE = [
    "*/apps/*",
    "*/config/*",
]

# Шаблоны исключения файлов
COVERAGE_EXCLUDE = [
    "*/tests/*",
    "*/migrations/*",
    "*/admin.py",
    "*/apps.py",
    "*/urls.py",
    "*/wsgi.py",
    "*/asgi.py",
    "*/settings.py",
    "*/conftest.py",
    "manage.py",
]

# Шаблоны исключения строк
COVERAGE_EXCLUDE_LINES = [
    "pragma: no cover",
    "def __repr__",
    "def __str__",
    "if settings.DEBUG",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
    "pass",
    "raise ImportError",
]

# ------------------ НАСТРОЙКИ ВЕТВЕЙ -------------------

# Включить измерение покрытия ветвей
COVERAGE_BRANCH = True

# ------------------ НАСТРОЙКИ ИНТЕГРАЦИИ С CI/CD -------------------

# Включить генерацию отчета для Codecov
COVERAGE_CODECOV_ENABLED = True

# Включить генерацию отчета для Coveralls
COVERAGE_COVERALLS_ENABLED = False

# Токен для Codecov
COVERAGE_CODECOV_TOKEN = os.environ.get("CODECOV_TOKEN", "")

# Токен для Coveralls
COVERAGE_COVERALLS_TOKEN = os.environ.get("COVERALLS_TOKEN", "")

# ------------------ НАСТРОЙКИ ПАРАЛЛЕЛЬНОГО ВЫПОЛНЕНИЯ -------------------

# Включить параллельное выполнение
COVERAGE_PARALLEL = True

# Объединять данные из разных процессов
COVERAGE_COMBINE = True

# ------------------ НАСТРОЙКИ ДОПОЛНИТЕЛЬНЫХ ПЛАГИНОВ -------------------

# Плагины для измерения покрытия
COVERAGE_PLUGINS = [
    "django_coverage_plugin",
]

# ------------------ НАСТРОЙКИ DJANGO INTEGRATION -------------------

# Включить учет шаблонов Django
COVERAGE_MEASURE_DJANGO_TEMPLATES = True

# ------------------ НАСТРОЙКИ ОТЧЕТОВ ПОКРЫТИЯ ДЛЯ РАЗНЫХ СРЕД -------------------

# Настройки отчетов для разных сред
COVERAGE_ENVIRONMENTS = {
    "development": {
        "html": True,
        "term": True,
        "xml": False,
        "json": False,
        "minimum_percentage": 70,
    },
    "staging": {
        "html": True,
        "term": True,
        "xml": True,
        "json": False,
        "minimum_percentage": 75,
    },
    "production": {
        "html": True,
        "term": True,
        "xml": True,
        "json": True,
        "minimum_percentage": 80,
    },
}

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование операций coverage
COVERAGE_ENABLE_LOGGING = True

# Уровень логирования
COVERAGE_LOGGING_LEVEL = "INFO"
