"""Development settings for matrevy project."""

import socket

from .base import *


###########
# GENERAL #
###########

DEBUG = True

ALLOWED_HOSTS = ['*']

########################
# django-debug-toolbar #
########################

INSTALLED_APPS.append("debug_toolbar")

MIDDLEWARE.insert(
    MIDDLEWARE.index("django.middleware.common.CommonMiddleware") + 1,
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)

_, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:ip.rfind(".")] + ".1" for ip in ips] + [
    "127.0.0.1",
    "10.0.2.2",
]

#########################
# django-hosts settings #
#########################

HOST_SCHEME = "http"

PARENT_HOST = "localhost:8000"
