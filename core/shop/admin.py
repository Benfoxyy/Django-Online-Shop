from django.contrib import admin
from .models import ProductModel,CategoryModel,ProductImage

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'discount_percent', 'stock', 'status')

@admin.register(CategoryModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(ProductImage)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')