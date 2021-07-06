from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


from products.models import Product
from .models import Coupon
from .forms import CouponForm
from .views import add_coupon




def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    coupon_id = request.session.get('coupon_id', int())
    code = None
    amount = 0
    

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })
    
    
 
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0   

    old_total= total    
    try:
        code = Coupon.objects.get(id=coupon_id)
        if code !=None:           
            
            amount = total*code.amount
            total = total - amount            
    except Coupon.DoesNotExist:
        code = None

    grand_total = delivery + total 
    
              

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'code': code,
        'amount':amount,        
        'old_total':old_total,
    }

    return context
