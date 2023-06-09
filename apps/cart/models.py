from django.db.models import (
    CASCADE,
    ForeignKey,
    PositiveIntegerField,
    BooleanField,
)

from apps.common.models import TimeStampedModel


class Cart(TimeStampedModel):
    user = ForeignKey("users.User", CASCADE, "cart", verbose_name="User")
    is_ordered = BooleanField(default=False)

    class Meta:
        db_table = "cart"
        verbose_name_plural = "Carts"

    @property
    def total_price(self):
        s = 0
        for cart in self.cartitem_set.all():
            for product in cart.product.all():
                s += product.sell_price
        return s

    def __str__(self):
        return f" cart created by {self.user.username}"


class CartItem(TimeStampedModel):
    cart = ForeignKey("cart.Cart", CASCADE, "cart_items", verbose_name="Cart")
    product = ForeignKey("product.Product", CASCADE, "cart_item", verbose_name="Product")
    quantity = PositiveIntegerField(default=1, verbose_name="Quantity")

    def __str__(self):
        return f"{self.cart.user.username} - {self.product.name}"

    def incerement_quantity(self, val):
        self.quantity += val
        self.product.quantity -= val
        self.product.save()
        self.save()

    def decrement_quantity(self, val):
        self.quantity -= val
        self.product.quantity += val
        if self.quantity == 0:
            self.delete()
        else:
            self.save()

    class Meta:
        unique_together = ["cart", "product"]
        db_table = "cart_item"
        verbose_name = "CartItem"
        verbose_name_plural = "MyCartItems"

    @classmethod
    def add_product(cls, cart, product):
        if product.quantity > 0:
            cart_item, created = cls.objects.get_or_create(cart=cart, product=product)
            if created:
                cart_item.decrement_quantity()
        else:
            raise Exception("Product is out of stock.")

    def save(self, *args, **kwargs):
        if self.pk:
            orig = CartItem.objects.get(pk=self.pk)
            if orig.quantity != self.quantity:
                diff = self.quantity - orig.quantity
                self.product.quantity -= diff
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)
