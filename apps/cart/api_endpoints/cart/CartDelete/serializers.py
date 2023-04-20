from rest_framework.serializers import ModelSerializer

from apps.cart.models import Cart


class CartDeleteSerializer(ModelSerializer):
    model = Cart
    fields = "user"
