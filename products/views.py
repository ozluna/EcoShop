from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


# Create your views here.


def all_products(request):
    products = Product.objects.all()
    query = None
    category = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET('catergory').split(',')
            products = products.filter(category_name_in=categories)
            categories = Category.object.filter(category_name_in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please type product name to search")
                return redirect(reverse('products'))
            quieries = Q(name_icontains=query) | Q(description_icontains=query)
            products = products.filter(quieries)
    context = {
        'products': products,
        'search_term': query,
        'current categories': category,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
