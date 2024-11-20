from django.views.generic import TemplateView,FormView,View
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import AddressModel,OrderModel,CouponModel,OrderItemsModel
from cart.models import CartModel
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
        total_price = cart.calculate_total_price()
        tax_price = total_price/100 * 9
        final_price = total_price + tax_price
        order = self.create_order(user,address,coupon,final_price)
        self.merge_items(cart,order)

        order.save()

        return super().form_valid(form)
    
    def create_order(self,user,address,coupon,final_price):
        if coupon:
            self.update_coupon(user,coupon)
            discounted_price = final_price/100 * coupon.discount_percent
            final_price -= discounted_price
        return OrderModel.objects.create(user=user,address=address,coupon=coupon,final_price=final_price)

    def merge_items(self,cart,order):
        for prod in cart.cart_items.all():
            OrderItemsModel.objects.create(
                order = order,
                product = prod.product,
                quantity = prod.quantity,
                price = prod.product.offer()
            )
        
    def update_coupon(self,user,coupon):
        if coupon:
            coupon.max_limit_usage -= 1
            coupon.used_by.add(user)
            coupon.save()

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartModel.objects.get(user=self.request.user)
        total_price = cart.calculate_total_price()
        tax_price = total_price/100 * 9
        final_price = total_price + tax_price
        context["addresses"] = AddressModel.objects.filter(user = self.request.user)
        context["total_price"] = total_price
        context["tax_price"] = tax_price
        context["final_price"] = final_price

        return context
    
class CheckView(View):
    def post(self, request, *args, **kwargs):
        coupon_code = request.POST.get('coupon_code')
        message = 'کد تخفیف با موفقیت ثبت شد'
        try:
            coupon = CouponModel.objects.get(code=coupon_code)
        except CouponModel.DoesNotExist:
            return JsonResponse({'message':'کد تخفیف یافت نشد'})
        
        else:
            if self.request.user in coupon.used_by.all():
                message = 'این کد توسط شما یک بار استفاده شده است'
            if coupon.max_limit_usage == 0 :
                message = 'کد دیگر فاقد ارزش است'
            else:
                cart = CartModel.objects.get(user=self.request.user)
                
                total_price = cart.calculate_total_price()
                
                discounted_price = total_price/100 * coupon.discount_percent


        return JsonResponse({'discounted_price':discounted_price,'message':message})   


class OrderCompleteView(TemplateView):
    template_name = 'order/complete.html'