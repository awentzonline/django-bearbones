from django.conf.urls import patterns, include, url

from example.api import api_v1_router


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cms/api/v1/', include(api_v1_router.urls)),
    url(r'^$', 'example.views.home_page', name='home'),
    url(r'^', include('example.urls')),
    url(r'^cms/', include('bbcms.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
