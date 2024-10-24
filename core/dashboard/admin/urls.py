from django.urls import path
from . import views

app_name = 'admin'

urlpatterns = [
    path('home/',views.AdminDashboard.as_view(),name='home'),
    path('change-pass/',views.ChangePassView.as_view(),name='change-pass'),
]