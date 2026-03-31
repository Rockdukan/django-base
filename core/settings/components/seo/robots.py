"""
Настройки robots.txt для Django

Компонент отвечает за настройку django-robots или аналогичных приложений,
которые обеспечивают динамическую генерацию файла robots.txt.

Robots.txt указывает поисковым роботам, какие страницы сайта следует
индексировать, а какие - игнорировать.
"""

import os

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ -------------------

# Время кэширования robots.txt в секундах (по умолчанию 24 часа)
ROBOTS_CACHE_TIMEOUT = int(os.environ.get("ROBOTS_CACHE_TIMEOUT", str(60 * 60 * 24)))

# Использовать имя хоста в путях robots.txt
# Если True, пути будут включать хост (https://example.com/path)
# Если False, пути будут относительными (/path)
ROBOTS_USE_HOST = os.environ.get("ROBOTS_USE_HOST", "False") == "True"

# Использовать схему (http/https) в хосте при ROBOTS_USE_HOST=True
ROBOTS_USE_SCHEME_IN_HOST = os.environ.get("ROBOTS_USE_SCHEME_IN_HOST", "True") == "True"

# ------------------ НАСТРОЙКИ SITEMAP -------------------

# Включить ссылку на sitemap.xml в robots.txt
ROBOTS_USE_SITEMAP = os.environ.get("ROBOTS_USE_SITEMAP", "False") == "True"

# URL-адреса карт сайта (sitemap.xml)
# Можно указать несколько адресов, если у вас несколько карт сайта
default_sitemap = os.environ.get("ROBOTS_SITEMAP_URL", "")
ROBOTS_SITEMAP_URLS = []

if default_sitemap:
    ROBOTS_SITEMAP_URLS.append(default_sitemap)

# Дополнительные sitemap URLs из переменной окружения
if os.environ.get("ROBOTS_ADDITIONAL_SITEMAPS"):
    additional_sitemaps = os.environ.get("ROBOTS_ADDITIONAL_SITEMAPS").split(",")
    ROBOTS_SITEMAP_URLS.extend([url.strip() for url in additional_sitemaps])

# Имя представления (view) для карты сайта
# Используется, если sitemap генерируется динамически с помощью Django
ROBOTS_SITEMAP_VIEW_NAME = os.environ.get("ROBOTS_SITEMAP_VIEW_NAME", "django.contrib.sitemaps.views.sitemap")

# ------------------ РАСШИРЕННЫЕ НАСТРОЙКИ -------------------

# Имя хоста по умолчанию, используемое при построении абсолютных URL
ROBOTS_DEFAULT_HOST = os.environ.get("ROBOTS_DEFAULT_HOST", "")

# Поддержка i18n в robots.txt
# Если True, будут созданы правила с учетом языков
ROBOTS_I18N_URLS = os.environ.get("ROBOTS_I18N_URLS", "False") == "True"

# Правила по умолчанию для роботов (если используется программная настройка)
# Формат: [("User-agent", "*"), ("Disallow", "/admin/"), ("Allow", "/")]
ROBOTS_DEFAULT_RULES = []

if os.environ.get("ROBOTS_DEFAULT_USER_AGENT"):
    user_agent = os.environ.get("ROBOTS_DEFAULT_USER_AGENT")
    ROBOTS_DEFAULT_RULES.append(("User-agent", user_agent))

if os.environ.get("ROBOTS_DISALLOW_PATHS"):
    disallow_paths = os.environ.get("ROBOTS_DISALLOW_PATHS").split(",")
    for path in disallow_paths:
        ROBOTS_DEFAULT_RULES.append(("Disallow", path.strip()))

if os.environ.get("ROBOTS_ALLOW_PATHS"):
    allow_paths = os.environ.get("ROBOTS_ALLOW_PATHS").split(",")
    for path in allow_paths:
        ROBOTS_DEFAULT_RULES.append(("Allow", path.strip()))

# Пользовательский обработчик для генерации robots.txt
# Можно указать свою функцию для формирования содержимого
ROBOTS_CUSTOM_HANDLER = os.environ.get("ROBOTS_CUSTOM_HANDLER", "")

# ------------------ ИНТЕГРАЦИЯ С БАЗОЙ ДАННЫХ -------------------

# Использовать модель Rule из django-robots для хранения правил в БД
ROBOTS_USE_DATABASE = os.environ.get("ROBOTS_USE_DATABASE", "True") == "True"
