import environ

env = environ.Env()

DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "HOST": env("DB_MSSQL_HOST", default="localhost"),
        "PORT": env("DB_MSSQL_PORT", default="5432"),
        "NAME": env("DB_MSSQL_NAME", default=""),
        "USER": env("DB_MSSQL_USER", default=""),
        "PASSWORD": env("DB_MSSQL_PASSWORD", default=""),
        "OPTIONS": {
            "driver": "ODBC Driver 17 for SQL Server",
        },
    },
}

# set this to False if you want to turn off pyodbc"s connection pooling
DATABASE_CONNECTION_POOLING = False
