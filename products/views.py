from django.shortcuts import render
from products.models import Product


def index(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'products/index.html', context)
