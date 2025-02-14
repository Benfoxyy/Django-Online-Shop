from rest_framework import serializers
from shop.models import ProductModel, CategoryModel
from django.urls import reverse


class CategoriesApiView(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = [
            "id",
            "title",
            "slug",
        ]


class ProductsApiSerializer(serializers.ModelSerializer):
    discounted_price = serializers.ReadOnlyField(source="offer")
    relative_url = serializers.ReadOnlyField(source="get_absolute_url")
    absolute_url = serializers.SerializerMethodField(
        method_name="obj_absolute_url"
    )

    class Meta:
        model = ProductModel
        fields = [
            "id",
            'user',
            "category",
            "title",
            "slug",
            "description",
            "stock",
            "status",
            "price",
            "discount_percent",
            "discounted_price",
            "sells",
            "avg_rate",
            "relative_url",
            "absolute_url",
            "created_date",
            "updated_date",
        ]
        read_only_fields = [
            "user",
            "sells",
            "avg_rate",
            "created_date",
            "updated_date",
        ]

    def obj_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(
            reverse("shop:shop-api-v1:products-detail", kwargs={"pk": obj.pk})
        )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get("request")
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("relative_url")
            rep.pop("absolute_url")
        rep["category"] = CategoriesApiView(
            instance.category.all(), many=True
        ).data
        return rep
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
