from rest_framework.generics import CreateAPIView

from apps.users.models import User

from .serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


__all__ = ["RegisterView"]
