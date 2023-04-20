from rest_framework.generics import CreateAPIView

from apps.cart.api_endpoints.cart.CartCreate.serializers import CartCreateSerializer
from apps.cart.models import Cart


class CartCreateView(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializer


__all__ = ["CartCreateView"]
