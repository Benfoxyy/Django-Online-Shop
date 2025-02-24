from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView
from . import views

app_name = "account-api-v1"

urlpatterns = [
    # registraion
    path("signup/", views.SignUpApiView.as_view(), name="signup"),
    # jwt
    path('jwt/access/', views.CudtomTokenObtainPairView.as_view(), name='jwt_access'),
    path('jwt/refresh/', views.CustomTokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
    # get user
    path("get/me/", views.GetMeApiView.as_view(), name="get-me"),
    path("get/user/<int:pk>/", views.GetUserApiView.as_view(), name="get-user"),
    # change_pasword
    # reset_password
    # email_validation
]
