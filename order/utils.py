import os
import datetime

from order.models import *
from Cart.cart import Cart

def checkout(request, first_name, last_name, email, address, zipcode, place):
    order = Order(first_name=first_name, last_name=last_name, email=email, address=address, zipcode=zipcode, place=place)
    
    order.save()
    
    cart = Cart(request)
    
    for item in cart:
        OrderItems.objects.create(order=order, product=item['product'], price = item['price'], quantity=item['quantity'])
    
    return order.id