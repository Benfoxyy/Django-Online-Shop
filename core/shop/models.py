from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField

class ProductStatus(models.IntegerChoices):
    active = 1, 'فعال'
    deactive = 2, 'غیرفعال'

class CategoryModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ProductModel(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT)
    category = models.ManyToManyField(CategoryModel)
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique=True)
    image = models.ImageField(default='default/proddef.png',upload_to='products/img')
    description = RichTextField()
    stock = models.PositiveIntegerField(default=0)
    status = models.IntegerField(choices=ProductStatus.choices,default=ProductStatus.active.value)
    price = models.DecimalField(decimal_places=0,max_digits=10)
    discount_percent = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])

    avg_rate = models.FloatField(default=0.0)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_date',)

    def offer(self):
        if self.discount_percent:
            return self.price-(self.price*self.discount_percent)/100
        return self.price
    
    def is_published(self):
        return self.status == ProductStatus.active.value

    def __str__(self):
        return self.title
    
class ProductImage(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='products/img/extera')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class WishListModel(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)