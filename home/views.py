from django.shortcuts import render
from products.models import Product

# Create your views here.


def index(request):

    products_newarrival = Product.objects.all().order_by('pk')[::-1][:4]

    context = {
        'product_newarrival': products_newarrival
    }
    return render(request, 'home/index.html', context)
