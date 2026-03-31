from split_settings.tools import include

from .base import *

# -------------------------- DEBUG SETTINGS ----------------------------
DEBUG = False
TEMPLATE_DEBUG = False

# ------------------------ PROJECT DIRECTORIES -------------------------
STATIC_ROOT = BASE_DIR / "static"

# ------------------------- SECURITY SETTINGS --------------------------
# Перенаправление с HTTP на HTTPS
SECURE_SSL_REDIRECT = True

# Установить флаг Secure для CSRF-cookie
CSRF_COOKIE_SECURE = True

# Установить флаг Secure для Session-cookie
SESSION_COOKIE_SECURE = True

# Разрешить запросы со всех доменов
CORS_ALLOW_ALL_ORIGINS = False

# Разрешить передачу учетных данных (cookies, HTTP-аутентификация)
CORS_ALLOW_CREDENTIALS = True

# -------------------------- CACHE SETTINGS ----------------------------
# CACHE_URL=redis://localhost:6379/1

# -------------------------- EMAIL SETTINGS ----------------------------
# Выбор бэкенда для отправки email
# Поддерживаемые значения:
# "django.core.mail.backends.smtp.EmailBackend" - отправка через SMTP
# "django.core.mail.backends.console.EmailBackend" - вывод в консоль
# "django.core.mail.backends.filebased.EmailBackend" - запись в файлы
# "django.core.mail.backends.locmem.EmailBackend" - хранение в памяти
# "django.core.mail.backends.dummy.EmailBackend" - подавление отправки
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# ------------------------ MIDDLEWARE SETTINGS -------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "core.middlewares.healthcheck.HealthcheckMiddleware",
    "core.middlewares.request_id.RequestIdMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "core.middlewares.admin_language.AdminLanguageMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "core.middlewares.AddContentTypeOptionsMiddleware",
    "core.middlewares.ReferrerPolicyMiddleware",
    "core.middlewares.PermissionsPolicyMiddleware",
    "core.middlewares.request_log_middleware.RequestLogMiddleware",
]

# ------------------------- TEMPLATE SETTINGS --------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "apps" / "common" / "templates", "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # ------------------ DJANGO -------------------
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
                "django.template.context_processors.debug",
                # ------------------ OTHER --------------------
                "core.context_processors.current_date_info",
            ],
        },
    },
]

# -------------------------- INSTALLED APPS ----------------------------
INSTALLED_APPS = [
    # ---------------- ADMIN ------------------
    "lucus",
    # ------------------ DJANGO -------------------
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "solo",
    # ----------------- PROJECT -------------------
    "apps.index",
]

# ------------------------ ADDITIONAL SETTINGS -------------------------
include(
    "components/api/rest_framework.py",
    "components/admin_tools/auditlog.py",
    "components/admin_tools/log_viewer.py",
    "components/admin_tools/constance.py",
    "components/tasks/django_celery_beat.py",
    "components/tasks/django_celery_results.py",
    "components/database/sqlite.py",
    "components/file_managers/filer.py",
    "components/security/base.py",
    "components/security/content_security.py",
    "components/security/cors.py",
    "components/security/csrf.py",
    "components/security/orm_security.py",
    "components/security/session.py",
    "components/security/throttling.py",
    "components/performance/caches.py",
    "components/performance/compression.py",
    "components/internationalization/base.py",
    "components/internationalization/modeltranslation.py",
)

SESSION_SAVE_EVERY_REQUEST = True
CSRF_REFERER_CHECK_ORIGIN = False
# На сервере в .env обязательно: CSRF_TRUSTED_ORIGINS=https://домен.ru,https://www.домен.ru
