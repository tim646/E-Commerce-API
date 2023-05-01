from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductReviewCreateSerializer


class ProductReviewCreateView(CreateAPIView):
    serializer_class = ProductReviewCreateSerializer
    permission_classes = [IsAuthenticated]


__all__ = ["ProductReviewCreateView"]
