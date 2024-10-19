from django.views.generic import TemplateView

class CustomerDashboard(TemplateView):
    template_name = 'dashboard/customer.html'