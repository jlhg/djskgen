from django.core.management import call_command
from django.core.management.commands import runserver


class Command(runserver.Command):
    def handle(self, *args, **options):
        call_command('collectstatic', interactive=False)

        return super().handle(*args, **options)
