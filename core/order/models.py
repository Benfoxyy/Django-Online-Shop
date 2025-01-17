from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal


class OrderStatusModel(models.IntegerChoices):
    pending = 1, "در انتظار پرداخت"
    success = 2, "موفقیت آمیز"
    faild = 3, "لغو شده"


class AddressModel(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    address = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address


class CouponModel(models.Model):
    code = models.CharField(max_length=100)
    discount_percent = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    max_limit_usage = models.IntegerField()
    used_by = models.ManyToManyField("accounts.User", blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ("-created_date",)


class OrderModel(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT)
    address = models.ForeignKey(AddressModel, on_delete=models.PROTECT)
    coupon = models.ForeignKey(
        CouponModel, on_delete=models.PROTECT, blank=True, null=True
    )
    status = models.IntegerField(
        choices=OrderStatusModel.choices,
        default=OrderStatusModel.pending.value,
    )
    final_price = models.DecimalField(
        default=0, max_digits=10, decimal_places=0
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ("-created_date",)

    def get_fulladdress(self):
        return f"({self.address.state} - {self.address.city}) {self.address.address}"

    def get_status(self):
        return {
            "id": self.status,
            "title": OrderStatusModel(self.status).name,
            "label": OrderStatusModel(self.status).label,
        }

    def get_totalprice(self):
        if self.coupon:
            discount_rate = Decimal(self.coupon.discount_percent) / Decimal(
                100
            )
            return self.final_price / (Decimal(1) - discount_rate)
        return self.final_price


class OrderItemsModel(models.Model):
    order = models.ForeignKey(
        OrderModel, on_delete=models.CASCADE, related_name="order_items"
    )
    product = models.ForeignKey("shop.ProductModel", on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=0)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order.user} - {self.product.title}"
