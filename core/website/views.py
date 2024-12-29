from django.views.generic import TemplateView,CreateView
from django.contrib.messages.views import SuccessMessageMixin
from dashboard.models import TicketModel

class IndexView(TemplateView):
    template_name = 'website/index.html'

class AboutView(TemplateView):
    template_name = 'website/about.html'

class ContactView(CreateView,SuccessMessageMixin):
    template_name = 'website/contact.html'
    model = TicketModel
    fields = '__all__'
    success_url = '/contact/'
    success_message = 'تیکت شما با موفقیت ارسال شد'