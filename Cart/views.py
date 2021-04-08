from django.shortcuts import render
from Cart.cart import *
# Create your views here.


def cart_details(request):
    cart = Cart(request)
   
    productString = ""
    
    for item in cart:
        product = item['product']
        b = "{'id':'%s','title':'%s','price':'%s','quantity':'%s', 'total_price':'%s'},"%(product.id, product.title, product.price, item['quantity'], item['total_price'])
        
        productString = productString + b
        
    context = {
        'cart': cart,
        'productString': productString,
        
    }
    
    return render(request, 'cart.html', context)