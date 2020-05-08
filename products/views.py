from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from products.models import Product, ProductCategory, Manufacturer
from accounts.models import add_history


def is_valid_queryparam(param):
    return param != '' and param is not None

def index(request):
    qs = Product.objects.all()
    categories = ProductCategory.objects.all()
    manufacturers = Manufacturer.objects.all()
    product_search = request.GET.get('product-search')
    category = request.GET.get('category')
    manufacturer = request.GET.get('manufacturer')
    if is_valid_queryparam(product_search):
        current_user = request.user
        add_history(product_search,current_user)
        qs = qs.filter(name__icontains=product_search)

    if is_valid_queryparam(category) and category != 'Choose...':
        qs = qs.filter(category__name=category)

    if is_valid_queryparam(manufacturer) and manufacturer != 'Choose...':
        qs = qs.filter(manufacturer__name=manufacturer)

    context = {
        'queryset': qs,
        'categories': categories,
        'manufacturers': manufacturers
    }
    return render(request, 'products/index.html', context)


def get_product_by_id(request, id):
    return render(request, 'products/product_details.html', {
            'product': get_object_or_404(Product, pk=id)
    })
