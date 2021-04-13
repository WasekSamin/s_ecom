from django.shortcuts import render, HttpResponse


def home(request):
    try:
        return render(request, 'home.html')
    except:
        return HttpResponse("404 Not found")


def shop_page(request):
    return render(request, 'shop.html')