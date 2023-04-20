from rest_framework.serializers import ModelSerializer

from apps.product.models import ProductReview


class ProductReviewCreateSerializer(ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ["product", "comment", "rating"]
