from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.utils import timezone


class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_item_total_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(default=timezone.now)
    order_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_order_total_price(self):
        total = 0
        for item in self.items.all():
            total += item.get_item_total_price()

        return total
