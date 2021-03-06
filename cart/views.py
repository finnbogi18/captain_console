from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Order, OrderItem, OrderContactInfo, OrderPaymentInfo
from products.models import Product
from django.utils import timezone
from django.db.models import F
from django.contrib.auth.decorators import login_required
from cart.forms.contact_form import ContactInformationForm
from cart.forms.payment_form import PaymentInformationForm
from django.contrib import messages


@login_required
def index(request):
    order_qs = Order.objects.filter(user=request.user, ordered=False, dismissed=False)
    context = {
        'orders': order_qs
    }
    return render(request, 'cart/index.html', context)


@login_required
def checkout(request):
    '''Renders the checkout phase and the
    contact information form.
    '''
    order_qs = Order.objects.filter(user=request.user, ordered=False, dismissed=False)
    order = order_qs[0]
    order_contact = OrderContactInfo.objects.get_or_create(order=order)
    order_contact_test = order_contact[0]
    context = {
        'orders': order_qs,
        'contact_form': ContactInformationForm(instance=order_contact_test)
    }
    if request.method == 'POST':
        contact_form = ContactInformationForm(instance=order_contact_test, data=request.POST)
        if contact_form.is_valid():
            contact_info = contact_form.save(commit=False)
            contact_info.save()
            return redirect('payment-index')
        else:
            messages.warning(request, 'Invalid contact information!')

    return render(request, 'cart/checkout.html', context)


@login_required
def payment(request):
    '''Renders the payment view and
    shows the payment information form.
    '''
    order_qs = Order.objects.filter(user=request.user, ordered=False, dismissed=False)
    order = order_qs[0]
    order_payment = OrderPaymentInfo.objects.get_or_create(order=order)
    order_payment_instance = order_payment[0]
    context = {
        'orders': order_qs,
        'payment_form': PaymentInformationForm(instance=order_payment_instance)
    }
    if request.method == 'POST':
        payment_form = PaymentInformationForm(instance=order_payment_instance, data=request.POST)
        if payment_form.is_valid():
            payment_info = payment_form.save(commit=False)
            payment_info.save()
            return redirect('review-index')
        else:
            messages.warning(request, 'Invalid Payment information.')

    return render(request, 'cart/payment.html', context)


@login_required
def review(request):
    '''Renders the review page with
    all the required information.
    '''
    order_qs = Order.objects.filter(user=request.user, ordered=False, dismissed=False)
    order_contact_qs = OrderContactInfo.objects.filter(order=order_qs[0])
    order_payment_qs = OrderPaymentInfo.objects.filter(order=order_qs[0])
    context = {
        'order': order_qs[0],
        'order_contact': order_contact_qs[0],
        'order_payment': order_payment_qs[0]
    }
    return render(request, 'cart/confirmation.html', context)


@login_required
def confirm_order(request):
    '''Marks the order as ordered and sets
    the ordered date to the current time.
    '''
    order_qs = Order.objects.filter(user=request.user, ordered=False, dismissed=False)
    order = order_qs[0]
    order.ordered = True
    order.order_date = timezone.now()
    order.save()
    messages.success(request, 'Order with the id {} was placed.'.format(order.id))
    return redirect('home-index')


@login_required
def add_to_cart(request, slug):
    '''Adds the item to the cart or increases the amount of
    that item in the cart.
    '''
    item = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user)
    order_qs = Order.objects.filter(user=request.user, ordered=False, dismissed=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity = F('quantity') + 1
            order_item.save()
            messages.success(request, 'Item was added to your cart.')
        else:
            order.items.add(order_item)
            messages.success(request, 'Item was added to your cart.')
        return redirect('product-index')
    else:  # Creates the order if this is the first item added into the cart.
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, order_date=ordered_date)
        order.items.add(order_item)
        messages.success(request, 'Item was added to your cart.')
    return redirect('product-index')


@login_required
def remove_one_item_from_cart(request, slug):
    '''Removes one item from the cart.
    '''
    item = get_object_or_404(Product, slug=slug)
    order_item = OrderItem.objects.get(
        item=item,
        user=request.user,
        is_ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False, dismissed=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            if order_item.quantity > 1:
                order_item.quantity = F('quantity') - 1
                order_item.save()
            else:
                order.items.remove(order_item)
                order_item.delete()
                if not order.items.filter(
                        user=request.user):  # checks if the cart is emptied and dismissed the order if so.
                    order.dismissed = True
                    order.save()

    return redirect('cart-index')
