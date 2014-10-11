from django.views.generic import DetailView, ListView, TemplateView

from .models import Content


class ContentDetailView(DetailView):
    model = Content
    context_object_name = 'content'


class ContentListView(ListView):
    model = Content
    paginate_by = 20


class HomePage(TemplateView):
    template_name = 'example/home.html'


content_detail = ContentDetailView.as_view()
content_list = ContentListView.as_view()
home_page = HomePage.as_view()
