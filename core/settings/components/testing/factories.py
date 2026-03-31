"""
Настройки Factory Boy для создания тестовых данных

Компонент отвечает за:
1. Настройку фабрик для создания тестовых объектов
2. Конфигурацию генераторов случайных данных
3. Настройки последовательностей и связей между объектами
4. Параметры интеграции с тестами
"""


# ------------------ ОСНОВНЫЕ НАСТРОЙКИ FACTORIES -------------------

# Включить Factory Boy для тестов
FACTORY_BOY_ENABLED = True

# ------------------ НАСТРОЙКИ ГЕНЕРАЦИИ ДАННЫХ -------------------

# Использовать детерминированную последовательность (для воспроизводимости тестов)
FACTORY_DETERMINISTIC_SEQUENCE = True

# Начальное значение для генератора случайных чисел (для воспроизводимости)
FACTORY_RANDOM_SEED = 12345

# ------------------ НАСТРОЙКИ FAKER -------------------

# Локаль для Faker (генератора случайных данных)
FACTORY_FAKER_LOCALE = "ru_RU"

# Провайдеры Faker, которые следует использовать
FACTORY_FAKER_PROVIDERS = [
    "faker.providers.address",
    "faker.providers.company",
    "faker.providers.date_time",
    "faker.providers.internet",
    "faker.providers.lorem",
    "faker.providers.person",
    "faker.providers.phone_number",
    "faker.providers.python",
    "faker.providers.ssn",
]

# ------------------ НАСТРОЙКИ ИНТЕГРАЦИИ С DJANGO -------------------

# Включить интеграцию с Django ORM
FACTORY_DJANGO_GET_OR_CREATE = False

# Стратегия сохранения объектов по умолчанию
# Допустимые значения: "build", "create", "build_strategy"
FACTORY_STRATEGY = "create"

# ------------------ НАСТРОЙКИ ИНИЦИАЛИЗАЦИИ БАЗЫ ДАННЫХ -------------------

# Автоматически заполнять базу данных тестовыми данными
FACTORY_AUTO_POPULATE_DATABASE = False

# Количество экземпляров каждой модели при автозаполнении
FACTORY_DEFAULT_BATCH_SIZE = 10

# Модели для автозаполнения
FACTORY_AUTO_POPULATE_MODELS = [
    "auth.User",
    "auth.Group",
]

# ------------------ НАСТРОЙКИ СВЯЗЕЙ МЕЖДУ МОДЕЛЯМИ -------------------

# Создавать связанные объекты автоматически
FACTORY_CREATE_RELATED_OBJECTS = True

# Стратегия для связанных объектов (create, build, batch)
FACTORY_RELATED_STRATEGY = "create"

# Максимальная глубина создания связанных объектов
FACTORY_MAX_RELATION_DEPTH = 5

# ------------------ НАСТРОЙКИ ПРОИЗВОДИТЕЛЬНОСТИ -------------------

# Использовать пакетное создание объектов для оптимизации
FACTORY_USE_BATCH_CREATE = True

# Размер пакета для batch_create
FACTORY_BATCH_SIZE = 100

# ------------------ НАСТРОЙКИ ПОСЛЕДОВАТЕЛЬНОСТЕЙ -------------------

# Сбрасывать последовательности после каждого теста
FACTORY_RESET_SEQUENCES = True

# Начальное значение для последовательностей
FACTORY_SEQUENCE_INITIAL = 1

# ------------------ НАСТРОЙКИ ФАЙЛОВ И МЕДИА -------------------

# Директория для временных файлов, создаваемых фабриками
FACTORY_TEMP_DIR = "tmp/factory_files"

# Максимальный размер генерируемых файлов (в байтах)
FACTORY_MAX_FILE_SIZE = 1024 * 1024  # 1 MB

# ------------------ НАСТРОЙКИ МОКИРОВАНИЯ -------------------

# Включить автоматическое создание моков для внешних сервисов
FACTORY_AUTO_MOCK_SERVICES = True

# Список сервисов для мокирования
FACTORY_MOCK_SERVICES = [
    "payment_gateway",
    "email_service",
    "sms_service",
]

# ------------------ НАСТРОЙКИ ОТЛАДКИ -------------------

# Включить режим отладки фабрик
FACTORY_DEBUG = False

# Лазурить предупреждения о создании большого количества объектов
FACTORY_WARN_LARGE_BATCH = True

# Пороговое значение для предупреждений о больших пакетах
FACTORY_LARGE_BATCH_THRESHOLD = 1000

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование операций с фабриками
FACTORY_ENABLE_LOGGING = True

# Уровень логирования
FACTORY_LOGGING_LEVEL = "INFO"
