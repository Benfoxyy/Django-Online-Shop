from typing import Any
from django.views import generic
from .models import ProductModel,ProductStatus

class ShopProductGridListView(generic.ListView):
    template_name = 'shop/products-grid.html'
    queryset = ProductModel.objects.filter(status=ProductStatus.active.value)

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['total_prod']= self.get_queryset().count()
        return context

class ShopProductListView(generic.ListView):
    template_name = 'shop/products.html'
    queryset = ProductModel.objects.filter(status=ProductStatus.active.value)

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['total_prod']= self.get_queryset().count()
        return context