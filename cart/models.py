from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.utils import timezone
from django_countries.fields import CountryField

MONTHS_CHOICES= (
    ("01", "01"),
    ("02", "02"),
    ("03", "03"),
    ("04", "04"),
    ("05", "05"),
    ("06", "06"),
    ("07", "07"),
    ("08", "08"),
    ("09", "09"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12")
)

YEAR_CHOICES = (
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024'),
    ('2025', '2025'),
    ('2026', '2026'),
    ('2027', '2027'),
    ('2028', '2028'),

)


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
    dismissed = models.BooleanField(default=False)

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
    cvc = models.CharField(max_length=3)
    expiry_month = models.CharField(
        max_length=2,
        choices=MONTHS_CHOICES,
        default='01'
    )
    expiry_year = models.CharField(
        max_length=4,
        choices=YEAR_CHOICES,
        default='1'
    )