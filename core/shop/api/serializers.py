from os import read
from rest_framework.serializers import ModelSerializer
from shop.models import ProductModel,CategoryModel

class ProductsApiSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
        read_only_fields = ['user']
        
        
class CategoriesApiView(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'