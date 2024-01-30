"""Production settings for matrevy project."""

from .base import *


###########
# GENERAL #
###########

DEBUG = False

ALLOWED_HOSTS = [
    'matrevy.dk',
    'admin.matrevy.dk',
    'backstage.matrevy.dk',
    'www.matrevy.dk',
]

############
# SECURITY #
############

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

#########################
# django-hosts settings #
#########################

HOST_SCHEME = "https"

PARENT_HOST = "matrevy.dk"
