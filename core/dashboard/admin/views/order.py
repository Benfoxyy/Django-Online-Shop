from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...permissions import AdminPermissions
from order.models import OrderModel


class OrdersList(LoginRequiredMixin, AdminPermissions, ListView):
    queryset = OrderModel.objects.all()
    template_name = "dashboard/admin/orders/list.html"
    context_object_name = "orders"

    paginate_by = 5

    def get_paginate_by(self, queryset):
        return self.request.GET.get("page_size", self.paginate_by)


class OrderSingle(LoginRequiredMixin, AdminPermissions, DetailView):
    model = OrderModel
    template_name = "dashboard/admin/orders/single.html"
    context_object_name = "order"
