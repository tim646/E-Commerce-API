from django.contrib import admin

from apps.order.models import Order, Payment, ShippingAddress

admin.site.register([Payment, Order, ShippingAddress])
