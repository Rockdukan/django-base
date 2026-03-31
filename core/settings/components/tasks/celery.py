"""
Настройки Celery для асинхронных задач

Компонент отвечает за:
1. Настройку брокера сообщений и бэкенда результатов
2. Конфигурацию очередей и маршрутизации задач
3. Настройки планировщика и периодических задач
4. Параметры мониторинга и обработки ошибок
"""

import os

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ CELERY -------------------

# URL брокера сообщений
CELERY_BROKER_URL = os.environ.get("REDIS_URL", "redis://127.0.0.1:6379/1")

# URL бэкенда результатов
CELERY_RESULT_BACKEND = os.environ.get("REDIS_URL", "redis://127.0.0.1:6379/1")

# ------------------ НАСТРОЙКИ СЕРИАЛИЗАЦИИ -------------------

# Допустимые форматы сериализации данных
CELERY_ACCEPT_CONTENT = ["json"]

# Формат сериализации для задач
CELERY_TASK_SERIALIZER = "json"

# Формат сериализации для результатов
CELERY_RESULT_SERIALIZER = "json"

# ------------------ НАСТРОЙКИ ЧАСОВОГО ПОЯСА -------------------

# Часовой пояс для Celery
CELERY_TIMEZONE = "Europe/Moscow"

# ------------------ НАСТРОЙКИ ВЫПОЛНЕНИЯ ЗАДАЧ -------------------

# Выполнять задачи сразу же в синхронном режиме (для отладки)
CELERY_TASK_ALWAYS_EAGER = True

# Передавать исключения из задач при синхронном выполнении
CELERY_TASK_EAGER_PROPAGATES = True

# ------------------ ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ CELERY -------------------

# Настройки очередей
CELERY_TASK_QUEUES = {
    "default": {
        "exchange": "default",
        "exchange_type": "direct",
        "routing_key": "default",
    },
    "high_priority": {
        "exchange": "high_priority",
        "exchange_type": "direct",
        "routing_key": "high_priority",
    },
    "low_priority": {
        "exchange": "low_priority",
        "exchange_type": "direct",
        "routing_key": "low_priority",
    },
}

# Очередь по умолчанию
CELERY_TASK_DEFAULT_QUEUE = "default"

# Очередь для задач по умолчанию
CELERY_TASK_DEFAULT_EXCHANGE = "default"

# Тип обмена по умолчанию
CELERY_TASK_DEFAULT_EXCHANGE_TYPE = "direct"

# Ключ маршрутизации по умолчанию
CELERY_TASK_DEFAULT_ROUTING_KEY = "default"

# ------------------ НАСТРОЙКИ МАРШРУТИЗАЦИИ ЗАДАЧ -------------------

# Правила маршрутизации для задач
CELERY_TASK_ROUTES = {
    "myapp.tasks.high_priority_task": {"queue": "high_priority"},
    "myapp.tasks.low_priority_task": {"queue": "low_priority"},
}

# ------------------ НАСТРОЙКИ ПЛАНИРОВЩИКА -------------------

# Включить планировщик задач
CELERY_BEAT_ENABLED = True

# Планировщик по умолчанию
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

# Максимальное время работы планировщика (в секундах)
CELERY_BEAT_MAX_LOOP_INTERVAL = 5

# ------------------ НАСТРОЙКИ ПЕРИОДИЧЕСКИХ ЗАДАЧ -------------------

# Расписание периодических задач (добавьте свои при использовании Celery)
CELERY_BEAT_SCHEDULE = {}

# ------------------ НАСТРОЙКИ РЕЗУЛЬТАТОВ -------------------

# Сохранять результаты задач
CELERY_TASK_IGNORE_RESULT = False

# Срок хранения результатов задач (в секундах)
CELERY_RESULT_EXPIRES = 24 * 60 * 60  # 24 часа

# Срок хранения исключений (в секундах)
CELERY_TASK_STORE_ERRORS_EVEN_IF_IGNORED = True

# ------------------ НАСТРОЙКИ МОНИТОРИНГА -------------------

# Включить мониторинг задач
CELERY_TASK_TRACK_STARTED = True

# Время для отправки heartbeat (в секундах)
CELERY_WORKER_SEND_TASK_EVENTS = True

# Принимать события от воркеров
CELERY_WORKER_ENABLE_REMOTE_CONTROL = True

# ------------------ НАСТРОЙКИ ВОРКЕРОВ -------------------

# Префикс имени воркера
CELERY_WORKER_NAME_PREFIX = "worker"

# Количество процессов воркера
CELERY_WORKER_CONCURRENCY = 4

# Максимальное количество задач, выполняемых воркером до перезапуска
CELERY_WORKER_MAX_TASKS_PER_CHILD = 1000

# Таймаут обработки задачи (в секундах)
CELERY_TASK_TIME_LIMIT = 60 * 5  # 5 минут

# Мягкий таймаут обработки задачи (в секундах)
CELERY_TASK_SOFT_TIME_LIMIT = 60 * 3  # 3 минуты

# ------------------ НАСТРОЙКИ ОБРАБОТКИ ОШИБОК -------------------

# Количество повторных попыток выполнения при ошибке
CELERY_TASK_MAX_RETRIES = 3

# Задержка перед повторной попыткой (в секундах)
CELERY_TASK_RETRY_DELAY = 60

# Использовать экспоненциальное увеличение задержки при повторах
CELERY_TASK_RETRY_BACKOFF = True

# Множитель для экспоненциального увеличения задержки
CELERY_TASK_RETRY_BACKOFF_MAX = 600  # 10 минут

# ------------------ НАСТРОЙКИ БЕЗОПАСНОСТИ -------------------

# Опции транспорта для брокера (например, SSL/TLS)
CELERY_BROKER_TRANSPORT_OPTIONS = {"visibility_timeout": 3600}

# Включить защищенное соединение с брокером
CELERY_BROKER_USE_SSL = False

# Пул соединений для брокера
CELERY_BROKER_POOL_LIMIT = 10

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование Celery
CELERY_WORKER_HIJACK_ROOT_LOGGER = False

# Уровень логирования
CELERY_WORKER_LOG_LEVEL = "INFO"

# Формат сообщений журнала
CELERY_WORKER_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
