from django.db import router
from rest_framework.routers import DefaultRouter
from . import views

app_name = "shop"

urlpatterns = []

router = DefaultRouter()
router.register("products", views.ProductsApiView, basename="products")
router.register("categories", views.CategoriesApiView, basename="categories")
urlpatterns += router.urls