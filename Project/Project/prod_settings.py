import dj_database_url
from .settings import *

DEBUG = False

SECRET_KEY = '4(3aipi5unhc53c53si#_d8@*!f%gsr0l6ri6$+=xi@a=+5@b='

ALLOWED_HOSTS = ['nathanetloic.herokuapp.com']

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

INSTALLED_APPS = [
    'HoneyPot',
    'users.apps.UsersConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATABASES['default'] = dj_database_url.config()
