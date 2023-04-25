from django.db.models import Avg
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.product.models import Product, ProductReview


class ProductListSerializer(ModelSerializer):
    description = serializers.SerializerMethodField()
    rating_avg = serializers.SerializerMethodField()
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    features = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product

        fields = [
            "id",
            "name",
            "image",
            "description",
            "original_price",
            "discount_percentage",
            "sell_price",
            "color",
            "rating_avg",
            "features",
            "brand",
            "category",
        ]

    def get_description(self, obj):
        return obj.description[:70] + "..."

    def get_rating_avg(self, obj):
        reviews = ProductReview.objects.filter(product=obj)
        if reviews:
            return reviews.aggregate(avg_rating=Avg("rating"))["avg_rating"]
        return 0


class RelatedProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "image", "sell_price", "original_price"]
