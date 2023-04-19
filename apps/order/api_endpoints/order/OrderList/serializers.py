from rest_framework.serializers import ModelSerializer

from apps.order.models import Order


class OrderListSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id'
            'user',
            'payment_method',
            'status',
            'cart',
            'shipping_cost',
            'total'
        )
