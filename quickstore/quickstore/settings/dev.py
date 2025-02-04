from .base import *

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "quickstore",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
