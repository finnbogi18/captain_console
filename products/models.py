from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()
    manufacturer = models.CharField(max_length=255)


class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    # TODO: ADD MORE MODELS.
