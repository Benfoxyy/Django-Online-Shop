from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import ReviewModel
from .forms import ReviewForm


class ReviewView(LoginRequiredMixin, CreateView):
    http_method_names = ["post"]
    model = ReviewModel
    form_class = ReviewForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        messages.success(self.request, "دیدگاه شما با موفقیت ثبت شد")
        return redirect(
            reverse_lazy(
                "shop:detail", kwargs={"slug": form.instance.product.slug}
            )
        )

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return redirect(self.request.META.get("HTTP_REFERER"))
