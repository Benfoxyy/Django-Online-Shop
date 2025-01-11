from django.contrib import admin
from .models import PaymentModel


@admin.register(PaymentModel)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "authority",
        "amount",
        # "status_code",
        "status",
        "created_date",
    )
