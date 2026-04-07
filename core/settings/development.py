from .base import *

# -------------------------- DEBUG SETTINGS ----------------------------
DEBUG = True
TEMPLATE_DEBUG = True

# ------------------------ PROJECT DIRECTORIES -------------------------
STATIC_DIR = BASE_DIR / "static"
STATICFILES_DIRS = [STATIC_DIR]

# ------------------------- SECURITY SETTINGS --------------------------
# Перенаправление с HTTP на HTTPS
SECURE_SSL_REDIRECT = False

# Установить флаг Secure для CSRF-cookie
CSRF_COOKIE_SECURE = False

# Установить флаг Secure для Session-cookie
SESSION_COOKIE_SECURE = False

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
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL", default="webmaster@localhost")

# Сохранять сессию при каждом запросе — сессия не теряется
SESSION_SAVE_EVERY_REQUEST = True

# Без этого при отсутствии Referer (приватность браузера/расширения) будет 403; защита — по токену в форме
CSRF_REFERER_CHECK_ORIGIN = False
