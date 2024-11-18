from django.views.generic import TemplateView,FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import AddressModel,OrderModel,CouponModel,OrderItemsModel
from cart.models import CartItemModel,CartModel
from cart.cart import CartSession
from .forms import CheckOutForm

class CheckOutView(SuccessMessageMixin,FormView):
    template_name = 'order/checkout.html'
    form_class = CheckOutForm
    success_url = reverse_lazy('order:complete')
    success_message = 'سفارش با موفقیت ثبت شد'

    def get_form_kwargs(self):
        kwargs = super(CheckOutView,self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    def form_valid(self, form):
        user = self.request.user
        cart = CartModel.objects.get(user=user)
        address = form.cleaned_data['address_id']
        coupon = form.cleaned_data['coupon_code']
        order = self.create_order(user,address,coupon)
        self.merge_items(cart,order)
        order.save()
        return super().form_valid(form)
    
    def create_order(self,user,address,coupon):
        if coupon:
            self.update_coupon(user,coupon)
        return OrderModel.objects.create(user=user,address=address,coupon=coupon)

    def merge_items(self,cart,order):
        for prod in cart.cart_items.all():
            OrderItemsModel.objects.create(
                order = order,
                product = prod.product,
                quantity = prod.quantity,
                price = prod.product.offer()
            )
        
    def update_coupon(self,user,coupon):
        coupon.max_limit_usage -= 1
        coupon.used_by.add(user)
        coupon.save()

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartModel.objects.get(user=self.request.user)
        total_price = cart.calculate_total_price()
        context["addresses"] = AddressModel.objects.filter(user = self.request.user)
        context["final_price"] = total_price
        return context

class OrderCompleteView(TemplateView):
    template_name = 'order/complete.html'