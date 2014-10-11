from django.views.generic import TemplateView


class CmsTemplateView(TemplateView):
    def get_template_names(self):
        return u'cms/{}.html'.format(self.kwargs.get('path'))


cms = TemplateView.as_view(template_name='cms/cms_base.html')
cms_template = CmsTemplateView.as_view()
