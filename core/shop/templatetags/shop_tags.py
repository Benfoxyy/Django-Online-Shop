from django import template
from shop.models import ProductStatus, ProductModel,WishListModel

register = template.Library()

@register.inclusion_tag('includes/latest_prod.html', takes_context=True)
def show_latest_products(context):
    request = context['request']
    latest_products = ProductModel.objects.filter(status=ProductStatus.active.value).order_by('-created_date')[:8]
    context.update({
        'latest_products': latest_products,
        'is_wished' : WishListModel.objects.filter(user=request.user).values_list('product_id',flat=True) if request.user.is_authenticated else [],
        'request': request
    })
    return context

@register.inclusion_tag('includes/similar_prod.html', takes_context=True)
def show_similar_products(context, product):
    request = context['request']
    similar_products = ProductModel.objects.filter(
        status=ProductStatus.active.value,
        category__in=product.category.all()
    ).exclude(id=product.id).order_by('-created_date')[:4]
    context.update({
        'similar_products': similar_products,
        'is_wished' : WishListModel.objects.filter(user=request.user).values_list('product_id',flat=True) if request.user.is_authenticated else [],
        'request': request
    })
    return context