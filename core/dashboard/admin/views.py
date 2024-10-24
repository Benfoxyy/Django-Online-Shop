from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from ..permissions import AdminPermissions
from .form import ChangePassForm

class AdminDashboard(AdminPermissions,TemplateView):
    template_name = 'dashboard/admin/home.html'

class ChangePassView(AdminPermissions,SuccessMessageMixin,PasswordChangeView):
    template_name = 'dashboard/admin/profile/change-pass.html'
    form_class = ChangePassForm
    success_url = reverse_lazy("dashboard:admin:change-pass")
    success_message = 'Password changed successfully'