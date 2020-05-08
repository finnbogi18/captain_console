from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from accounts.models import Profile, SearchHistory
from forms import UserCreationForm
from django.shortcuts import render, redirect
from accounts.forms.profile_form import ProfileForm

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
@login_required
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
@login_required
def profile(request):
    context = {'accounts': Profile.objects.all(),
               'searches': User.objects.get(id=request.user.id).searchhistory_set.all()}
    return render(request, 'accounts/profile.html', context)

@login_required
def search_history(request):
    context = {'accounts': Profile.objects.all(),
               'searches': User.objects.get(id=request.user.id).searchhistory_set.all()}
    return render(request, 'accounts/searchhistory.html',context)