================
Django Ratelimit
================

Django Ratelimit provides a decorator to rate-limit views. Limiting can
be based on IP address or a field in the request--either a GET or POST
variable.

.. image:: https://travis-ci.org/jsocol/django-ratelimit.png?branch=master
   :target: https://travis-ci.org/jsocol/django-ratelimit

:Code:          https://github.com/jsocol/django-ratelimit
:License:       Apache Software License 2.0; see LICENSE file
:Issues:        https://github.com/jsocol/django-ratelimit/issues
:Documentation: http://django-ratelimit.readthedocs.io/

执行命令

::

      pip install -r requirements.txt
      

::
      
      
在 django-ratelimit 的基础上增加了超过频率邮件报警的功能, settings 文件如下


::

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

      EMAIL_RECEIVER = ['**', '**']  # 需要接收邮件的列表

      RATELIMIT_USE_CACHE = 'default'

      RATELIMIT_COUNT_TO_SEND_EMAIL = [2, 50, 100]  # 当计数器到某个值时发邮件，防止邮件发送太频繁

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
      CELERY_RESULT_BACKEND = "redis://%s:%d/2" % (REDIS_HOST, REDIS_PORT)
      REDIS_BROKER = "redis://%s:%d/3" % (REDIS_HOST, REDIS_PORT)
