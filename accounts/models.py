from django.db import models


"""class ProductCategory(models.Model):
    name = models.CharField(max_length=255)"""


class Account(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    #TODO: skoða þetta!

    """description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()
    manufacturer = models.CharField(max_length=255)"""


class SearchHistory(models.Model):
    search = models.CharField(max_length=999)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
