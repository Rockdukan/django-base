import environ

env = environ.Env()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": env("DB_MYSQL_HOST", default="localhost"),
        "PORT": env("DB_MYSQL_PORT", default="3306"),
        "NAME": env("DB_MYSQL_NAME", default=""),
        "USER": env("DB_MYSQL_USER", default=""),
        "PASSWORD": env("DB_MYSQL_PASSWORD", default=""),
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        "CONN_MAX_AGE": 60 * 10,  # 10 minutes
    }
}
