from django.urls import path
from .. import views

urlpatterns = [
    path(
        "products/show/", views.AdminShowProducts.as_view(), name="show-prod"
    ),
    path(
        "products/<int:pk>/edit/",
        views.AdminEditProducts.as_view(),
        name="edit-prod",
    ),
    path(
        "products/<int:pk>/delete/",
        views.AdminDeleteProducts.as_view(),
        name="delete-prod",
    ),
    path(
        "products/create/",
        views.AdminCreateProducts.as_view(),
        name="create-prod",
    ),
]
