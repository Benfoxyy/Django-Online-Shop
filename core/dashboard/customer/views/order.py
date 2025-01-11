from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...permissions import CustomerPermissions
from ..forms import *
from order.models import OrderModel


class OrderView(LoginRequiredMixin, CustomerPermissions, ListView):
    template_name = "dashboard/customer/orders/orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        queryset = OrderModel.objects.filter(user=self.request.user)
        return queryset

    paginate_by = 9

    def get_paginate_by(self, queryset):
        return self.request.GET.get("page_size", self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders_counter"] = len(self.get_queryset())
        return context


class OrderDetailView(LoginRequiredMixin, CustomerPermissions, DetailView):
    model = OrderModel
    template_name = "dashboard/customer/orders/order-detail.html"
    context_object_name = "order"


class OrderInvoiceView(LoginRequiredMixin, DetailView):
    model = OrderModel
    template_name = "dashboard/customer/orders/order-invoice.html"
    context_object_name = "order"
