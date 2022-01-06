from .base import *

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = [config('ALLOWED_HOST_1'), config('ALLOWED_HOST_2')]
SECRET_KEY = config('SECRET_KEY')

try:
    from .local import *
except ImportError:
    pass
