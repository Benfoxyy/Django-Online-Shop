from django.urls import path, include
from . import views

app_name = "dashboard"

urlpatterns = [
    path("check/", views.DashboardCheckView.as_view(), name="check"),
    path("admin/", include("dashboard.admin.urls")),
    path("customer/", include("dashboard.customer.urls")),
    path(
        "profile/edit/", views.ProfileEditView.as_view(), name="profile-edit"
    ),
]
