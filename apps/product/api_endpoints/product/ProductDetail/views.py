from rest_framework.generics import RetrieveAPIView

from apps.product.models import Product

from .serializers import ProductDetailSerializer


class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = "id"


__all__ = ["ProductDetailView"]
