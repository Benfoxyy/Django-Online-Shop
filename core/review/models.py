from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
from shop.models import ProductModel

class ReviewModel(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    description = models.TextField()
    rate = models.IntegerField(default=5, validators=[MinValueValidator(0),MaxValueValidator(5)])

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.product}'
    
    class Meta:
        ordering = ['-created_date']



@receiver(post_save,sender=ReviewModel)
def create_profile(sender,instance,created,**kwargs):
    if created:
        product = instance.product
        rates = ReviewModel.objects.filter(product=product).values_list('rate',flat=True)
        product.avg_rate = "{:.1f}".format(sum(rates)/len(rates))
        product.save()
