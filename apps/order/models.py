from django.db.models import (CASCADE, CharField, DateTimeField, DecimalField,
                              ForeignKey, Model, OneToOneField,
                              PositiveIntegerField)

from apps.common.models import TimeStampedModel
from apps.order.choices import OrderStatusChoice


class Cart(TimeStampedModel):
    user = ForeignKey("users.User", CASCADE, "carts")
    product = ForeignKey("product.Product", CASCADE, "cart")

    class Meta:
        unique_together = ["user", "product"]
        db_table = "cart"
        verbose_name_plural = "Carts"


class CartItem(TimeStampedModel):
    cart = ForeignKey("order.Cart", CASCADE, "cart_items")
    product = ForeignKey("product.Product", CASCADE, "cart_item")
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
        db_table = "cart_item"
        verbose_name = "CartItem"
        verbose_name_plural = "CartItems"

    @classmethod
    def add_product(cls, cart, product):
        cart_item, created = cls.objects.get_or_create(cart=cart, product=product)
        if created:
            cart_item.decrement_quantity()


class Payment(Model):
    order = ForeignKey("order.Order", CASCADE)
    amount = DecimalField(max_digits=10, decimal_places=2)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "payment"


class Order(TimeStampedModel):
    user = ForeignKey("users.User", CASCADE)
    cart = OneToOneField("order.Cart", CASCADE)
    status = CharField(choices=OrderStatusChoice.choices, default=OrderStatusChoice.PENDING)

    class Meta:
        db_table = "order"


class ShippingAddress(TimeStampedModel):
    user = ForeignKey("users.User", CASCADE)
    order = OneToOneField("order.Order", CASCADE)
    name = CharField(max_length=255)
    address = CharField(max_length=255)
    city = CharField(max_length=255)
    state = CharField(max_length=255)
    zip_code = CharField(max_length=10)

    class Meta:
        db_table = "shipping"
