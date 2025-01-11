from django.contrib import admin
from .models import (
    ProductModel,
    CategoryModel,
    ProductImageModel,
    WishListModel,
)


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "price",
        "discount_percent",
        "stock",
        "status",
    )


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(ProductImageModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "product")


@admin.register(WishListModel)
class WishListAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product")
