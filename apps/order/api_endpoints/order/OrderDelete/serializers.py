from rest_framework.serializers import ModelSerializer

from apps.order.models import Order


class OrderDeleteSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("user", "id")
