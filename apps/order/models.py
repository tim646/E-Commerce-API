from django.db.models import (CASCADE, CharField, DecimalField, ForeignKey,
                              OneToOneField, PositiveIntegerField)

from apps.common.models import TimeStampedModel
from apps.order.choices import OrderStatusChoice, PaymentMethodChoice


class Cart(TimeStampedModel):
    user = ForeignKey("users.User", CASCADE, "carts", verbose_name='User')

    class Meta:
        db_table = "cart"
        verbose_name_plural = "Carts"


class CartItem(TimeStampedModel):
    cart = ForeignKey("order.Cart", CASCADE, "cart_items", verbose_name='Cart')
    product = ForeignKey("product.Product", CASCADE, "cart_item", verbose_name='Product')
    quantity = PositiveIntegerField(default=1, verbose_name="Quantity")

    def __str__(self):
        return f"{self.cart.user.username} - {self.product.name}"

    def incerement_quantity(self):
        self.quantity += 1
        self.save()

    def decrement_quantity(self):
        self.quantity -= 1
        if self.quantity == 0:
            self.delete()
        else:
            self.save()

    class Meta:
        unique_together = ["cart", "product"]
        db_table = "cart_item"
        verbose_name = "CartItem"
        verbose_name_plural = "CartItems"

    @classmethod
    def add_product(cls, cart, product):
        cart_item, created = cls.objects.get_or_create(cart=cart, product=product)
        if created:
            cart_item.decrement_quantity()


class Payment(TimeStampedModel):
    order = ForeignKey("order.Order", CASCADE, verbose_name='Order')
    amount = DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')

    class Meta:
        db_table = "payment"


class Order(TimeStampedModel):
    user = ForeignKey("users.User", CASCADE, verbose_name='Order')
    payment_method = CharField(max_length=24, choices=PaymentMethodChoice.choices, verbose_name='Payment Method')
    status = CharField(choices=OrderStatusChoice.choices, default=OrderStatusChoice.PENDING, verbose_name='Status')
    cart = OneToOneField("order.Cart", CASCADE, verbose_name='Cart')
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
