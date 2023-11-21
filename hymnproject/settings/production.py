from .base import *  # noqa
from .base import env
import dj_database_url
import os

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True


SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
)

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env.bool("DJANGO_DEBUG")
DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() == "true"

# DATABASES = {"default": os.environ.get.db("DATABASE_URL")}
DATABASES["default"] = dj_database_url.parse(os.environ.get("DATABASE_URL"))

# CSRF_TRUSTED_ORIGINS = ["http://localhost:8080","http://localhost:5173",]
DOMAIN = "Devotion"
SITE_NAME = "Devotion"
ALLOWED_HOSTS = ["*"]
