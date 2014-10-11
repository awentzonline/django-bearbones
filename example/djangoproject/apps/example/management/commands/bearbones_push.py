from django.core import management
from django.core.management.base import BaseCommand
from django.utils import timezone
from django_medusa.renderers import StaticSiteRenderer
from django_medusa.utils import get_static_renderers

from example.models import SitePush


class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
        sitepush = SitePush.objects.create()
        management.call_command(
            'collectstatic',
            interactive=False,
            ignore_patterns=['admin', '*.less', 'rest_framework', 'node_modules']
        )
        management.call_command('staticsitegen')
        sitepush.time_completed = timezone.now()
        sitepush.save()
