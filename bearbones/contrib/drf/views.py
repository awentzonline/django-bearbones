from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.utils import timezone
from rest_framework import decorators, filters, status, viewsets, routers

from bearbones.models import BaseContent
from .serializers import BaseContentSerializer


class BaseContentViewSet(viewsets.ModelViewSet):
    model = BaseContent
    # serializer_map = (
    #     (BaseContent, BaseContentSerializer),
    # )
    # serializer_class = BaseContentSerializer

    def get_serializer_class(self):
        klass = None

        if hasattr(self, 'object'):
            klass = self.object.__class__
        elif 'ctype' in self.request.REQUEST:
            natural_key = self.request.REQUEST['ctype'].split('_')
            content_type = ContentType.objects.get_by_natural_key(*natural_key)
            klass = content_type.model_class()
            if not issubclass(klass, self.model):
                raise Http404('Content type not found.')
        if klass:
            # find the first, best matching serializer
            for serializer_target, serializer_class in self.serializer_map:
                if issubclass(klass, serializer_target):
                    return serializer_class
        return super(BaseContentViewSet, self).get_serializer_class()

    @decorators.action()
    def publish(self):
        self.object.time_published = timezone.now()
        return Response(dict(detail="Published"))
