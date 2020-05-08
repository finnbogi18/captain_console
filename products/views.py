from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from products.models import Product


def index(request):
    qs = Product.objects.all()
    product_search = request.GET.get('product-search')
    print(product_search)
    if product_search != '' and product_search is not None:
        qs = qs.filter(name__icontains=product_search)
    context = {
        'queryset': qs
    }
    return render(request, 'products/index.html', context)


def get_product_by_id(request, id):
    return render(request, 'products/product_details.html', {
            'product': get_object_or_404(Product, pk=id)
    })
