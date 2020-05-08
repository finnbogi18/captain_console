from django.db import models
from django.urls import reverse


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_add_to_cart_url(self):
        return reverse('add-to-cart', kwargs={
            'slug': self.slug
        })

    def get_remove_one_cart(self):
        return reverse('remove-one-cart', kwargs={
            'slug': self.slug
        })


class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image

