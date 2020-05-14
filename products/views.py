from django.shortcuts import render, get_object_or_404
from products.models import Product, ProductCategory, Manufacturer
from accounts.models import add_history


def is_valid_queryparam(param):
    return param != '' and param is not None


def index(request):
    """This is the main function for the product view. It runs validations for queries
    and gets all of the data to send in as context to show on the webpage."""
    qs = Product.objects.all() #query set
    categories = ProductCategory.objects.all()
    manufacturers = Manufacturer.objects.all()
    product_search = request.GET.get('product-search')
    category = request.GET.get('category')
    manufacturer = request.GET.get('manufacturer')
    order_by = request.GET.get('order-by')
    search_string = '' # instanciates an empty string to be used in inside the if statement
    if is_valid_queryparam(product_search): # this checks if the query is valid and continues to manipulate the data depending on the query
        search_string = product_search
        current_user = request.user
        qs = qs.filter(name__icontains=product_search)
        if request.user.is_authenticated:
            add_history(product_search, current_user)

    if is_valid_queryparam(category) and category != 'Choose...': # filters by category
        qs = qs.filter(category__name=category)

    if is_valid_queryparam(manufacturer) and manufacturer != 'Choose...': # filters by manufacturer
        qs = qs.filter(manufacturer__name=manufacturer)

    if order_by == 'name-dec': # order by statements
        print('name dec')
        qs = qs.order_by('-name')
    elif order_by == 'name-ac':
        print('name ac')
        qs = qs.order_by('name')
    elif order_by == 'price-dec':
        print('price dec')
        qs = qs.order_by('-price')
    elif order_by == 'price-ac':
        print('price ac')
        qs = qs.order_by('price')


    context = { # puts everything into the context to send to the webpage
        'queryset': qs,
        'categories': categories,
        'manufacturers': manufacturers,
        'searchstring': search_string
    }
    return render(request, 'products/index.html', context)


def get_product_by_id(request, id):
    return render(request, 'products/product_details.html', {
            'product': get_object_or_404(Product, pk=id)
    })
