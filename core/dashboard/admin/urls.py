from django.urls import path
from . import views

app_name = 'admin'

urlpatterns = [
    path('home/',views.AdminDashboard.as_view(),name='home'),
    path('change-pass/',views.ChangePassView.as_view(),name='change-pass'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('profile/edit/',views.ProfileEditView.as_view(),name='profile-edit'),
]