import os

from core.helpers import DotEnvReader, set_secret_key_env

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOT_ENV_PATH = os.path.join(PROJECT_ROOT, '.env')

DotEnvReader(DOT_ENV_PATH).read()

PRODUCTION = bool(int(os.getenv('PRODUCTION', 0)))
DEBUG = bool(int(os.getenv('DEBUG', 0 if PRODUCTION else 1)))

SECRET_KEY = os.getenv('SECRET_KEY')

# If in production and SECRET_KEY is not set, let it fail
if not SECRET_KEY and PRODUCTION:
    set_secret_key_env(DOT_ENV_PATH)

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'app',
]

INSTALLED_APPS = LOCAL_APPS + DJANGO_APPS

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*' if not PRODUCTION else '').split(',')

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'assets'),
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
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
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
