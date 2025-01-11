from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from accounts.models import Profile


class ChangePassForm(PasswordChangeForm):
    pass


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "phone_number"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["phone_number"].widget.attrs[
            "class"
        ] = "form-control text-center"
        self.fields["first_name"].widget.attrs[
            "placeholder"
        ] = "نام خود را وارد نمایید"
        self.fields["last_name"].widget.attrs[
            "placeholder"
        ] = "نام خانوادگی را وارد نمایید"
        self.fields["phone_number"].widget.attrs[
            "placeholder"
        ] = "شماره همراه را وارد نمایید"
