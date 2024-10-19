from django.urls import path
from . import views

app_name = 'admin'

urlpatterns = [
    path('admin/',views.AdminDashboard.as_view(),name='home'),
]