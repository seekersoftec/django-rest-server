from .basic import *

env = environ.Env()
environ.Env.read_env()  # the .env file should be in the settings path, not the manage.py path

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS.extend(env('ALLOWED_HOSTS').split(','))

INSTALLED_APPS.extend(
    [
        'storages',
    ]
)

DATABASES = {
    'default': env.db(),  # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'sentry': {
            'level': env('LOGGING_LEVEL'),  # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': env('LOGGING_LEVEL', default='INFO'),
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': env('MAIL_ADMINS_LOGGING_LEVEL', default='ERROR'),
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'sentry'],
            'propagate': True,
        },
        'django.db.backends': {
            'level': env('LOGGING_LEVEL'),
            'handlers': ['console', 'sentry'],
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins', 'sentry'],
            'level': env('LOGGING_LEVEL', default='WARNING'),
            'propagate': False,
        },
        'raven': {
            'level': env('LOGGING_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': env('LOGGING_LEVEL'),
            'handlers': ['console'],
            'propagate': False,
        },
    }
}

CACHES = {
    'default': env.cache(),
    'redis': env.cache('REDIS_URL')
}
