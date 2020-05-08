from django.shortcuts import render, redirect


def index(request):
    product_search = request.GET.get('product-search')
    if product_search != '' and product_search is not None:
        return redirect('product-index')
    return render(request, 'home/index.html')
