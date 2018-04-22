import os

from core.helpers import DotEnvReader, generate_secret_key

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DotEnvReader(os.path.join(PROJECT_ROOT, '.env')).read()

PRODUCTION = bool(int(os.getenv('PRODUCTION', 0)))
DEBUG = bool(int(os.getenv('DEBUG', 0 if PRODUCTION else 1)))

SECRET_KEY = os.getenv('SECRET_KEY')

# If in production and SECRET_KEY is not set, let it fail
if not SECRET_KEY and PRODUCTION:
    with open('.env', 'wb') as env:
        env.write(('SECRET_KEY=' + generate_secret_key()).encode())

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

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
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
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
