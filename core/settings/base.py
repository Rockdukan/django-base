import os
from pathlib import Path

import environ
from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
from split_settings.tools import include


# ------------------------ PROJECT DIRECTORIES -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent
LOGS_DIR = BASE_DIR / "logs"
MEDIA_ROOT = BASE_DIR / "media"

# ------------------------------ ENVIRON -------------------------------
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# -------------------------- DEBUG SETTINGS ----------------------------
DEBUG = env.bool("DEBUG", default=False)
TEMPLATE_DEBUG = env.bool("TEMPLATE_DEBUG", default=DEBUG)

# ------------------------ CORE SECURITY SETTINGS ----------------------
# В production обязательно задайте SECRET_KEY в окружении.
SECRET_KEY = env.str("SECRET_KEY", default="django-insecure-change-me")

# ------------------------- SECURITY SETTINGS --------------------------
ALLOWED_HOSTS = ["127.0.0.1", "localhost"] + env.list("ALLOWED_HOSTS", default=[])

# --------------------------- SITE SETTINGS ----------------------------
SITE_ID = 1

# -------------------------- WSGI SETTINGS -----------------------------
WSGI_APPLICATION = "core.wsgi.application"

# -------------------------- ASGI SETTINGS -----------------------------
ASGI_APPLICATION = "core.asgi.application"

# -------------------------- URL SETTINGS ------------------------------
ADMIN_MEDIA_PREFIX = "/media/cabinet/"
MEDIA_URL = "/media/"
ROOT_URLCONF = "core.urls"
STATIC_URL = "/static/"

# --------------------------- AUTH SETTINGS ----------------------------
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

# -------------------------- MODELS SETTINGS ---------------------------
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# ---------------------------- STATICFILES -----------------------------
# Механизмы для поиска статических файлов
STATICFILES_FINDERS = (
    # Поиск в директориях, указанных в STATICFILES_DIRS
    "django.contrib.staticfiles.finders.FileSystemFinder",
    # Поиск в поддиректории static каждого приложения
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# Класс хранилища для статических файлов
# ManifestStaticFilesStorage добавляет хэш к именам
# файлов для инвалидации кэша
STATICFILES_STORAGE = ManifestStaticFilesStorage

USE_DJANGO_JQUERY = True

# ------------------------ MIDDLEWARE SETTINGS -------------------------
MIDDLEWARE = [
    # ------------------ DJANGO -------------------
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    # ----------------- PROJECT -------------------
    "core.middlewares.healthcheck.HealthcheckMiddleware",
    "core.middlewares.request_id.RequestIdMiddleware",
    "core.middlewares.admin_language.AdminLanguageMiddleware",
    "core.middlewares.AddContentTypeOptionsMiddleware",
    "core.middlewares.ReferrerPolicyMiddleware",
    "core.middlewares.PermissionsPolicyMiddleware",
    "core.middlewares.request_log_middleware.RequestLogMiddleware",
]

# ------------------------- TEMPLATE SETTINGS --------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates", BASE_DIR / "apps" / "common" / "templates"],
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
    # ------------------ ADMIN --------------------
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
    # ------------------ OTHER --------------------
    "auditlog",
    "constance",
    "constance.backends.database",
    "log_viewer",
    "solo",
    # ----------------- PROJECT -------------------
    "apps.index",
]

# ------------------------ ADDITIONAL SETTINGS -------------------------
include(
    "components/database/sqlite.py",
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
    "components/admin_tools/auditlog.py",
    "components/admin_tools/log_viewer.py",
    "components/admin_tools/constance.py",
    "components/custom_admin/lucus.py",
    "components/tasks/django_celery_beat.py",
    "components/tasks/django_celery_results.py",
    "components/file_managers/filer.py",
)
