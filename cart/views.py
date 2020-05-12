from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Order, OrderItem, OrderContactInfo
from products.models import Product
from django.utils import timezone
from django.db.models import F
from django.contrib.auth.decorators import login_required
from cart.forms.contact_form import ContactInformationForm
from django.contrib.auth.models import User


def index(request):
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    context = {
        'orders': order_qs
    }
    return render(request, 'cart/index.html', context)


def checkout(request):
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order = order_qs[0]
    order_contact = OrderContactInfo.objects.get_or_create(order=order)
    order_contact_test = order_contact[0]
    context = {
        'orders':order_qs,
        'contact_form': ContactInformationForm(instance=order_contact_test)
    }
    if request.method == 'POST':
        contact_form = ContactInformationForm(instance=order_contact_test, data=request.POST)
        if contact_form.is_valid():
            contact_info = contact_form.save(commit=False)
            contact_info.save()
            return render(request, 'cart/checkout.html', context)

    return render(request, 'cart/checkout.html', context)


@login_required
def add_to_cart(request, slug):
    print('im in add to cart')
    item = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity = F('quantity') + 1
            order_item.save()
        else:
            order.items.add(order_item)
        return redirect('product-index')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, order_date=ordered_date)
        order.items.add(order_item)
    return redirect('cart-index')


@login_required
def remove_one_item_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item = OrderItem.objects.get(
        item=item,
        user=request.user,
        is_ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            if order_item.quantity > 1:
                order_item.quantity = F('quantity') - 1
                order_item.save()
            else:
                order.items.remove(order_item)

    return redirect('cart-index')


@login_required
def remove_all_item_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                is_ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            return redirect('cart-index')

    return redirect('cart-index')
