import os

from django.conf import settings
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()


if not settings.TEST:  # pragma: no cover
    call_command('collectstatic', interactive=False)
