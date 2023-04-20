from rest_framework.generics import DestroyAPIView

from apps.cart.api_endpoints.cart_item.CartItemDelete.serializers import CartItemDeleteSerializer
from apps.cart.models import CartItem
from apps.common.permissions import IsOwnerOrReadOnly


class CartItemDeleteView(DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemDeleteSerializer
    permission_classes = [IsOwnerOrReadOnly]


__all__ = ["CartItemDeleteView"]
