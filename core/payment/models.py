from django.db import models


class PaymentStatus(models.IntegerChoices):
    pending = 1, "در حال انتظار"
    success = 2, "موفق"
    faild = 3, "نا موفق"


class PaymentModel(models.Model):
    authority = models.CharField(max_length=40)
    amount = models.DecimalField(decimal_places=0, max_digits=10)
    order = models.ForeignKey(
        "order.OrderModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="order_model",
    )
    status = models.IntegerField(
        choices=PaymentStatus.choices, default=PaymentStatus.pending.value
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.authority} , {self.amount}"
