from django.views.generic import UpdateView

from apps.cart.api_endpoints.cart_item.CartItemUpdate.serializers import \
    CartItemUpdateSerializer
from apps.cart.models import CartItem


class CartItemUpdateView(UpdateView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemUpdateSerializer


__all__ = ['CartItemUpdateView']
