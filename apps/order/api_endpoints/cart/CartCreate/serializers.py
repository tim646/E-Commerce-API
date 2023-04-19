from rest_framework.serializers import ModelSerializer

from apps.order.models import Cart


class CartCreateSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            'user',
        )
