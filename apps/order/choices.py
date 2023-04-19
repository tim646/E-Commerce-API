from django.db.models import TextChoices


class OrderStatusChoice(TextChoices):
    PENDING = "P", "Pending"
    CONFIRMED = "C", "Confirmed"
    SHIPPED = "S", "Shipped"
    DELIVERED = "D", "Delivered"
    CANCELLED = "X", "Cancelled"


class PaymentMethodChoice(TextChoices):
    CREDIT_CARD = 'CC', 'Credit Card'
    DEBIT_CARD = 'DC', 'Debit Card'
    PAYPAL = 'PP', 'PayPal'
    GOOGLE_PAY = 'GP', 'Google Pay'
    APPLE_PAY = 'AP', 'Apple Pay'
    BANK_TRANSFER = 'BT', 'Bank Transfer'
    CASH_ON_DELIVERY = 'COD', 'Cash on Delivery'
    BITCOIN = 'BTC', 'Bitcoin'
    ETHEREUM = 'ETH', 'Ethereum'
    CASH = 'CA', 'Cash'
