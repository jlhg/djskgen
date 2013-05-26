from os.path import join, normpath
from defaults import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': normpath(join(DJANGO_ROOT, 'default.db')),  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Modify it for any changes on apps, this variable is for Django template loader.
# https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.app_directories.Loader
INSTALLED_APPS += ('example_app',)
