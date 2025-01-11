from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from ...permissions import AdminPermissions
from ..forms import *
from accounts.models import User, Profile


class AdminDashboard(LoginRequiredMixin, AdminPermissions, TemplateView):
    template_name = "dashboard/admin/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_info"] = User.objects.get(pk=self.request.user.id)
        return context


class ChangePassView(
    LoginRequiredMixin,
    AdminPermissions,
    SuccessMessageMixin,
    PasswordChangeView,
):
    template_name = "dashboard/admin/profile/change-pass.html"
    form_class = ChangePassForm
    success_url = reverse_lazy("dashboard:admin:change-pass")
    success_message = "Password changed successfully"


class ProfileView(
    LoginRequiredMixin, AdminPermissions, UpdateView, SuccessMessageMixin
):
    template_name = "dashboard/admin/profile/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("dashboard:admin:profile")
    success_message = "Profile changed successfully"

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
