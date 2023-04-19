from rest_framework.generics import DestroyAPIView

from apps.order.api_endpoints.order.OrderDelete.serializers import \
    OrderDeleteSerializer
from apps.order.models import Order


class OrderDeleteView(DestroyAPIView):
    queryset = Order
    serializer_class = OrderDeleteSerializer


__all__ = ["OrderDeleteView"]
