from .base import *  # noqa
from .base import env


DATABASES = {"default": env.db("DATABASE_URL")}
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="oXPWQPA3C3sdBCuBeXUKq3LBp9YDJ33-306p9EAKf1ja1xkWnKY",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# CSRF_TRUSTED_ORIGINS = ["http://localhost:8080","http://localhost:5173",]
DOMAIN = "Devotion"
SITE_NAME = "Devotion"
ALLOWED_HOSTS = ['*']