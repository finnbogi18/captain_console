from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from products.models import Product


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'products/index.html', context)


def get_product_by_id(request, id):
    return render(request, 'products/product_details.html', {
            'product': get_object_or_404(Product, pk=id)
    })