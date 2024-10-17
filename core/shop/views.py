from django.views import generic
from .models import ProductModel,ProductStatus,CategoryModel
from django.core.exceptions import FieldError
from cart.cart import CartSession
from django.http import JsonResponse

class ShopProductGridListView(generic.ListView):
    template_name = 'shop/products-grid.html'
    paginate_by = 9
    
    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)

    def get_queryset(self):
        queryset = ProductModel.objects.filter(status=ProductStatus.active.value)
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(title__icontains=search_q)
        if minprice_q := self.request.GET.get("min_price"):
            queryset = queryset.filter(price__gte=minprice_q)
        if maxprice_q := self.request.GET.get("max_price"):
            queryset = queryset.filter(price__lte=maxprice_q)
        if category_id := self.request.GET.get("category_id"):
            queryset = queryset.filter(category__id=category_id)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset
    

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['total_prod']= self.get_queryset().count()
        context['categories']= CategoryModel.objects.all()
        return context

class ShopProductListView(generic.ListView):
    template_name = 'shop/products.html'
    queryset = ProductModel.objects.filter(status=ProductStatus.active.value)
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['total_prod']= self.get_queryset().count()
        return context
    

class ShopProductDetailView(generic.DeleteView):
    template_name = 'shop/product_detail.html'
    queryset = ProductModel.objects.filter(status=ProductStatus.active.value)


class AddProdDetailView(generic.View):
    def post(self, request, *args, **kwargs):
        cart = CartSession(request.session)
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        if product_id and quantity:
            cart.add_prod(product_id,quantity)
        return JsonResponse({'cart':cart.get_cart(),'total_quantity':cart.get_cart_quantity()})   