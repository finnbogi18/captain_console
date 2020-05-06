from accounts.models import Profile
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
               'search': user.searchhistory_set.filter(user=request.user).all()}
    return render(request, 'accounts/profile.html', context)