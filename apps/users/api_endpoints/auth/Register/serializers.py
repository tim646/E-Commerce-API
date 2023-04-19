from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.users.models import User


class RegisterSerializer(ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["phone_number", "username", "email", "password1", "password2"]

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        password1 = attrs.get("password1")
        password2 = attrs.get("password2")
        if password1 != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})
        user_qs = User.objects.filter(phone_number=phone_number)
        if user_qs.exists():
            raise serializers.ValidationError({"phone_number": "This phone number has already been registered."})
        return attrs

    def create(self, validated_data):
        phone_number = validated_data.get("phone_number")
        username = validated_data.get("username")
        email = validated_data.get("email")
        password = validated_data.get("password1")
        user_obj = User(
            phone_number=phone_number,
            username=username,
            email=email,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data
