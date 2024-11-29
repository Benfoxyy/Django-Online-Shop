from django.views.generic import View
from django.urls import reverse_lazy
from django.shortcuts import redirect,get_object_or_404
from .zarinpal_client import ZarinPalSandbox
from .models import PaymentModel,PaymentStatus
from order.models import OrderModel

class VerificationView(View):

    def get(self, request, *args, **kwargs):
        payment_obj = get_object_or_404(PaymentModel,authority=request.GET.get('Authority'))
        order = OrderModel.objects.get(id=payment_obj.order.id)
        zarinpal = ZarinPalSandbox()
        response = zarinpal.payment_verification(order.final_price,payment_obj.authority)
        try:
            if response['data']['code'] == 100 or response['data']['code'] == 101:
                payment_obj.status = PaymentStatus.success.value
                payment_obj.save()
                return redirect(reverse_lazy('order:complete'))
        except KeyError:
            payment_obj.status = PaymentStatus.faild.value
            payment_obj.save()
            return redirect(reverse_lazy('order:faild'))
        
