from django.db import models


class WishList(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="wishlist")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="wishlist")

    class Meta:
        verbose_name = "wishlist"
        verbose_name_plural = "wishlist"

    def __str__(self):
        return f"{self.user} - {self.product}"
