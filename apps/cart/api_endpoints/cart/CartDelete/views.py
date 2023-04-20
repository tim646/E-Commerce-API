from rest_framework.generics import DestroyAPIView

from apps.cart.api_endpoints.cart.CartDelete.serializers import CartDeleteSerializer
from apps.cart.models import Cart


class CartDeleteView(DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartDeleteSerializer


__all__ = ["CartDeleteView"]
