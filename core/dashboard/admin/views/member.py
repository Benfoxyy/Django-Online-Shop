from django.views.generic import UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import FieldError
from ...permissions import AdminPermissions
from ..forms import *
from accounts.models import User, UserType


class AdminMemberListView(LoginRequiredMixin, AdminPermissions, ListView):
    template_name = "dashboard/admin/members/member-list.html"
    context_object_name = "members"

    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get("page_size", self.paginate_by)

    def get_queryset(self):
        queryset = (
            User.objects.all()
            .exclude(email=self.request.user.email)
            .exclude(user_type=UserType.superuser.value)
        )
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(email__icontains=search_q)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset


class AdminMemberEditView(
    LoginRequiredMixin, AdminPermissions, UpdateView, SuccessMessageMixin
):
    template_name = "dashboard/admin/members/member-edit.html"
    form_class = AdminMemberEditForm
    success_message = "کاربر با موفقیت ویرایش شد"

    def get_queryset(self):
        return (
            User.objects.all()
            .exclude(email=self.request.user.email)
            .exclude(user_type=UserType.superuser.value)
        )

    def get_success_url(self):
        return reverse_lazy(
            "dashboard:admin:member-edit", kwargs={"pk": self.get_object().pk}
        )
