from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination

from django_filters.rest_framework import DjangoFilterBackend

from apps.product.models import Product

from .serializers import ProductListSerializer, RelatedProductListSerializer

from .filters import ProductFilter


# Create a view class
class ProductListView(ListAPIView):
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = Product.objects.all()
    filterset_class = ProductFilter


class RelatedProductListView(ListAPIView):
    serializer_class = RelatedProductListSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        product_id = self.kwargs["product_id"]
        product = Product.objects.get(id=product_id)
        category = product.category
        features = product.features.all()
        queryset = (
            Product.objects.filter(Q(category=category) | Q(features__in=features)).distinct().exclude(id=product_id)
        )
        return queryset


class YouMayLikeProductListView(ListAPIView):
    serializer_class = RelatedProductListSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        product_id = self.kwargs["product_id"]
        product = Product.objects.get(id=product_id)
        category = product.category
        design = product.design
        queryset = Product.objects.filter(Q(category=category) & Q(design__icontains=design)).exclude(id=product_id)
        return queryset


__all__ = ["ProductListView", "RelatedProductListView", "YouMayLikeProductListView"]
