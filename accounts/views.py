from forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.

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

def profile(request):
    return render(request, 'accounts/profile.html')