from django import template
from shop.models import ProductStatus, ProductModel
register = template.Library()

@register.inclusion_tag('includes/latest_prod.html')
def show_latest_products():
    latest_products = ProductModel.objects.filter(status=ProductStatus.active.value).order_by('-created_date')[:8]
    return {'latest_products': latest_products}

@register.inclusion_tag('includes/similar_prod.html')
def show_similar_products(product):
    similar_products = ProductModel.objects.filter(
        status=ProductStatus.active.value,
        category__in=product.category.all()
        ).exclude(id=product.id).order_by('-created_date')[:4]
    return {'similar_products': similar_products}
