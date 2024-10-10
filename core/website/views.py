from django.shortcuts import render
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'website/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["cart"] = self.request.session.get('cart')
    #     return context
    

class AboutView(generic.TemplateView):
    template_name = 'website/about.html'

class ContactView(generic.TemplateView):
    template_name = 'website/contact.html'