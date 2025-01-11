from django.views.generic import TemplateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from accounts.models import User
from ...permissions import CustomerPermissions
from ..forms import *


class CustomerDashboard(
    LoginRequiredMixin, CustomerPermissions, TemplateView
):
    template_name = "dashboard/customer/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_info"] = User.objects.get(pk=self.request.user.id)
        return context


class ChangePassView(
    LoginRequiredMixin,
    CustomerPermissions,
    SuccessMessageMixin,
    PasswordChangeView,
):
    template_name = "dashboard/customer/profile/change-pass.html"
    form_class = ChangePassForm
    success_url = reverse_lazy("dashboard:customer:change-pass")
    success_message = "گذرواژه با موفقیت تغییر کرد"


class ProfileView(
    LoginRequiredMixin, CustomerPermissions, UpdateView, SuccessMessageMixin
):
    template_name = "dashboard/customer/profile/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("dashboard:customer:profile")
    success_message = "پروفایل شما با موفقیت تغییر کرد"

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
