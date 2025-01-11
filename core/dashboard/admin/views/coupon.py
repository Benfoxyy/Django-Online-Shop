from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import FieldError
from ...permissions import AdminPermissions
from ..forms import AdminCouponForm
from order.models import CouponModel
from ..forms import *
from django.db.models import Count, F


class AdminCouponView(LoginRequiredMixin, AdminPermissions, ListView):
    template_name = "dashboard/admin/coupons/coupon-list.html"
    context_object_name = "coupons"

    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get("page_size", self.paginate_by)

    def get_queryset(self):
        queryset = CouponModel.objects.all()
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(code__icontains=search_q)
        if category_id := self.request.GET.get("category_id"):
            if category_id == "1":
                queryset = queryset.annotate(
                    used_count=Count("used_by")
                ).exclude(max_limit_usage=F("used_count"))
            elif category_id == "2":
                queryset = queryset.annotate(
                    used_count=Count("used_by")
                ).filter(max_limit_usage=F("used_count"))
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset


class AdminCouponCreateView(
    LoginRequiredMixin, AdminPermissions, CreateView, SuccessMessageMixin
):
    queryset = CouponModel.objects.all()
    template_name = "dashboard/admin/coupons/coupon-create.html"
    form_class = AdminCouponForm
    success_url = reverse_lazy("dashboard:admin:coupon-list")
    success_message = "کد تخفیف با موفقیت ایجاد شد"
