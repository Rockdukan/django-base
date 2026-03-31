"""
Настройки обнаружения IP-адресов пользователей

Компонент отвечает за:
1. Настройку методов определения реального IP
2. Конфигурацию заголовков для работы за прокси
3. Параметры фильтрации и валидации адресов
4. Настройки безопасности и приватности
"""


# ------------------ ОСНОВНЫЕ НАСТРОЙКИ IP DETECTION -------------------

# Включить определение IP
IP_DETECTION_ENABLED = True

# ------------------ НАСТРОЙКИ ОБНАРУЖЕНИЯ IP -------------------

# Метод определения IP-адреса
# Поддерживаемые значения:
# "REMOTE_ADDR" - стандартный метод Django
# "HTTP_X_FORWARDED_FOR" - для работы за прокси
# "HTTP_X_REAL_IP" - для работы за Nginx
# "HTTP_CLIENT_IP" - другой распространенный заголовок
# "CUSTOM" - собственный метод (требует настройки IP_DETECTION_CUSTOM_CALLBACK)
IP_DETECTION_METHOD = "REMOTE_ADDR"

# Порядок проверки заголовков для определения IP
IP_DETECTION_HEADERS_ORDER = [
    "HTTP_X_FORWARDED_FOR",
    "HTTP_X_REAL_IP",
    "HTTP_CLIENT_IP",
    "REMOTE_ADDR",
]

# ------------------ НАСТРОЙКИ ПРОКСИРОВАНИЯ -------------------

# Приложение находится за прокси/балансировщиком
IP_DETECTION_BEHIND_PROXY = False

# Количество прокси в цепочке
IP_DETECTION_PROXY_COUNT = 1

# Список доверенных прокси (IP или CIDR-нотация)
IP_DETECTION_TRUSTED_PROXIES = [
    "127.0.0.1",
    "10.0.0.0/8",
    "172.16.0.0/12",
    "192.168.0.0/16",
]

# Доверять всем прокси
IP_DETECTION_TRUST_ALL_PROXIES = False

# ------------------ НАСТРОЙКИ ФИЛЬТРАЦИИ -------------------

# Исключать частные IP-адреса из определения
IP_DETECTION_EXCLUDE_PRIVATE = True

# Исключать IP-адреса петли обратной связи (127.0.0.0/8)
IP_DETECTION_EXCLUDE_LOOPBACK = True

# Исключать IP-адреса Docker
IP_DETECTION_EXCLUDE_DOCKER = True

# Исключать IP-адреса Link-Local
IP_DETECTION_EXCLUDE_LINK_LOCAL = True

# ------------------ НАСТРОЙКИ ПРИВАТНОСТИ -------------------

# Анонимизировать IP-адреса (например, 192.168.1.1 -> 192.168.1.0)
IP_DETECTION_ANONYMIZE = False

# Степень анонимизации (количество последних октетов для IPv4 или гексетов для IPv6)
IP_DETECTION_ANONYMIZE_LEVEL = 1

# ------------------ НАСТРОЙКИ ВАЛИДАЦИИ -------------------

# Проверять валидность найденного IP-адреса
IP_DETECTION_VALIDATE_IP = True

# Поддержка IPv6
IP_DETECTION_SUPPORT_IPV6 = True

# ------------------ НАСТРОЙКИ ЗАЩИТЫ ОТ СПУФИНГА -------------------

# Включить защиту от подделки IP-адреса
IP_DETECTION_SPOOFING_PROTECTION = True

# Максимальное количество IP-адресов в заголовке X-Forwarded-For
IP_DETECTION_MAX_FORWARDED_IPS = 10

# ------------------ НАСТРОЙКИ ГЕОИНФОРМАЦИИ -------------------

# Сохранять информацию о стране/городе для IP
IP_DETECTION_STORE_GEO_INFO = False

# Провайдер геоинформации для IP
IP_DETECTION_GEO_PROVIDER = "maxmind"

# ------------------ НАСТРОЙКИ КЭШИРОВАНИЯ -------------------

# Включить кэширование результатов IP-определения
IP_DETECTION_CACHE_ENABLED = True

# Время жизни кэша (в секундах)
IP_DETECTION_CACHE_TIMEOUT = 60 * 60  # 1 час

# ------------------ НАСТРОЙКИ БЕЗОПАСНОСТИ -------------------

# Включить ограничение запросов по IP
IP_DETECTION_RATE_LIMITING = False

# Лимит запросов для одного IP (запросов/период)
IP_DETECTION_RATE_LIMIT = "100/hour"

# Путь к файлу черного списка IP-адресов
IP_DETECTION_BLACKLIST_FILE = None

# ------------------ НАСТРОЙКИ ЛОГИРОВАНИЯ -------------------

# Включить логирование операций определения IP
IP_DETECTION_ENABLE_LOGGING = True

# Уровень логирования
IP_DETECTION_LOGGING_LEVEL = "INFO"

# Журналировать все запросы с IP (может быть большим объемом данных)
IP_DETECTION_LOG_ALL_REQUESTS = False
