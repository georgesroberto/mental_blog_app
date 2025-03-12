"""
Development settings
"""

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-jejrx$ycg72sg*$m&ldql!2j30%)92jkyx^8eqh%$d+rsa3uep"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIRS = [ BASE_DIR / "assets" ]