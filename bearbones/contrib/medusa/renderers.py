from django.conf import settings
from django.utils import timezone
from django_medusa.renderers import StaticSiteRenderer

from bearbones.models import BaseContent


class SettingsPathRenderer(StaticSiteRenderer):
    settings_attr = 'MEDUSA_RENDER_PATHS'
    extra_paths = []

    def get_paths(self):
        paths = set(
            getattr(settings, self.settings_attr, [])
        ) | set(self.extra_paths)
        return paths


class BaseContentDetailRenderer(StaticSiteRenderer):
    model = BaseContent
    
    def get_paths(self):
        self.time_last_update = self.get_time_last_update()
        qs = self.get_queryset()
        paths = set(self.make_content_url(c) for c in qs)
        return paths

    def make_content_url(self, c):
        return c.get_absolute_url()

    def get_queryset(self):
        """Defaults to updated things which have been published."""
        qs = self.model.objects.filter(time_published__lte=timezone.now())
        time_last_update = getattr(self, 'time_last_update', None)
        if time_last_update:
            qs = qs.filter(time_updated__gt=time_last_update)
        return qs

    def get_time_last_update(self):
        return None
