from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination

from apps.product.models import Product

from .serializers import ProductListSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = ProductListSerializer


__all__ = ["ProductListView"]
