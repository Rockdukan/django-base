import os
from pathlib import Path

import environ
from django.contrib.staticfiles.storage import ManifestStaticFilesStorage

from core.settings.dashboard import LUCUS_DASHBOARD

# ------------------------ PROJECT DIRECTORIES -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent
LOGS_DIR = BASE_DIR / "logs"
MEDIA_ROOT = BASE_DIR / "media"

# ------------------------------ ENVIRON -------------------------------
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# ------------------------- SECURITY SETTINGS --------------------------
ALLOWED_HOSTS = ["127.0.0.1", "localhost"] + env.list("ALLOWED_HOSTS", default=[])

# --------------------------- SITE SETTINGS ----------------------------
SITE_ID = 1

# -------------------------- WSGI SETTINGS -----------------------------
WSGI_APPLICATION = "core.wsgi.application"

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
