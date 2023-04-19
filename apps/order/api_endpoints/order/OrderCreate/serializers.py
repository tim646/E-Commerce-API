from rest_framework.serializers import ModelSerializer

from apps.order.models import Order


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "cart",
            "user",
            "status",
        )
