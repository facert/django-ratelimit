from django.core.exceptions import PermissionDenied


class Ratelimited(PermissionDenied):

    def __init__(self, usage):
        self.usage = usage
        super(Ratelimited, self).__init__()
