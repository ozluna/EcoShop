from django.shortcuts import render, redirect, reverse
from django.contrib import messages


# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty at the moment")
        return redirect(reverse('products'))
    
    context = {
        'stripe_public_key': 'pk_live_51IqjPKCAbWLyaUT3nGLrvpQTRuhnVw9uqW1ASuBjsNM7nEZTNj6zkOzMCGP6loTcYfng23w6y8YQHnpY3r40jmT600395yHjGb',

    }
    return render(request,context)