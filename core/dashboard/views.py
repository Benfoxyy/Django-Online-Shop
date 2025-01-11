from django.views.generic import View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import UserType
from django.contrib.messages.views import SuccessMessageMixin
from accounts.models import Profile
from django.urls import reverse_lazy
from django.shortcuts import redirect


class DashboardCheckView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        user_type = request.user.user_type
        if user_type == UserType.customer.value:
            return redirect(reverse_lazy("dashboard:customer:home"))
        elif user_type == UserType.admin.value:
            return redirect(reverse_lazy("dashboard:admin:home"))
        return super().dispatch(request, *args, **kwargs)


class ProfileEditView(UpdateView, SuccessMessageMixin):
    http_method_names = ["post"]
    model = Profile
    fields = ["avatar"]
    success_url = reverse_lazy("dashboard:check")
    success_message = "عکس پروفایل شما با موفقیت تغییر کرد"

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
