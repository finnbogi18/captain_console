from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from accounts.models import Profile, SearchHistory
from forms import UserCreationForm
from django.shortcuts import render, redirect
from accounts.forms.profile_form import ProfileForm, UserForm
from django.contrib.auth import login

from products.models import Product


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('accounts-login')
    return render(request, 'accounts/register.html', {
        'form': UserCreationForm()
    })


@login_required
def edit(request):
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
    return render(request, 'accounts/edit.html', context)


@login_required
def profile(request):
    context = {'accounts': Profile.objects.all(),
               'searches': User.objects.get(id=request.user.id).searchhistory_set.order_by('-date')}
    return render(request, 'accounts/profile.html', context)


@login_required
def search_history(request):
    context = {'accounts': Profile.objects.all(),
               'searches': User.objects.get(id=request.user.id).searchhistory_set.order_by('-date')}

    return render(request, 'accounts/searchhistory.html', context)


@login_required
def clear_search(request):
    SearchHistory.objects.filter(user=request.user).delete()
    return redirect ('accounts-profile')
