from rest_framework.generics import ListAPIView

from apps.wishlist.models import WishList

from .serializers import WishlistAllSerializer


class WishListAllView(ListAPIView):
    serializer_class = WishlistAllSerializer
    queryset = WishList.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)


__all__ = ["WishListAllView"]
