from django.contrib import admin
from cart.models import OrderItem, Order

class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order)


class OrderItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(OrderItem)

