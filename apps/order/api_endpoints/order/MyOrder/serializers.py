from rest_framework.serializers import ModelSerializer

from apps.order.models import Order


class MyOrderListSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("status", "payment_method", "status", "cart", "shipping_cost", "total")
