from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Order, OrderItem
from products.models import Product
from django.utils import timezone


# Create your views here.

def index(request):
    return render(request, 'cart/index.html')


def add_to_cart(request, id):
    item = get_object_or_404(Product, id=id)
    order_item = OrderItem.objects.create(item=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, order_date=ordered_date)
        order.items.add(order_item)
    return redirect('home-index')
