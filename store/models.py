from django.db import models

# Create your models here.


class Brand(models.Model):
    brand_slug = models.SlugField(unique=True, null=True, blank=True)
    title = models.CharField(max_length=120, unique=True)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

class Category(models.Model):
    cat_slug = models.SlugField(unique=True, null=True, blank=True)
    title = models.CharField(max_length=120, unique=True)
    img = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.title



class SubCategory(models.Model):
    sub_slug = models.SlugField(unique=True, null=True, blank=True)
    title = models.CharField(max_length=120, unique=True)
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title




class Shop(models.Model):
    shop_slug = models.SlugField(unique=True, null=True, blank=True)
    title = models.CharField(max_length=120, unique=True)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

class Slider(models.Model):
    slider_slug = models.SlugField(unique=True, null=True, blank=True)
    title = models.CharField(max_length=120, unique=True)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

class Campaign(models.Model):
    campaign_slug = models.SlugField(unique=True, null=True, blank=True)
    title = models.CharField(max_length=120, unique=True)
    img = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.title

class Offer(models.Model):
    offer_slug = models.SlugField(unique=True, null=True, blank=True)
    offer_title = models.CharField(max_length=120, unique=True)
    offer_img = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.offer_title


class Product(models.Model):
    product_slug = models.SlugField(null=True, blank=True)
    title = models.CharField(max_length=120)
    img = models.ImageField(upload_to="images/")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)
    isFavorite = models.BooleanField()
    market_price = models.IntegerField()
    sale_price = models.IntegerField()
    stock_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title


class Currency(models.Model):
    currency_name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.currency_name