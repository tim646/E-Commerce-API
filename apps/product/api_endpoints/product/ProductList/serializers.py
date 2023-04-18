from django.db.models import Avg
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from apps.product.models import Product, ProductReview


class ProductListSerializer(ModelSerializer):
    description = serializers.SerializerMethodField()
    rating_avg = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'sell_price', 'original_price', 'color', 'rating_avg']

    def get_description(self, obj):
        return obj.description[:70] + '...'

    def get_rating_avg(self, obj):
        reviews = ProductReview.objects.filter(product=obj)
        if reviews:
            return reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
        return 0
