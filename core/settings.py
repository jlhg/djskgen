import os
import sys

from core.utils import EnvHelper

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env_helper = EnvHelper(env_file=os.path.join(BASE_DIR, '.env'))
env_helper.read_env_file()

TEST = 'test' in sys.argv

PRODUCTION = bool(int(os.getenv('PRODUCTION', 0)))
DEBUG = bool(int(os.getenv('DEBUG', 0 if PRODUCTION else 1)))

SECRET_KEY = os.getenv('SECRET_KEY')

# If in production and SECRET_KEY is not set, let it fail
if not SECRET_KEY and PRODUCTION:
    env_helper.set_secret_key()  # pragma: no cover

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
]

LOCAL_APPS = [
    'app',
]

INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS + DJANGO_APPS

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*' if not PRODUCTION else '').split(',')

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'app', 'assets'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'app', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {},
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

GOOGLE_ANALYTICS_ID = os.getenv('GOOGLE_ANALYTICS_ID') if PRODUCTION and not TEST else None
