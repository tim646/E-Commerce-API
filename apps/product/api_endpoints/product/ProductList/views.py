from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from apps.product.models import Product
from .serializers import ProductListSerializer


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = ProductListSerializer


__all__ = ['ProductList']
