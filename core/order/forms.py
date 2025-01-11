from django import forms
from order.models import AddressModel, CouponModel


class CheckOutForm(forms.Form):
    address_id = forms.IntegerField(required=True)
    coupon_code = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(CheckOutForm, self).__init__(*args, **kwargs)

    def clean_address_id(self):
        address_id = self.cleaned_data.get("address_id")
        try:
            address = AddressModel.objects.get(
                id=address_id, user=self.request.user
            )
        except AddressModel.DoesNotExist:
            raise forms.ValidationError("آدرس با اطلاعات کاربر تطابق ندارد")

        return address

    def clean_coupon_code(self):
        coupon_code = self.cleaned_data.get("coupon_code")
        coupon = None
        if coupon_code == "":
            return coupon

        try:
            coupon = CouponModel.objects.get(code=coupon_code)
        except CouponModel.DoesNotExist:
            raise forms.ValidationError("کد وارد شده اشتباه است")

        if coupon:
            if self.request.user in coupon.used_by.all():
                raise forms.ValidationError(
                    "این کد توسط شما یک بار استفاده شده است"
                )
            if coupon.max_limit_usage == 0:
                raise forms.ValidationError("کد دیگر فاقد ارزش است")
        return coupon
