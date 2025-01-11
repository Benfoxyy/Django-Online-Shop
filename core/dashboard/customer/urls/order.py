from django.urls import path
from .. import views

urlpatterns = [
    path("orders/", views.OrderView.as_view(), name="order-list"),
    path(
        "order/<int:pk>/",
        views.OrderDetailView.as_view(),
        name="order-detail",
    ),
    path(
        "order/<int:pk>/invoice/",
        views.OrderInvoiceView.as_view(),
        name="order-invoice",
    ),
]
