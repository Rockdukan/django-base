import environ

env = environ.Env()

DATABASES = {
    "default": env.db(
        "DATABASE_URL",
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
    )
}

# Проверка работоспособности соединений перед использованием (Django 4.2+)
CONN_HEALTH_CHECKS = False

# Роутеры для перенаправления запросов между
# несколькими БД, если необходимо
DATABASE_ROUTERS = []

# Кастомные пути для модулей миграций
MIGRATION_MODULES = {}
