import os
from sys import path

from django.core.wsgi import get_wsgi_application

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path.append(SITE_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.production")

application = get_wsgi_application()
