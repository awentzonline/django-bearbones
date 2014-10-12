from bearbones.models import BaseContent, BaseTag
from django.core.urlresolvers import reverse
from django.db import models
from jsonfield import JSONField


class Tag(BaseTag):
    pass


class Content(BaseContent):
    description = models.TextField(default='', blank=True)

    class Meta:
        ordering = ('-time_created',)

    def get_absolute_url(self):
        return reverse('content-detail', kwargs=dict(
            pk=self.pk,
            slug=self.slug
        ))


class CoolContent(Content):
    cool = models.BooleanField(default=True)


class Post(Content):
    chunks = JSONField(default=[], blank=True)


class SitePush(models.Model):
    time_started = models.DateTimeField(auto_now_add=True, db_index=True)
    time_completed = models.DateTimeField(blank=True, null=True, db_index=True)
