from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer
from rest_framework.generics import GenericAPIView

from apps.users.models import User


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)



        return Response({"success": True, 'data': serializer.data}, status=status.HTTP_200_OK)


__all__ = ["LoginView"]
