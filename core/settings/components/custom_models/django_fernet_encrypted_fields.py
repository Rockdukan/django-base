import environ

env = environ.Env()


SALT_KEY = env.str("SALT_KEY")
