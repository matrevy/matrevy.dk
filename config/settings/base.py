"""Base settings for matrevy project."""

from pathlib import Path

import environ

_ = gettext = lambda s: s


BASE_DIR = Path(__file__).resolve().parents[2]

env = environ.Env()

###########
# GENERAL #
###########

SECRET_KEY = env('DJANGO_SECRET_KEY')

SITE_ID = 1

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'matrevy.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_NAME'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

############
# SECURITY #
############

SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_HTTPONLY = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = 'DENY'

#################
# GLOBALIZATION #
#################

LANGUAGE_CODE = 'da'

LANGUAGES = [
    ('da', _('Dansk')),
    ('en', _('Engelsk')),
    ('nb', _('Norsk')),
]

LANGUAGES_BIDI = []

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

TIME_ZONE = 'Europe/Copenhagen'

USE_I18N = True

USE_L10N = True

USE_TZ = True

####################
# STATIC AND MEDIA #
####################

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'

#########
# EMAIL #
#########

ADMINS = env.list('ADMINS', default=[])

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'noreply@matrevy.dk'

SERVER_EMAIL = 'root@matrevy.dk'

EMAIL_SUBJECT_PREFIX = '[Matematikrevy] '

EMAIL_BACKEND = env(
    'EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend'
)

EMAIL_HOST = env('EMAIL_HOST', default='localhost')

EMAIL_PORT = env.int('EMAIL_PORT', default=25)

EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='')

EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')

EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=False)

###########
# LOGGING #
###########

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(name)s: (%(levelname)s) %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'fmt': '[%(asctime)s] %(name)s: (%(levelname)s) %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'verbose',
            'filters': ['require_debug_true'],
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'verbose',
            'filters': ['require_debug_false'],
            'filename': BASE_DIR / 'logs' / 'error.log',
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 5,
        },
        'django.server': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'django.server',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'matrevy': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
