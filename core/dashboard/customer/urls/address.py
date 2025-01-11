from django.urls import path
from .. import views

urlpatterns = [
    path("addresses/", views.AddressesView.as_view(), name="addresses"),
    path(
        "addresses-add/",
        views.AddAddressesView.as_view(),
        name="add-addresses",
    ),
    path(
        "addresses-change/<int:pk>/",
        views.ChangeAddressesView.as_view(),
        name="change-addresses",
    ),
]
