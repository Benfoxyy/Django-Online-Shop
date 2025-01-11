from django import forms
from accounts.models import User


class AdminMemberEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "is_active",
            "is_verified",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["is_active"].widget.attrs["class"] = "form-check-input"
        self.fields["is_verified"].widget.attrs["class"] = "form-check-input"
