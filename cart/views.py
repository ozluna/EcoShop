from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_cart(request):
    # A view renders the cart contents page
    return render(request, 'cart/cart.html')


def add_cart(request, item_id):
    # Add specified item to the cart

    product = get_object_or_404(Product,pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to{cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to you cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    # Adjust the items in cart
    product = get_object_or_404(Product,pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'{cart[item_id]} sucessfully removed')

    request.session['cart'] = cart
    return redirect(reverse(view_cart))


def remove_cart(request, item_id):
    # Remove the items from cart
    try:
        product = get_object_or_404(Product,pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        request.session['cart'] = cart
        messages.success(request, f'{cart[item_id]} sucessfully removed')
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request,f'Error removing the item {e}')
        return HttpResponse(status=500)
