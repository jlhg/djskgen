from os import path as os_path
from sys import path

DJANGO_ROOT = os_path.dirname(os_path.dirname(os_path.abspath(__file__)))

SITE_ROOT = os_path.dirname(DJANGO_ROOT)

SITE_NAME = os_path.basename(DJANGO_ROOT)

DEBUG = False
TEMPLATE_DEBUG = DEBUG
path.append(DJANGO_ROOT)

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'Asia/Taipei'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os_path.normpath(os_path.join(SITE_ROOT, 'media'))
MEDIA_URL = '/media/'
STATIC_ROOT = 'static'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os_path.normpath(os_path.join(SITE_ROOT, 'static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = r"kc_24q58sez2!wqf_@=t)cc&ettfs&=jn8st@y9m_v0&n#+qku"

FIXTURE_DIRS = (
    os_path.normpath(os_path.join(SITE_ROOT, 'fixtures')),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = '%s.urls' % SITE_NAME

WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    os_path.normpath(os_path.join(SITE_ROOT, 'templates')),
)

INSTALLED_APPS = (
    'django.contrib.staticfiles',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
