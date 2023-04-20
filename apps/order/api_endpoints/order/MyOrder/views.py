from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.order.api_endpoints.order.MyOrder.filters import IsOwnerFilterBackend
from apps.order.api_endpoints.order.MyOrder.serializers import MyOrderListSerializer
from apps.order.models import Order


class MyOrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = MyOrderListSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    filter_backends = [IsOwnerFilterBackend, DjangoFilterBackend]
    filterset_fields = ["payment_method", "status"]
