from django.db import models

# Create your models here.
class Shop(models.Model):
    owner = models.OneToOneField("User", on_delete=models.CASCADE, related_name='shop')

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='reviews')

class User(models.Model):
    reviewed_products = models.ManyToManyField(Product, related_name='user')