from django.core import serializers
from django.test import TestCase

from example.models import Content, CoolContent, Tag


class ContentTestCase(TestCase):
    def setUp(self):
        self.content = CoolContent.objects.create(
            title="This is cool", cool=True
        )

    def test_serialize_content(self):
        data = serializers.serialize('json', [self.content])
        print data
