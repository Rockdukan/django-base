"""
Настройки django-silk

Компонент отвечает за:
1. Профилирование SQL-запросов и скорости запросов
2. Отладку производительности проекта
"""

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ SILK -------------------

# Включить Silk (только в режиме DEBUG)
SILKY_PYTHON_PROFILER = True
SILKY_AUTHENTICATION = False
SILKY_AUTHORISATION = False
SILKY_META = True

# URL silk-панели
SILKY_URL_PATH = "/cabinet/silk/"
