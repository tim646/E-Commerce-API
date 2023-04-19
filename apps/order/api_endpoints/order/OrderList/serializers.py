from rest_framework.serializers import ModelSerializer

from apps.order.models import Order


class OrderListSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "user",
            "cart",
            "status",
        )
