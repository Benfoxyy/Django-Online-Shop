from django.urls import path
from . import views

app_name = 'admin'

urlpatterns = [
    path('home/',views.AdminDashboard.as_view(),name='home'),
    path('change-pass/',views.ChangePassView.as_view(),name='change-pass'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('products/show/',views.AdminShowProducts.as_view(),name='show-prod'),
    path('products/<int:pk>/edit/',views.AdminEditProducts.as_view(),name='edit-prod'),
    path('products/<int:pk>/delete/',views.AdminDeleteProducts.as_view(),name='delete-prod'),
    path('products/create/',views.AdminCreateProducts.as_view(),name='create-prod'),
]