from django import forms
from shop.models import ProductModel
from django_ckeditor_5.widgets import CKEditor5Widget


class AdminEditProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = [
            "title",
            "slug",
            "price",
            "discount_percent",
            "category",
            "stock",
            "status",
            "description",
        ]
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs["class"] = "form-control"
        self.fields["title"].widget.attrs["id"] = "titleInput"
        self.fields["slug"].widget.attrs["class"] = "form-control"
        self.fields["slug"].widget.attrs["id"] = "slugInput"
        self.fields["category"].widget.attrs["id"] = "cat-id"
        self.fields["stock"].widget.attrs["class"] = "form-control"
        self.fields["stock"].widget.attrs["type"] = "number"
        self.fields["status"].widget.attrs["class"] = "form-select"
        self.fields["price"].widget.attrs["class"] = "form-control"
        self.fields["discount_percent"].widget.attrs["class"] = "form-control"


class ProductImageForm(forms.Form):
    images = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["images"].widget.attrs["class"] = "form-control"
        self.fields["images"].widget.attrs["multiple"] = True
