# -*- coding: utf-8 -*-
# from __future__ import absolute_import
import os
import json
import django
from celery import Celery

from django.conf import settings
from django.core import mail


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sebug.settings')
django.setup()

app = Celery('sync', backend=settings.CELERY_RESULT_BACKEND, broker=settings.REDIS_BROKER)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task()
def send_mail(usage):
    emails = ['seebug block spider', json.dumps(usage), settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVER]
    if usage['count'] in settings.RATELIMIT_COUNT_TO_SEND_EMAIL:
        mail.send_mail(*emails)


if __name__ == '__main__':
    app.start()
