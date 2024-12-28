from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from accounts.models import Profile,User
from shop.models import ProductModel
from order.models import CouponModel

class ChangePassForm(PasswordChangeForm):
    pass

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'phone_number'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control text-center'
        self.fields['first_name'].widget.attrs['placeholder'] = 'نام خود را وارد نمایید'
        self.fields['last_name'].widget.attrs['placeholder'] = 'نام خانوادگی را وارد نمایید'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'شماره همراه را وارد نمایید'


class AdminEditProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = [
            'title',
            'slug',
            'price',
            'discount_percent',
            'category',
            'stock',
            'status',
            'description',
            'image',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['id'] = 'titleInput'
        self.fields['slug'].widget.attrs['class'] = 'form-control'
        self.fields['slug'].widget.attrs['id'] = 'slugInput'
        self.fields['category'].widget.attrs['id'] = 'cat-id'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['id'] = 'ckeditor'
        self.fields['stock'].widget.attrs['class'] = 'form-control'
        self.fields['stock'].widget.attrs['type'] = 'number'
        self.fields['status'].widget.attrs['class'] = 'form-select'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['discount_percent'].widget.attrs['class'] = 'form-control'



class AdminCouponForm(forms.ModelForm):
    class Meta:
        model = CouponModel
        fields = [
            'code',
            'discount_percent',
            'max_limit_usage',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].widget.attrs['class'] = 'form-control text-center'
        self.fields['code'].widget.attrs['placeholder'] = 'کد تخفیف را وارد نمایید'
        self.fields['discount_percent'].widget.attrs['class'] = 'form-control text-center'
        self.fields['discount_percent'].widget.attrs['placeholder'] = 'مقدار تخفیف'
        self.fields['max_limit_usage'].widget.attrs['class'] = 'form-control text-center'
        self.fields['max_limit_usage'].widget.attrs['placeholder'] = 'حداکثر تعداد استفاده'



class AdminMemberEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'is_active',
            'is_verified',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_active'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_verified'].widget.attrs['class'] = 'form-check-input'