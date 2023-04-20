from rest_framework.generics import CreateAPIView

from apps.common.permissions import IsOwnerOrReadOnly
from apps.order.api_endpoints.order.OrderCreate.serializers import OrderCreateSerializer
from apps.order.models import Order


class OrderCreateView(CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Order.objects.all()


__all__ = ["OrderCreateView"]
