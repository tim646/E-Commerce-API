from rest_framework.serializers import ModelSerializer

from apps.order.models import Order


class OrderUpdateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("user", "payment_method", "status", "cart", "shipping_cost", "total")
