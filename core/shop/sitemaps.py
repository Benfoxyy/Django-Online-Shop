from django.contrib.sitemaps import Sitemap
from .models import ProductModel, ProductStatus


class ProductSitemap(Sitemap):
    changefreq = "dayly"
    priority = 0.8

    def items(self):
        return ProductModel.objects.filter(status=ProductStatus.active.value)

    def lastmod(self, obj):
        return obj.updated_date
