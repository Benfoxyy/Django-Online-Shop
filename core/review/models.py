from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class ReviewModel(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    product = models.ForeignKey("shop.ProductModel", on_delete=models.CASCADE)
    description = models.TextField()
    rate = models.IntegerField(default=5, validators=[MinValueValidator(0),MaxValueValidator(5)])

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.product}'
    
    class Meta:
        ordering = ['-created_date']