from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_list_or_404
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from ..permissions import CustomerPermissions
from .forms import *
from .forms import AddAddressesForm
from order.models import AddressModel,OrderModel

class CustomerDashboard(LoginRequiredMixin,CustomerPermissions,TemplateView):
    template_name = 'dashboard/customer/home.html'

class ChangePassView(LoginRequiredMixin,CustomerPermissions,SuccessMessageMixin,PasswordChangeView):
    template_name = 'dashboard/customer/profile/change-pass.html'
    form_class = ChangePassForm
    success_url = reverse_lazy("dashboard:customer:change-pass")
    success_message = 'گذرواژه با موفقیت تغییر کرد'

class ProfileView(LoginRequiredMixin,CustomerPermissions,UpdateView,SuccessMessageMixin):
    template_name = 'dashboard/customer/profile/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy("dashboard:customer:profile")
    success_message = 'پروفایل شما با موفقیت تغییر کرد'

    def get_object(self, queryset = None):
        return Profile.objects.get(user = self.request.user)

class AddressesView(LoginRequiredMixin,CustomerPermissions,ListView):
    template_name = 'dashboard/customer/orders/addresses.html'
    context_object_name = 'addresses'
    
    def get_queryset(self):
        queryset = AddressModel.objects.filter(user=self.request.user)
        return queryset
    
    
class AddAddressesView(LoginRequiredMixin,CustomerPermissions,CreateView,SuccessMessageMixin):
    form_class = AddAddressesForm
    template_name = 'dashboard/customer/orders/add-addresses.html'
    success_message = 'آدرس با موفقیت ذخیره شد'
    success_url = reverse_lazy('dashboard:customer:addresses')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ChangeAddressesView(LoginRequiredMixin,CustomerPermissions,UpdateView):
    template_name = 'dashboard/customer/orders/change-addresses.html'
    form_class = AddAddressesForm
    success_url = reverse_lazy("dashboard:customer:addresses")
    success_message = 'Profile changed successfully'

    def get_object(self, queryset = None):
        return AddressModel.objects.get(pk=self.kwargs.get('pk') ,user = self.request.user)
    

class OrderView(ListView):
    template_name = 'dashboard/customer/orders/orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = get_list_or_404(OrderModel, user=self.request.user)
        return queryset
    

    paginate_by = 9
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders_counter"] =len(self.get_queryset())
        return context
    

class OrderDetailView(DetailView):
    model = OrderModel
    template_name = 'dashboard/customer/orders/order-detail.html'
    context_object_name = 'order'

    
class OrderInvoiceView(DetailView):
    model = OrderModel
    template_name = 'dashboard/customer/orders/order-invoice.html'
    context_object_name = 'order'