from django.shortcuts import render
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'website/index.html'

class AboutView(generic.TemplateView):
    template_name = 'website/about.html'

class ContactView(generic.TemplateView):
    template_name = 'website/contact.html'