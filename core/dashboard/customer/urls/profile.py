from django.urls import path
from .. import views

urlpatterns = [
    path("home/", views.CustomerDashboard.as_view(), name="home"),
    path("change-pass/", views.ChangePassView.as_view(), name="change-pass"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
]
