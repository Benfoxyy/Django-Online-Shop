from django.contrib import admin
from .models import ReviewModel


@admin.register(ReviewModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "rate")
