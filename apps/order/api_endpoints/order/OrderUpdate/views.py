from rest_framework.generics import UpdateAPIView

from apps.order.api_endpoints.order.OrderUpdate.serializers import \
    OrderUpdateSerializer
from apps.order.models import Order


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer


__all__ = ["OrderUpdateView"]
