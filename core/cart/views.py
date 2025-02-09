from django.views.generic import View, TemplateView
from django.http import JsonResponse
from .cart import CartSession


class AddProdView(View):
    def post(self, request, *args, **kwargs):
        cart = CartSession(request.session)
        if product_id := request.POST.get("product_id"):
            cart.add_prod(product_id)
        if request.user.is_authenticated:
            cart.cart_merge(request.user)
        return JsonResponse(
            {
                "cart": cart.get_cart(),
                "total_quantity": cart.get_cart_quantity(),
                "message": "!!محصول به سبد خرید اضافه شد",
            }
        )


class DelProdView(View):
    def post(self, request, *args, **kwargs):
        cart = CartSession(request.session)
        if product_id := request.POST.get("product_id"):
            cart.del_prod(product_id)
        if request.user.is_authenticated:
            cart.cart_merge(request.user)
        return JsonResponse(
            {
                "cart": cart.get_cart(),
                "total_quantity": cart.get_cart_quantity(),
            }
        )


class ChangeProdQuantityView(View):
    def post(self, request, *args, **kwargs):
        cart = CartSession(request.session)
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")
        if product_id and quantity:
            cart.change_prod_quantity(product_id, quantity)
        if request.user.is_authenticated:
            cart.cart_merge(request.user)
        return JsonResponse(
            {
                "cart": cart.get_cart(),
                "total_quantity": cart.get_cart_quantity(),
            }
        )


class CartView(TemplateView):
    template_name = "cart/cart.html"

    def get_template_names(self):
        cart = CartSession(self.request.session)
        if not cart.get_cart_items():
            return ["cart/empty-cart.html"]
        return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartSession(self.request.session)
        context["cart_items"] = cart.get_cart_items()
        context["total_quantity"] = cart.get_cart_quantity()
        context["total_price"] = cart.get_total_price()

        return context


class ClearView(View):
    def post(self, request, *args, **kwargs):
        cart = CartSession(request.session)
        cart.clear()
        if request.user.is_authenticated:
            cart.cart_merge(request.user)
        return JsonResponse({"cart": cart.get_cart()})
