from rest_framework.generics import ListAPIView

from apps.order.api_endpoints.cart_item.CartItemList.serializers import \
    CartItemListSerializer
from apps.order.models import CartItem


class CartItemList(ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemListSerializer


__all__ = ['CartItemList']
