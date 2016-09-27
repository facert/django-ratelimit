SECRET_KEY = 'ratelimit'

INSTALLED_APPS = (
    'ratelimit',
)


MIDDLEWARE_CLASSES = (
    'ratelimit.middleware.RatelimitMiddleware',
)

# email settings
EMAIL_HOST = '***'
EMAIL_PORT = '***'
EMAIL_USE_SSL = True
EMAIL_HOST_USER = '***'
EMAIL_HOST_PASSWORD = '***'
DEFAULT_FROM_EMAIL = '***'

EMAIL_RECEIVER = ['**', '**']

RATELIMIT_USE_CACHE = 'default'

RATELIMIT_COUNT_TO_SEND_EMAIL = [2, 50, 100]

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


REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379


RATELIMIT_VIEW = 'ratelimit.views.ratelimited'
RATELIMIT_TASK = 'ratelimit.task.send_mail'
RATELIMIT_COUNT_TO_SEND_EMAIL = [2, 50, 100]
CELERY_RESULT_BACKEND = "redis://%s:%d/2" % (REDIS_HOST, REDIS_PORT)
REDIS_BROKER = "redis://%s:%d/3" % (REDIS_HOST, REDIS_PORT)


# silence system check about unset `MIDDLEWARE_CLASSES`
SILENCED_SYSTEM_CHECKS = ['1_7.W001']
