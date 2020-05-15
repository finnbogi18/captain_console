from django.urls import path
from . import views
from cart.views import add_to_cart, remove_one_item_from_cart

urlpatterns = [
    path('', views.index, name="product-index"),
    path('<int:id>', views.get_product_by_id, name="product_details"),
    path('<slug>', add_to_cart, name="add-to-cart"),
    path('<slug>/remove-one', remove_one_item_from_cart, name="remove-one-cart"),
]