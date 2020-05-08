from django.contrib import admin
from products.models import Product, ProductCategory, ProductImage, Manufacturer


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product)


class ProductCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductCategory)


class ProductImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductImage)


class ProductManufacturerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Manufacturer)
