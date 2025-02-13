from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from .forms import SetPasswordForm

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="sign-up"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/reset_password/reset_password.html"
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/reset_password/reset_password_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/reset_password/reset_password_form.html",
            form_class=SetPasswordForm,
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/reset_password/reset_password_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("api/v1/", include("accounts.api.v1.urls")),
]
