from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.wishlist.models import WishList


class WishListDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, product_id):
        saved = get_object_or_404(WishList, product_id=product_id, user=request.user)
        saved.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


__all__ = ["WishListDeleteView"]
