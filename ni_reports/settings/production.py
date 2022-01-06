from .base import *

DEBUG = False
ALLOWED_HOSTS = [config('ALLOWED_HOST_1'), config('ALLOWED_HOST_2')]

try:
    from .local import *
except ImportError:
    pass
