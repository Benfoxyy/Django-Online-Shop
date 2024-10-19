from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from accounts.models import UserType

class DashboardCheckView(LoginRequiredMixin,View):
    def dispatch(self, request, *args, **kwargs):
        user_type = request.user.user_type
        if user_type == UserType.customer.value:
            return redirect(reverse_lazy('dashboard:customer:home'))
        elif user_type == UserType.admin.value:
            return redirect(reverse_lazy('dashboard:admin:home'))
        return super().dispatch(request, *args, **kwargs)
    