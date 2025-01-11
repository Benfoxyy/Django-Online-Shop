from django.urls import path, include

app_name = "admin"

urlpatterns = [
    path("", include("dashboard.admin.urls.profile")),
    path("", include("dashboard.admin.urls.product")),
    path("", include("dashboard.admin.urls.order")),
    path("", include("dashboard.admin.urls.coupon")),
    path("", include("dashboard.admin.urls.member")),
    path("", include("dashboard.admin.urls.ticket")),
]
