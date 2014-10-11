from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from bearbones.models import BaseContent


class ContentTypeField(serializers.WritableField):
    """Converts between natural key for native use and integer for non-native."""
    def to_native(self, value):
        """Convert to natural key."""
        content_type = ContentType.objects.get_for_id(value)
        return '_'.join(content_type.natural_key())

    def from_native(self, value):
        """Convert to integer id."""
        natural_key = value.split('_')
        content_type = ContentType.objects.get_by_natural_key(*natural_key)
        return content_type.id


class BaseContentSerializer(serializers.ModelSerializer):
    ctype = ContentTypeField(source='polymorphic_ctype_id', read_only=True)
    absolute_url = serializers.Field(source='get_absolute_url')

    class Meta:
        model = BaseContent  # override this
        exclude = ('polymorphic_ctype',)
