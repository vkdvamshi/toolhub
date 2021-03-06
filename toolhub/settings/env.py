from environ import Env

from .base import *  # noqa: F401, F403

env = Env()


SECRET_KEY = env.str('SECRET_KEY', default='keepitsecret')
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])
DATABASES = {
    'default': env.db(default='sqlite:///db.sqlite'),
}
TIME_ZONE = env.str('TIME_ZONE', default='UTC')
LANGUAGE_CODE = env.str('LANGUAGE_CODE', default='en-us')

STATIC_ROOT = env.str('STATIC_ROOT', default=f'{BASE_DIR}static/')
STATIC_URL = env.str('STATIC_URL', default='/static/')
MEDIA_ROOT = env.str('MEDIA_ROOT', default=f'{BASE_DIR}media/')
MEDIA_URL = env.str('MEDIA_URL', default='/media/')
