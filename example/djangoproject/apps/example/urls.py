from django.conf.urls import patterns, include, url


urlpatterns = patterns('example.views',
    url(r'^view/(?P<slug>.+)/(?P<pk>\d+)/$', 'content_detail', name='content-detail'),
    url(r'^list/', 'content_list', name='content-list'),
)
