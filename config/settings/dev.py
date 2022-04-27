"""Development settings for matrevy project."""

from .base import *


###########
# GENERAL #
###########

DEBUG = True

ALLOWED_HOSTS = ['*']

########################
# django-debug-toolbar #
########################

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE

INTERNAL_IPS = ['127.0.0.1']

import socket

_, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += ['.'.join(ip.split('.')[:-1] + ['1']) for ip in ips]
