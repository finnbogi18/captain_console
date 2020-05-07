from django.contrib.auth.models import User

from accounts.models import Profile, SearchHistory
from forms import UserCreationForm
from django.shortcuts import render, redirect
from accounts.forms.profile_form import ProfileForm
from accounts.forms.search_form import SearchForm

# Create your views here.
from products.models import Product


def index(request):
    return render(request, 'accounts/index.html')

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts-login')
    return render(request, 'accounts/register.html', {
        'form': UserCreationForm()
    })

def edit(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('accounts-profile')
    return render(request, 'accounts/edit.html', {
    'form': ProfileForm(instance=profile)
    })

def profile(request):
    context = {'accounts': Profile.objects.all(),
               'searches': User.objects.get(id=request.user.id).searchhistory_set.all()}
    return render(request, 'accounts/profile.html', context)

def add_history(request):
    profile = SearchHistory.objects.filter(user=request.user).first().user_id
    if request.method == 'POST':
        form = SearchForm(data=request.POST)
        if form.is_valid():
            search = form.save(commit=False)
            search.user = request.user
            search.save()
            return redirect('accounts-profile')
    else:
        form = SearchForm()
    return render(request, 'base.html',{
        'form': form
    })

def search_history(request):
    context = {'accounts': Profile.objects.all(),
               'searches': User.objects.get(id=request.user.id).searchhistory_set.all()}
    return render(request, 'accounts/searchhistory.html',context)