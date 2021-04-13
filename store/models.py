from django.db import models

# Create your models here.


class Brand(models.Model):
    title = models.CharField(max_length=120)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=120)
    img = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.title



class SubCategory(models.Model):
    title = models.CharField(max_length=120)
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title




class Shop(models.Model):
    title = models.CharField(max_length=120)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=120)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

class Campaign(models.Model):
    title = models.CharField(max_length=120)
    img = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.title

class Offer(models.Model):
    offer_title = models.CharField(max_length=120)
    offer_img = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.offer_title


class Product(models.Model):
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
    currency_name = models.CharField(max_length=120)

    def __str__(self):
        return self.currency_name