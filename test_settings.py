SECRET_KEY = 'ratelimit'

INSTALLED_APPS = (
    'ratelimit',
)

RATELIMIT_USE_CACHE = 'default'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'ratelimit-tests',
    },
    'connection-errors': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'test-connection-errors',
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    },
}

RATELIMIT_VIEW = 'ratelimit.exception.CustomRatelimited'


EMAIL_BACKEND = 'ratelimit.celery_email.backends.CeleryEmailBackend'


CELERY_EMAIL_TASK_CONFIG = {
    'queue': 'email',
    'rate_limit': '50/m',  # * CELERY_EMAIL_CHUNK_SIZE (default: 10)
}

# silence system check about unset `MIDDLEWARE_CLASSES`
SILENCED_SYSTEM_CHECKS = ['1_7.W001']
