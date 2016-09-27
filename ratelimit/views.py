from importlib import import_module

from django.conf import settings
from django.http import HttpResponseForbidden


def ratelimited(request, exception):
    usage = exception.usage
    if usage:
        task_view = settings.RATELIMIT_TASK
        if task_view:
            mod, attr = task_view.rsplit('.', 1)
            keyfn = getattr(import_module(mod), attr)
            keyfn.delay(usage)
    return HttpResponseForbidden()
