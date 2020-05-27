"""Development settings for matrevy project."""
from .base import *


########
# CORE #
########

DEBUG = True

ALLOWED_HOSTS = ['*']

########################
# django-debug-toolbar #
########################

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE

INTERNAL_IPS = ['127.0.0.1']
