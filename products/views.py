from django.shortcuts import render

# Create your views here.

consoles = [
    {'name': 'Nintendo 64',
     'price': 29.99},
    {'name': 'Gameboy',
     'price': 19.99}
]


def index(request):
    return render(request, 'products/index.html', context={ 'consoles': consoles})
