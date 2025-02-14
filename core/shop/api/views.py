from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ProductsApiSerializer, CategoriesApiView
from shop.models import ProductModel, ProductStatus, CategoryModel
from .paginations import CustomPagination


class ProductsApiView(ModelViewSet):
    serializer_class = ProductsApiSerializer
    queryset = ProductModel.objects.filter(status=ProductStatus.active.value)
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category"]
    search_fields = ["title"]
    ordering_fields = ["created_date"]
    pagination_class = CustomPagination


class CategoriesApiView(ModelViewSet):
    serializer_class = CategoriesApiView
    queryset = CategoryModel.objects.all()
