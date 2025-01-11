from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import CustomAuthenticationForm, RegistrationForm
from django.contrib.messages.views import SuccessMessageMixin


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = "accounts/signup.html"
    form_class = RegistrationForm
    success_message = "ثبت نام کاربر با موفقیت انجام شد"
    success_url = "/"

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        login(self.request, user)
        return response


class LoginView(SuccessMessageMixin, auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = CustomAuthenticationForm
    redirect_authenticated_user = True
    success_message = "کاربر با موفقیت وارد شد"


class LogoutView(auth_views.LogoutView):
    pass
