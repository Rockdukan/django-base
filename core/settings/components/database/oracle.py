import environ

env = environ.Env()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.oracle",
        "HOST": env("DB_ORACLE_HOST", default="localhost"),
        "PORT": env("DB_ORACLE_PORT", default="5432"),
        "NAME": env("DB_ORACLE_NAME", default=""),
        "USER": env("DB_ORACLE_USER", default=""),
        "PASSWORD": env("DB_ORACLE_PASSWORD", default=""),
    }
}
