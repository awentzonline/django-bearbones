from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from polymorphic import PolymorphicModel


class BaseContent(PolymorphicModel):
    time_created = models.DateTimeField(auto_now_add=True, db_index=True)
    time_updated = models.DateTimeField(auto_now=True, db_index=True)
    time_published = models.DateTimeField(blank=True, null=True, db_index=True)

    title = models.TextField()
    slug = models.TextField(blank=True, default='')

    class Meta(PolymorphicModel.Meta):
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(BaseContent, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('bearbones:content-detail', kwargs=dict(
            pk=self.pk,
            slug=self.slug
        ))


class BaseTag(PolymorphicModel):
    label = models.CharField(max_length=255, blank=False, null=False)
    slug = models.CharField(max_length=255)

    class Meta(PolymorphicModel.Meta):
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.label)
        return super(BaseTag, self).save(*args, **kwargs)
