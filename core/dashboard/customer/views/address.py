from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ...permissions import CustomerPermissions
from ..forms import *
from order.models import AddressModel


class AddressesView(LoginRequiredMixin, CustomerPermissions, ListView):
    template_name = "dashboard/customer/orders/addresses.html"
    context_object_name = "addresses"

    def get_queryset(self):
        queryset = AddressModel.objects.filter(user=self.request.user)
        return queryset


class AddAddressesView(
    LoginRequiredMixin, CustomerPermissions, CreateView, SuccessMessageMixin
):
    form_class = AddAddressesForm
    template_name = "dashboard/customer/orders/add-addresses.html"
    success_message = "آدرس با موفقیت ذخیره شد"
    success_url = reverse_lazy("dashboard:customer:addresses")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChangeAddressesView(
    LoginRequiredMixin, CustomerPermissions, UpdateView
):
    template_name = "dashboard/customer/orders/change-addresses.html"
    form_class = AddAddressesForm
    success_url = reverse_lazy("dashboard:customer:addresses")
    success_message = "Profile changed successfully"

    def get_object(self, queryset=None):
        return AddressModel.objects.get(
            pk=self.kwargs.get("pk"), user=self.request.user
        )
