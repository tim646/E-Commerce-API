from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.product.models import ProductReview
from .serializers import ProductReviewUpdateSerializer


class ProductReviewUpdateView(UpdateAPIView):
    serializer_class = ProductReviewUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "product_id"

    def get_queryset(self):
        return ProductReview.objects.all()

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
