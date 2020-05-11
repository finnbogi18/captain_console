from django.contrib import admin
from cart.models import OrderItem, Order, OrderContactInfo


class OrderAdmin(admin.ModelAdmin):
    pass


class OrderItemAdmin(admin.ModelAdmin):
    pass


class OrderContactInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(OrderContactInfo)

