from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.product.models import ProductReview


class ProductReviewUpdateSerializer(ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ["comment", "rating"]

    def validate(self, attrs):
        review = self.instance
        if review.date_created != review.date_updated:
            raise serializers.ValidationError("You can't update this review, because it was already updated.")
        return attrs
