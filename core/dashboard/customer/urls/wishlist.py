from django.urls import path
from .. import views

urlpatterns = [
    path("whishlist/", views.WishListView.as_view(), name="wishlist"),
    path(
        "whishlist/delete/<int:pk>/",
        views.DeleteWishView.as_view(),
        name="delete-wish",
    ),
]
