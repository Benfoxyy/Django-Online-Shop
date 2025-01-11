from django.urls import path
from .. import views

urlpatterns = [
    path("coupon/list/", views.AdminCouponView.as_view(), name="coupon-list"),
    path(
        "coupon/create/",
        views.AdminCouponCreateView.as_view(),
        name="coupon-create",
    ),
]
