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

EMAIL_HOST = env.str("EMAIL_HOST", default="localhost")
EMAIL_PORT = env.int("EMAIL_PORT", default=25)
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=False)
EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL", default=False)
DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL", default="webmaster@localhost")

SESSION_SAVE_EVERY_REQUEST = True
CSRF_REFERER_CHECK_ORIGIN = False
# На сервере в .env обязательно: CSRF_TRUSTED_ORIGINS=https://домен.ru,https://www.домен.ru
