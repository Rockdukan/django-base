"""
Настройки django-celery-results

Компонент отвечает за:
1. Хранение результатов выполнения задач Celery в базе данных Django
2. Мониторинг состояния задач через Django-админку
3. Конфигурацию модели хранения результатов
"""

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ DJANGO-CELERY-RESULTS -------------------

# Бэкенд для хранения результатов задач
CELERY_RESULT_BACKEND = "django-db"

# Модель для хранения результатов задач
# По умолчанию используется django_celery_results.models.TaskResult
# Если используется кастомная модель, указывается в виде "myapp.models.MyTaskResult"
CELERY_RESULT_BACKEND_MODEL = "django_celery_results.TaskResult"

# ------------------ НАСТРОЙКИ ХРАНЕНИЯ РЕЗУЛЬТАТОВ -------------------

# Срок хранения результатов задач (в секундах)
CELERY_RESULT_EXPIRES = 24 * 60 * 60  # 24 часа

# Максимальная длина хранимого результата (в символах)
# None — без ограничения
DJANGO_CELERY_RESULTS_TASK_RESULT_MAX_LENGTH = 20000

# ------------------ НАСТРОЙКИ ПОДРОБНОСТИ ХРАНЕНИЯ -------------------

# Сохранять traceback в случае ошибок выполнения задач
DJANGO_CELERY_RESULTS_STORE_TRACEBACKS = True

# Уровень детализации информации о задаче:
# True  - сохранять полный контекст задачи (аргументы, kwargs)
# False - сохранять минимальный набор данных
DJANGO_CELERY_RESULTS_FULL_TASK_DETAILS = True

# ------------------ НАСТРОЙКИ БЕЗОПАСНОСТИ -------------------

# Шифровать данные результатов
DJANGO_CELERY_RESULTS_ENCRYPT = False

# Ключ шифрования, если используется шифрование
DJANGO_CELERY_RESULTS_ENCRYPT_KEY = None

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование событий django-celery-results
DJANGO_CELERY_RESULTS_ENABLE_LOGGING = True

# Уровень логирования
DJANGO_CELERY_RESULTS_LOGGING_LEVEL = "INFO"

# Формат сообщений журнала
DJANGO_CELERY_RESULTS_LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
