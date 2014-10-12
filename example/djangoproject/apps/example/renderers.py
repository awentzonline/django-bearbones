from bearbones.contrib.medusa.renderers import (
        BaseContentDetailRenderer, SettingsPathRenderer)
from django.core.urlresolvers import reverse

from example.models import Content, SitePush


class HomeRenderer(SettingsPathRenderer):
    extra_paths = [
        reverse('content-list')
    ]

   
class ContentDetailRenderer(BaseContentDetailRenderer):
    model = Content

    def get_time_last_update(self):
        try:
            last_push = SitePush.objects.filter(time_completed__isnull=False).order_by('-time_completed').first()
        except SitePush.DoesNotExist:
            last_push = None
        if last_push:
            return last_push.time_completed
        return None



renderers = [HomeRenderer, ContentDetailRenderer]
