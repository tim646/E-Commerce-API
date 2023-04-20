from django.views.generic import UpdateView

from apps.cart.api_endpoints.cart_item.CartItemUpdate.serializers import CartItemUpdateSerializer
from apps.cart.models import CartItem
from apps.common.permissions import IsOwnerOrReadOnly


class CartItemUpdateView(UpdateView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemUpdateSerializer
    permission_class = [IsOwnerOrReadOnly]


__all__ = ["CartItemUpdateView"]
