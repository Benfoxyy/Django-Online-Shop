from django import forms
from .models import ReviewModel


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ["product", "rate", "description"]

        error_messages = {
            "description": {
                "required": "فیلد توضیحات اجباری است",
            },
        }
