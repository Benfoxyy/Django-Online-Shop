from django.urls import path
from . import views

app_name = "account-api-v1"

urlpatterns = [
    # registraion
    path("signup/", views.SignUpApiView.as_view(), name="signup"),
    # change_pasword
    # reset_password
    # email_validation
    # jwt
]
