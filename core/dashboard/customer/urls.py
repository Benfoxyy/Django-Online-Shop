from django.urls import path
from . import views

app_name = 'customer'  # Define app name here. This will be used in the URL configuration.  # noqa: E501

urlpatterns = [
    path('home/',views.CustomerDashboard.as_view(),name='home'),
    path('addresses/',views.AddressesView.as_view(),name='addresses'),
    path('addresses-add/',views.AddAddressesView.as_view(),name='add-addresses'),
    path('addresses-change/<int:pk>/',views.ChangeAddressesView.as_view(),name='change-addresses'),
]
