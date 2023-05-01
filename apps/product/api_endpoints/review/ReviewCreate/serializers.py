from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.product.models import ProductReview


class ProductReviewCreateSerializer(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ProductReview
        fields = ["user", "product", "comment", "rating"]

    def validate_rating(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError("Rating must be between 1 and 10")
        return value

    def create(self, validated_data):
        user = self.context["request"].user
        product = validated_data["product"]

        comment_owner = ProductReview.objects.filter(user=user, product=product).exists()
        if comment_owner:
            raise serializers.ValidationError("You can't comment twice")

        validated_data["user"] = user
        return super().create(validated_data)
