from django.db.models import (CASCADE, CharField, DecimalField, ForeignKey,
                              OneToOneField)

from apps.common.models import TimeStampedModel
from apps.order.choices import OrderStatusChoice, PaymentMethodChoice


class Payment(TimeStampedModel):
    order = ForeignKey("order.Order", CASCADE, verbose_name='Order')
    amount = DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')

    class Meta:
        db_table = "payment"


class Order(TimeStampedModel):
    user = ForeignKey("users.User", CASCADE, verbose_name='Order')
    payment_method = CharField(max_length=24, choices=PaymentMethodChoice.choices, verbose_name='Payment Method')
    status = CharField(choices=OrderStatusChoice.choices, default=OrderStatusChoice.PENDING, verbose_name='Status')
    cart = OneToOneField("cart.Cart", CASCADE, verbose_name='Cart')
    shipping_cost = DecimalField(max_digits=10, decimal_places=2)
    total = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "order"


class ShippingAddress(TimeStampedModel):
    user = ForeignKey("users.User", CASCADE, verbose_name='User')
    order = OneToOneField("order.Order", CASCADE, verbose_name='Order')
    name = CharField(max_length=255, verbose_name='Name')
    address = CharField(max_length=255, verbose_name='Address')
    city = CharField(max_length=255, verbose_name='City')
    state = CharField(max_length=255, verbose_name='State')
    zip_code = CharField(max_length=10, verbose_name='Zip Code')

    class Meta:
        db_table = "shipping"
