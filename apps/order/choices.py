from django.db.models import TextChoices


class OrderStatusChoice(TextChoices):
    PENDING = "P", "Pending"
    CONFIRMED = "C", "Confirmed"
    SHIPPED = "S", "Shipped"
    DELIVERED = "D", "Delivered"
    CANCELLED = "X", "Cancelled"
