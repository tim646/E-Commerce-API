from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.cart.api_endpoints.cart_item.CartItemDetail.serializers import CartItemDetailSerializer
from apps.cart.models import CartItem


class CartItemDetailView(RetrieveAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemDetailSerializer
    permission_classes = [
        IsAuthenticated,
    ]


__all__ = ["CartItemDetailView"]
