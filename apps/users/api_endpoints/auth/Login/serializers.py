from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from apps.users.models import User


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    def get_tokens(self, user):
        phone_number = user.get("phone_number")
        token = User.objects.get(phone_number=phone_number).tokens
        return token

    class Meta:
        model = User
        fields = ["phone_number", "password", "tokens"]

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        print(phone_number)
        password = attrs.get("password")
        user = authenticate(phone_number=phone_number, password=password)
        print(user)
        if not user:
            raise AuthenticationFailed({"message": "Phone number or password is not correct"})
        if not user.is_active:
            raise AuthenticationFailed({"message": "Account disabled"})

        data = {
            "phone_number": user.phone_number,
        }
        return data
