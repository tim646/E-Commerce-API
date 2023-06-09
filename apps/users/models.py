import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken

from apps.common.models import TimeStampedModel
from apps.users.managers import SoftDeleteUserManager


# Create your models here.
class User(AbstractUser, TimeStampedModel):
    phone_number = PhoneNumberField(region="UZ", unique=True, null=True, verbose_name="Phone number")

    first_name = None
    last_name = None
    full_name = models.CharField(max_length=32, null=True, blank=True, verbose_name="Full name")

    uuid = models.UUIDField("UUID", unique=True, default=uuid.uuid4, editable=False, db_index=True)
    username = models.CharField(
        "Username",
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        null=True,
        validators=[UnicodeUsernameValidator()],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )

    is_deleted = models.BooleanField("Is deleted", default=False)
    is_active = models.BooleanField("Is active", default=True)
    email = models.EmailField("Email", unique=True)
    address = models.CharField("Address", max_length=255, null=True, blank=True)

    objects = SoftDeleteUserManager()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["username", "password"]  # type: ignore

    def __str__(self):
        if self.username:
            return self.username
        if self.phone_number:
            return str(self.phone_number)
        if self.email:
            return self.email

    def prepare_to_delete(self):
        self.is_deleted = True
        for x in ["email", "username", "phone_number"]:
            if getattr(self, x):
                setattr(self, x, f"DELETED_{self.id}_{getattr(self, x)}")
        self.save()

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
