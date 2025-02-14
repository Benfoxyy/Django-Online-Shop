from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from . import views

app_name = "account-api-v1"

urlpatterns = [
    # registraion
    path("signup/", views.SignUpApiView.as_view(), name="signup"),
    # jwt
    path('jwt/access/', TokenObtainPairView.as_view(), name='jwt_access'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
    # change_pasword
    # reset_password
    # email_validation
]
