from bearbones.contrib.drf.serializers import BaseContentSerializer
from rest_framework import serializers

from .models import Content, CoolContent, Post, SitePush


class ContentSerializer(BaseContentSerializer):
    class Meta(BaseContentSerializer.Meta):
        model = Content


class CoolContentSerializer(ContentSerializer):
    class Meta(ContentSerializer.Meta):
        model = CoolContent


class PostSerializer(ContentSerializer):
    class Meta(ContentSerializer.Meta):
        model = Post


class SitePushSerializer(serializers.ModelSerializer):
    class Meta:
        model = SitePush
