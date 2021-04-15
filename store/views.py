from django.shortcuts import render
from .models import Category, Banner, SubCategory, LocalGroceryImage, Product, Shop, Campaign, Offer, Brand

# Create your views here.


def homeView(request):
    campaigns, offers, shops = None, None, None
    categories = Category.objects.all()
    shop_obj = Shop.objects.all()
    campaign_obj = Campaign.objects.all()
    offer_obj = Offer.objects.all()
    brands = Brand.objects.all().order_by("-id")

    if len(shop_obj) > 0:
        shops = Shop.objects.all().order_by("-id")[:6]
    if len(campaign_obj) > 0:
        campaigns = Campaign.objects.all().order_by("-id")[0]
    if len(offer_obj) > 0:
        offers = Offer.objects.all().order_by("-id")[0]

    banners, local_grocery_images, products, show_categories = None, None, None, None
    subcategories = SubCategory.objects.all()
    local_grocery_obj = LocalGroceryImage.objects.all()
    product_obj = Product.objects.all()
    show_category_obj = Category.objects.all()
    all_products = Product.objects.all().order_by("-id")

    if len(Banner.objects.all()) > 0:
        banners = Banner.objects.all().order_by("-id")[:6]
    if len(local_grocery_obj) > 0:
        local_grocery_images = LocalGroceryImage.objects.all().order_by(
            "-id")[:2]
    if len(product_obj) > 0:
        products = Product.objects.all().order_by("-id")[:6]
    if len(show_category_obj) > 0:
        show_categories = Category.objects.all()[:6]

    context = {
        "categories": categories,
        "shops": shops,
        "banners": banners,
        "subcategories": subcategories,
        "local_grocery_images": local_grocery_images,
        "products": products,
        "show_categories": show_categories,
        "campaigns": campaigns,
        "offers": offers,
        "all_products": all_products,
        "brands": brands
    }
    return render(request, 'store/home.html', context)


def shop_page(request):
    return render(request, 'shop.html')
