from django.views.generic import ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import FieldError
from ...permissions import AdminPermissions
from ..forms import *
from ...models import TicketModel


class AdminTicketListView(LoginRequiredMixin, AdminPermissions, ListView):
    template_name = "dashboard/admin/tickets/ticket-list.html"
    context_object_name = "tickets"

    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get("page_size", self.paginate_by)

    def get_queryset(self):
        queryset = TicketModel.objects.all()
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(description__icontains=search_q)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset


class AdminTicketDetailView(LoginRequiredMixin, AdminPermissions, DetailView):
    model = TicketModel
    template_name = "dashboard/admin/tickets/ticket-detail.html"
    context_object_name = "ticket"


class AdminTicketDeleteView(
    LoginRequiredMixin, AdminPermissions, DeleteView, SuccessMessageMixin
):
    queryset = TicketModel.objects.all()
    template_name = "dashboard/admin/tickets/ticket-delete.html"
    success_url = reverse_lazy("dashboard:admin:ticket-list")
    success_message = "تیکت با موفقیت حذف شد"
