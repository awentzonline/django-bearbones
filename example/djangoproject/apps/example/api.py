from bearbones.contrib.drf.views import BaseContentViewSet
from rest_framework import routers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Content, CoolContent, SitePush
from .serializers import (
    ContentSerializer, CoolContentSerializer, SitePushSerializer
)


class ContentViewSet(BaseContentViewSet):
    model = Content
    serializer_class = None
    serializer_map = (
        (CoolContent, CoolContentSerializer),
        (Content, ContentSerializer),
    )
    paginate_by = 10


# class SitePushView(APIView):
#     def get(self, request): 
#         serializer = SitePushSerializer(data=SitePush.objects.all())
#         return Response(serializer.data)

#     def post(self, request):
#         sitepush = SitePush.objects.create()
#         # TODO: enqueue task
#         serializer = SitePushSerializer(data=sitepush)
#         return Response(serializer.data)

class SitePushView(viewsets.ReadOnlyModelViewSet):
    model = SitePush


api_v1_router = routers.DefaultRouter()
api_v1_router.register('content', ContentViewSet)
api_v1_router.register('sitepush', SitePushView)
