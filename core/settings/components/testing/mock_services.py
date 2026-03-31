"""
Настройки мокирования внешних сервисов для тестирования

Компонент отвечает за:
1. Настройку мокирования внешних API и сервисов
2. Конфигурацию ответов от мокированных сервисов
3. Настройки записи и воспроизведения запросов
4. Параметры интеграции с тестами
"""


# ------------------ ОСНОВНЫЕ НАСТРОЙКИ MOCK_SERVICES -------------------

# Включить мокирование сервисов
MOCK_SERVICES_ENABLED = True

# ------------------ НАСТРОЙКИ МОКИРОВАНИЯ HTTP -------------------

# Библиотека для мокирования HTTP запросов
# Поддерживаемые значения: "requests_mock", "responses", "vcrpy", "httmock", "httpretty"
MOCK_HTTP_LIBRARY = "requests_mock"

# Базовый URL для мокирования
MOCK_BASE_URL = "https://api.example.com"

# ------------------ НАСТРОЙКИ VCR -------------------

# Директория для хранения кассет VCR
MOCK_VCR_CASSETTE_DIR = "tests/fixtures/vcr_cassettes"

# Режим записи VCR
# Поддерживаемые значения: "all", "new_episodes", "once", "none"
MOCK_VCR_RECORD_MODE = "once"

# Фильтр для удаления конфиденциальных данных
MOCK_VCR_FILTER_SENSITIVE_DATA = [
    ("api_key=([^&]+)", "api_key=FILTERED"),
    ("password=([^&]+)", "password=FILTERED"),
    ("token=([^&]+)", "token=FILTERED"),
]

# ------------------ НАСТРОЙКИ ЗАПИСИ И ВОСПРОИЗВЕДЕНИЯ -------------------

# Включить режим записи реальных запросов
MOCK_RECORD_REAL_REQUESTS = False

# Директория для хранения записанных запросов
MOCK_RECORDS_DIR = "tests/fixtures/recordings"

# Воспроизводить записанные запросы, если нет соответствующего мока
MOCK_FALLBACK_TO_RECORDINGS = True

# ------------------ НАСТРОЙКИ МОКИРОВАНИЯ СЕРВИСОВ -------------------

# Список сервисов для мокирования
MOCK_SERVICES = [
    "payment_gateway",
    "email_service",
    "sms_service",
    "shipping_service",
    "geocoding_service",
    "authentication_service",
]

# Конфигурация для каждого сервиса
MOCK_SERVICE_CONFIGS = {
    "payment_gateway": {
        "base_url": "https://api.payment.example.com",
        "endpoints": {
            "authorize": "/payments/authorize",
            "capture": "/payments/capture",
            "refund": "/payments/refund",
        },
        "default_response": {
            "status_code": 200,
            "content": {"status": "success", "transaction_id": "mock-txn-12345"},
        },
    },
    "email_service": {
        "base_url": "https://api.email.example.com",
        "endpoints": {
            "send": "/v1/send",
            "validate": "/v1/validate",
        },
        "default_response": {
            "status_code": 200,
            "content": {"status": "queued", "message_id": "mock-msg-12345"},
        },
    },
    "sms_service": {
        "base_url": "https://api.sms.example.com",
        "endpoints": {
            "send": "/v1/messages",
            "status": "/v1/messages/{message_id}",
        },
        "default_response": {
            "status_code": 200,
            "content": {"status": "sent", "message_id": "mock-sms-12345"},
        },
    },
}

# ------------------ НАСТРОЙКИ ПОВЕДЕНИЯ МОКОВ -------------------

# Реализовать задержку в ответах моков для имитации реальных сервисов
MOCK_SIMULATE_LATENCY = False

# Минимальное время задержки (в миллисекундах)
MOCK_MIN_LATENCY = 50

# Максимальное время задержки (в миллисекундах)
MOCK_MAX_LATENCY = 300

# Вероятность ошибки в ответе мока (0-1)
MOCK_ERROR_PROBABILITY = 0.0

# ------------------ НАСТРОЙКИ ОТВЕТОВ МОКОВ -------------------

# Формат ответов моков по умолчанию (json, xml, text)
MOCK_DEFAULT_RESPONSE_FORMAT = "json"

# Код статуса по умолчанию для успешных ответов
MOCK_DEFAULT_SUCCESS_STATUS = 200

# Код статуса по умолчанию для ошибочных ответов
MOCK_DEFAULT_ERROR_STATUS = 400

# Заголовки ответов по умолчанию
MOCK_DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "X-Mocked-By": "django-mock-services",
}

# ------------------ НАСТРОЙКИ ИНТЕГРАЦИИ С PYTEST -------------------

# Автоматически включать мокирование для pytest
MOCK_PYTEST_AUTO_ENABLE = True

# Фикстура pytest для мокирования
MOCK_PYTEST_FIXTURE_NAME = "mock_services"

# Область действия фикстуры (function, class, module, session)
MOCK_PYTEST_FIXTURE_SCOPE = "function"

# ------------------ НАСТРОЙКИ ИНТЕГРАЦИИ С UNITTEST -------------------

# Миксин для unittest с поддержкой мокирования
MOCK_UNITTEST_MIXIN = "tests.mixins.MockServicesMixin"

# ------------------ НАСТРОЙКИ ШАБЛОНОВ ОТВЕТОВ -------------------

# Директория с шаблонами ответов
MOCK_RESPONSE_TEMPLATES_DIR = "tests/fixtures/mock_responses"

# Формат шаблонов (json, yaml)
MOCK_TEMPLATE_FORMAT = "json"

# ------------------ НАСТРОЙКИ АСИНХРОННОСТИ -------------------

# Поддержка асинхронных моков (для aiohttp, httpx и т.д.)
MOCK_ASYNC_ENABLED = True

# Библиотека для асинхронного мокирования
MOCK_ASYNC_LIBRARY = "aioresponses"

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование мокированных запросов
MOCK_ENABLE_LOGGING = True

# Уровень логирования
MOCK_LOGGING_LEVEL = "INFO"

# Включить подробное логирование запросов и ответов
MOCK_VERBOSE_LOGGING = True

# Формат сообщений журнала
MOCK_LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
