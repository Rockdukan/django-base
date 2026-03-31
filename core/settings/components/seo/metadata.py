import os

"""
Настройки метаданных SEO для Django

Компонент отвечает за:
1. Настройку мета-тегов для SEO
2. Конфигурацию Open Graph и Twitter Cards
3. Настройку Schema.org микроразметки
4. Управление заголовками и описаниями страниц
"""

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ META -------------------

# Название сайта (для SEO-заголовков)
SITE_NAME = os.environ.get("SITE_NAME", "Мой сайт")

# Домен сайта (для канонических URL)
SITE_DOMAIN = os.environ.get("SITE_DOMAIN", "example.com")

# Базовый протокол (http или https)
SITE_PROTOCOL = os.environ.get("SITE_PROTOCOL", "https")

# ------------------ НАСТРОЙКИ ДЛЯ DJANGO-META -------------------

# Включить django-meta для управления метаданными
META_ENABLED = os.environ.get("META_ENABLED", "True") == "True"

# Настройки для django-meta
META_SITE_PROTOCOL = SITE_PROTOCOL
META_SITE_DOMAIN = SITE_DOMAIN
META_SITE_NAME = SITE_NAME
META_INCLUDE_KEYWORDS = os.environ.get("META_INCLUDE_KEYWORDS", "True") == "True"
META_DEFAULT_KEYWORDS = (
    os.environ.get("META_DEFAULT_KEYWORDS", "").split(",") if os.environ.get("META_DEFAULT_KEYWORDS") else []
)
META_DESCRIPTION_LENGTH = int(os.environ.get("META_DESCRIPTION_LENGTH", "160"))
META_TITLE_LENGTH = int(os.environ.get("META_TITLE_LENGTH", "70"))

# ------------------ НАСТРОЙКИ ДЛЯ OPEN GRAPH -------------------

# Включить Open Graph мета-теги
META_USE_OG_PROPERTIES = os.environ.get("META_USE_OG_PROPERTIES", "True") == "True"

# Тип сайта для Open Graph
META_OG_TYPE = os.environ.get("META_OG_TYPE", "website")

# Локаль для Open Graph
META_OG_LOCALE = os.environ.get("META_OG_LOCALE", "ru_RU")

# URL изображения по умолчанию для Open Graph
META_OG_IMAGE = os.environ.get("META_OG_IMAGE", "")

# ------------------ НАСТРОЙКИ ДЛЯ TWITTER CARDS -------------------

# Включить Twitter Cards мета-теги
META_USE_TWITTER_PROPERTIES = os.environ.get("META_USE_TWITTER_PROPERTIES", "True") == "True"

# Тип карточки для Twitter
META_TWITTER_TYPE = os.environ.get("META_TWITTER_TYPE", "summary_large_image")

# Имя сайта в Twitter
META_TWITTER_SITE = os.environ.get("META_TWITTER_SITE", "")

# Имя автора в Twitter
META_TWITTER_AUTHOR = os.environ.get("META_TWITTER_AUTHOR", "")

# ------------------ НАСТРОЙКИ ДЛЯ SCHEMA.ORG -------------------

# Включить микроразметку Schema.org
META_USE_SCHEMAORG = os.environ.get("META_USE_SCHEMAORG", "True") == "True"

# Тип сущности Schema.org по умолчанию
META_SCHEMAORG_TYPE = os.environ.get("META_SCHEMAORG_TYPE", "Organization")

# Имя организации для Schema.org
META_SCHEMAORG_NAME = os.environ.get("META_SCHEMAORG_NAME", SITE_NAME)

# Дополнительные атрибуты Schema.org
META_SCHEMAORG_LOGO = os.environ.get("META_SCHEMAORG_LOGO", "")
META_SCHEMAORG_PHONE = os.environ.get("META_SCHEMAORG_PHONE", "")
META_SCHEMAORG_EMAIL = os.environ.get("META_SCHEMAORG_EMAIL", "")

# ------------------ НАСТРОЙКИ ДЛЯ CANONICAL URL -------------------

# Включить канонические URL
META_USE_CANONICAL_URL = os.environ.get("META_USE_CANONICAL_URL", "True") == "True"

# Принудительно использовать HTTPS для канонических URL
META_CANONICAL_FORCE_HTTPS = os.environ.get("META_CANONICAL_FORCE_HTTPS", "True") == "True"

# ------------------ НАСТРОЙКИ ДЛЯ РОБОТОВ -------------------

# Значение мета-тега robots по умолчанию
META_DEFAULT_ROBOTS = os.environ.get("META_DEFAULT_ROBOTS", "index, follow")

# ------------------ ИНТЕГРАЦИЯ С DJANGO -------------------

# Настройки для интеграции с Django
META_USE_SITES = os.environ.get("META_USE_SITES", "True") == "True"

# ------------------ НАСТРОЙКИ ДЛЯ ПРИЛОЖЕНИЙ DJANGO -------------------

# Включить meta приложение в INSTALLED_APPS
INSTALLED_APPS_META = ["meta"]
