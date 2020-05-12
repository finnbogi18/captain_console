from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.utils import timezone
from django_countries.fields import CountryField


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
        return f"{self.id} - {self.user.username}"

    def get_order_total_price(self):
        total = 0
        for item in self.items.all():
            total += item.get_item_total_price()

        return total

    def confirm_order(self):
        self.ordered = True


class OrderContactInfo(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = CountryField()
    postal_code = models.CharField(max_length=255)

    def __str__(self):
        return f"Order id: {self.order.id}, Owner: {self.first_name} {self.last_name}"


class OrderPaymentInfo(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=19)
    cardholder_name = models.CharField(max_length=255)
    cvv = models.IntegerField()
