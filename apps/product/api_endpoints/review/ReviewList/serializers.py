from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.product.models import ProductReview


class ProductReviewListSerializer(ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = ProductReview
        fields = ["id", "username", "rating", "comment", "date_created", "date_updated"]

    def get_username(self, obj):
        return obj.user.username
