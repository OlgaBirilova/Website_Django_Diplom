from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Cart
from catalog.models import Product
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class CartAddView(TemplateView):
    
    @method_decorator(login_required)
    def get(self, request, id):
        book = Product.objects.get(id=id)
        cart = Cart.objects.get(user=request.user)
        cart.products.add(product)
        
        return redirect('catalog-index')
    
class CartDelView(TemplateView):
    
    @method_decorator(login_required)
    def get(self, request, id):
        cart = Cart.objects.get(user=request.user)
        cart.products.set(cart.products.exclude(id=id))
        
        return redirect('catalog-index')
    
class CartDelAllView(TemplateView):
    
    @method_decorator(login_required)
    def get(self, request):
        Cart.objects.get(user=request.user).products.set(list())
    
        return redirect('catalog-index')