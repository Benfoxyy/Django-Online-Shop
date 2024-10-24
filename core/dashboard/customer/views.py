from django.views.generic import TemplateView
from ..permissions import CustomerPermissions

class CustomerDashboard(CustomerPermissions,TemplateView):
    template_name = 'dashboard/customer/home.html'