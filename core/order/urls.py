from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path("checkout/", views.CheckOutView.as_view(), name="checkout"),
    path("check/", views.CheckView.as_view(), name="check"),
    path("complete/", views.OrderCompleteView.as_view(), name="complete"),
    path("faild/", views.OrderFaildView.as_view(), name="faild"),
]
