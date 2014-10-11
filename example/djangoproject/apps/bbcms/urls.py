from django.conf.urls import patterns, include, url


urlpatterns = patterns('bbcms.views',
    url(r'^templates/(?P<path>[\w/]+).html', 'cms_template'),
    url(r'^app/', 'cms'),
)
