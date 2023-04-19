from django.contrib import admin

from apps.order.models import Cart, CartItem, Order, Payment, ShippingAddress

admin.site.register([Cart, CartItem, Payment, Order, ShippingAddress])
