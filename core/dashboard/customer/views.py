from django.views.generic import TemplateView,ListView,CreateView,UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from ..permissions import CustomerPermissions
from .forms import AddAddressesForm
from order.models import AddressModel

class CustomerDashboard(CustomerPermissions,TemplateView):
    template_name = 'dashboard/customer/home.html'

class AddressesView(CustomerPermissions,ListView):
    template_name = 'dashboard/customer/orders/addresses.html'
    context_object_name = 'addresses'
    
    def get_queryset(self):
        queryset = AddressModel.objects.filter(user=self.request.user)
        return queryset
    
    
class AddAddressesView(CustomerPermissions,CreateView,SuccessMessageMixin):
    form_class = AddAddressesForm
    template_name = 'dashboard/customer/orders/add-addresses.html'
    success_message = 'آدرس به درستی زخیره شد'
    success_url = reverse_lazy('dashboard:customer:addresses')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ChangeAddressesView(CustomerPermissions,UpdateView):
    template_name = 'dashboard/customer/orders/change-addresses.html'
    form_class = AddAddressesForm
    success_url = reverse_lazy("dashboard:customer:addresses")
    success_message = 'Profile changed successfully'

    def get_object(self, queryset = None):
        return AddressModel.objects.get(pk=self.kwargs.get('pk') ,user = self.request.user)