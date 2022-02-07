from .base import *

DEBUG = False

SECRET_KEY = 'django-insecure-uev7)lwr8nz3(5o(gu75&=mq4kru9x!grv0s7y3-4(hnlh5&s('

try:
    from .local import *
except ImportError:
    pass
