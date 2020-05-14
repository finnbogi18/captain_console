from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from accounts.models import Profile, SearchHistory
from cart.models import Order, OrderContactInfo, OrderPaymentInfo
from forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms.profile_form import ProfileForm, UserForm
from django.contrib import messages


def login(request):
    """This is the login page"""
    return render(request, 'accounts/login.html')


def register(request):
    """This is to open up forms to sign up to the page"""
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('accounts-login')
        else:
            messages.warning(request, 'Invalid information in sign up!')
    return render(request, 'accounts/register.html', {
        'form': UserCreationForm()
    })


@login_required
def edit(request):
    """This is to edit the profile"""
    user = User.objects.filter(id=request.user.id).first()
    profile = Profile.objects.filter(user=user).first()
    context = {
        'profile_form': ProfileForm(instance=profile),
        'user_form': UserForm(instance=user)
    }
    if request.method == 'POST':
        user_form = UserForm(instance=user, data=request.POST)
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            user_temp = user_form.save(commit=False)
            profile_temp = profile_form.save(commit=False)
            profile_temp.save()
            user_temp.save()
            return redirect('accounts-profile')
        else:
            messages.warning(request, 'Invalid information!')
    return render(request, 'accounts/edit.html', context)


@login_required
def profile(request):
    """This is to open the profile html"""
    context = {'accounts': Profile.objects.all(),
               'searches': User.objects.get(id=request.user.id).searchhistory_set.order_by('-date'),
               'orders': Order.objects.filter(user_id=request.user.id, ordered=True)
               }
    return render(request, 'accounts/profile.html', context)


@login_required
def search_history(request):
    """This is to view the whole search history, the client is able to access this if he has more then 5 searches"""
    context = {'accounts': Profile.objects.all(),
               'searches': User.objects.get(id=request.user.id).searchhistory_set.order_by('-date')}

    return render(request, 'accounts/searchhistory.html', context)


@login_required
def clear_search(request):
    """This clears the search history when the client presses "clear search" """
    SearchHistory.objects.filter(user=request.user).delete()
    return redirect('accounts-profile')


@login_required
def order_history(request):
    """This opens up the orderhistory. If the client has more than 5 orders he is able to open this"""
    context = {'accounts': Profile.objects.all(),
               'orders': Order.objects.filter(user_id=request.user.id, ordered=True),
    }
    return render(request, 'accounts/orderhistory.html', context)


@login_required
def order_id(request, id):
    """this is to show the order from the profile app. We need a specific number which is the order ID"""
    order = get_object_or_404(Order, pk=id)
    if order.user_id == request.user.id:
        context = {
            'order': order,
            'order_contact': OrderContactInfo.objects.filter(order_id=id).first,
            'order_payment': OrderPaymentInfo.objects.filter(order_id=id).first,
        }
        return render(request, 'accounts/order.html', context)
    else:
        return redirect('accounts-profile')
