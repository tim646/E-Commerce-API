from rest_framework.generics import RetrieveAPIView

from apps.product.models import Supplier

from .serializers import SupplierDetailForProductSerializer, SupplierSerializer


class SupplierDetailView(RetrieveAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    lookup_field = "id"


class SupplierDetailForProductView(RetrieveAPIView):
    serializer_class = SupplierDetailForProductSerializer
    queryset = Supplier.objects.all()
    lookup_field = "id"


__all__ = ["SupplierDetailForProductView", "SupplierDetailView"]
