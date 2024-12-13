from django.contrib.auth import views as auth_views
from .forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class LoginView(SuccessMessageMixin,auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    success_message = 'کاربر با موفقیت وارد شد'
    

class LogoutView(auth_views.LogoutView):
    pass