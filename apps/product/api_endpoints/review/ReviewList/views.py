from rest_framework.generics import ListAPIView
from .serializers import ProductReviewListSerializer

from apps.product.models import ProductReview


class ProductReviewListView(ListAPIView):
    serializer_class = ProductReviewListSerializer
    lookup_field = "product_id"

    def get_queryset(self):
        product_id = self.kwargs.get(self.lookup_field)
        return ProductReview.objects.filter(product_id=product_id)


__all__ = ["ProductReviewListView"]
