from django.views.generic import View,TemplateView
from django.http import JsonResponse
from .cart import CartSession

class AddProd(View):
    def post(self, request, *args, **kwargs):
        cart = CartSession(request.session)
        if product_id := request.POST.get('product_id'):
            cart.add_prod(product_id)
        return JsonResponse({'cart':cart.get_cart(),'total_quantity':cart.get_cart_quantity()})
    
class CartView(TemplateView):
    template_name = 'cart/cart.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartSession(self.request.session)
        context['cart_items'] = cart.get_cart_items()
        context['total_quantity'] = cart.get_cart_quantity()
        context['total_price'] = cart.get_total_price()
        
        return context
    