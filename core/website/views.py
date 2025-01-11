from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from dashboard.models import TicketModel


class IndexView(TemplateView):
    template_name = "website/index.html"


class AboutView(TemplateView):
    template_name = "website/about.html"


class ContactView(CreateView, SuccessMessageMixin):
    template_name = "website/contact.html"
    model = TicketModel
    fields = "__all__"
    success_url = "/contact/"
    success_message = "تیکت شما با موفقیت ارسال شد"

    error_messages = {
        "name": {
            "required": "فیلد اسم اجباری است",
        },
    }

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return redirect(self.request.META.get("HTTP_REFERER"))
