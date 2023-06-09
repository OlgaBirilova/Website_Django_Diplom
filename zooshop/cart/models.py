from django.db import models
from django.shortcuts import reverse, redirect
from django.contrib.auth.models import User
from catalog.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product, blank=True)
        
    def get_total_price(self):
        return sum([product.price for product in self.products.all()])    
        
    def get_total_quantity(self):
        return len([product for product in self.products.all()])
    
    def display_products(self):
        return ", ".join([product.title for product in self.products.all()])