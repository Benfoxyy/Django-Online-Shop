from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.CartView.as_view(), name="cart-summery"),
    path("session/add-prod/", views.AddProdView.as_view(), name="add-prod"),
    path("session/del-prod/", views.DelProdView.as_view(), name="del-prod"),
    path("session/clear/", views.ClearView.as_view(), name="clear"),
    path(
        "session/change-prod-quantity/",
        views.ChangeProdQuantityView.as_view(),
        name="change-prod-quantity",
    ),
]
