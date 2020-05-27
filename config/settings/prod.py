"""Production settings for matrevy project."""
from .base import *


########
# CORE #
########

DEBUG = False

ALLOWED_HOSTS = [
    'www.matrevy.dk',
    'matrevy.dk',
] + secrets.get('ALLOWED_HOSTS', [])

############
# SECURITY #
############

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True
