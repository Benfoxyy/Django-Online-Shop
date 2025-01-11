from django.urls import path
from .. import views

urlpatterns = [
    path("orders/list/", views.OrdersList.as_view(), name="orders-list"),
    path("order/<int:pk>/", views.OrderSingle.as_view(), name="order-single"),
]
