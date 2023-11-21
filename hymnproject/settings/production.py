from .base import *  # noqa
from .base import env
import dj_database_url
import os

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True


SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG")

database_url = os.environ.get(
    "DATABASE_URL"
)

DATABASES["default"] = dj_database_url.parse(database_url)

# CSRF_TRUSTED_ORIGINS = ["http://localhost:8080","http://localhost:5173",]
DOMAIN = "Devotion"
SITE_NAME = "Devotion"
ALLOWED_HOSTS = ["*"]
