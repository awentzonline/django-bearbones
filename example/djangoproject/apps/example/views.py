from django.utils import timezone
from django.views.generic import DetailView, ListView, TemplateView

from .models import Content


class IsPublishedMixin(object):
    published = None

    def get_queryset(self, **kwargs):
        qs = super(IsPublishedMixin, self).get_queryset(**kwargs)
        if not self.published is None:
            if self.published:
                qs = qs.filter(time_published__lte=timezone.now())
            else:
                qs = qs.filter(time_published__null=True)
        return qs


class ContentDetailView(IsPublishedMixin, DetailView):
    model = Content
    context_object_name = 'content'


class ContentListView(IsPublishedMixin, ListView):
    model = Content
    paginate_by = 20
    published = True


class HomePage(TemplateView):
    template_name = 'example/home.html'


content_detail = ContentDetailView.as_view()
content_list = ContentListView.as_view()
home_page = HomePage.as_view()
