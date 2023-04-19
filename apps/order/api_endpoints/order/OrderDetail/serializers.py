from rest_framework.serializers import ModelSerializer

from apps.order.models import Order


class OrderDetailSerializer(ModelSerializer):
    class Mete:
        model = Order
        fields = (
            "cart",
            "user",
            "status",
        )
