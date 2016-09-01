from .base import *     # noqa
import dj_database_url

DEBUG = get_env_var('DJANGO_DEBUG', False)

SECRET_KEY = get_env_var('DJANGO_SECRET_KEY')

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['macdown.uranusjr.com', 'macdown.herokuapp.com']

STATIC_ROOT = 'static'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_REQUIRED_PATH_PATTERN = r'/admin/'
