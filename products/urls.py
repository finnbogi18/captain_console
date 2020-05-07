from django.urls import path
from . import views
from cart.views import add_to_cart

urlpatterns = [
    path('', views.index, name="product-index"),
    path('<int:id>', views.get_product_by_id, name="product_details"),
    path('cart/<int:id>', add_to_cart, name="add-to-cart ")
]