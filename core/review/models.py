from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Avg
from shop.models import ProductModel


class ReviewModel(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    description = models.TextField()
    rate = models.IntegerField(
        default=5, validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.product}"

    class Meta:
        ordering = ["-created_date"]


@receiver(post_save, sender=ReviewModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        rates = ReviewModel.objects.filter(product=product).aggregate(
            Avg("rate")
        )["rate__avg"]
        product.avg_rate = round(rates, 1)
        product.save()
