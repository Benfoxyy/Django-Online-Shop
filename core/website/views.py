from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'website/index.html'

class AboutView(TemplateView):
    template_name = 'website/about.html'

class ContactView(TemplateView):
    template_name = 'website/contact.html'