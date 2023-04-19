from django.contrib import admin

from apps.cart.models import Cart, CartItem

admin.site.register([Cart, CartItem])
