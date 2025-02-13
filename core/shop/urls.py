from django.urls import include, path, re_path
from . import views

app_name = "shop"

urlpatterns = [
    path(
        "product/list/grid/",
        views.ShopProductGridListView.as_view(),
        name="list_grid",
    ),
    path("product/list/", views.ShopProductListView.as_view(), name="list"),
    re_path(
        r"product/(?P<slug>[-\w]+)/detail/",
        views.ShopProductDetailView.as_view(),
        name="detail",
    ),
    path(
        "product/add-or-remove-wish/",
        views.AddOrRemoveWish.as_view(),
        name="modify-wish",
    ),
    # Shop API section
    path("api/v1/", include("shop.api.urls")),
]
