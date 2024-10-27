from django.views.generic import TemplateView,UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from ..permissions import AdminPermissions
from .form import ChangePassForm,ProfileForm
from accounts.models import Profile

class AdminDashboard(AdminPermissions,TemplateView):
    template_name = 'dashboard/admin/home.html'

class ChangePassView(AdminPermissions,SuccessMessageMixin,PasswordChangeView):
    template_name = 'dashboard/admin/profile/change-pass.html'
    form_class = ChangePassForm
    success_url = reverse_lazy("dashboard:admin:change-pass")
    success_message = 'Password changed successfully'

class ProfileView(AdminPermissions,UpdateView,SuccessMessageMixin):
    template_name = 'dashboard/admin/profile/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy("dashboard:admin:profile")
    success_message = 'Profile changed successfully'

    def get_object(self, queryset = None):
        return Profile.objects.get(user = self.request.user)
    
class ProfileEditView(AdminPermissions,UpdateView,SuccessMessageMixin):
    http_method_names = ['post']
    model = Profile
    fields = ['avatar']
    success_url = reverse_lazy("dashboard:admin:home")
    success_message = 'Profile picture changed successfully'

    def get_object(self, queryset = None):
        return Profile.objects.get(user = self.request.user)
    
    def form_invalid(self, form):
        messages.error(self.request,'وایییی')
        return redirect(self.success_url)
