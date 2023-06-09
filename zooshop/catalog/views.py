from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Animal, Сategory, Product
from cart.cart import get_cart


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    
    def get(self, request):
        products = Product.objects.all()
        category = Сategory.objects.all().count()
        animals = Animal.objects.all().count()
        numb = products.count()
        params =  get_cart(request, {'products': products, 'numb': numb, 'category': category, 'animals': animals})
        return render(request, self.template_name, params)


class ProductView(TemplateView):
    template_name = 'catalog/product.html'
    
    def get(self, request, id):
        product = Product.objects.get(id=id)
        params =  get_cart(request, {'product': product})
        return render(request, self.template_name, params)
    

class CatsView(TemplateView):
    template_name = 'catalog/index.html'
    
    def get(self, request):
        products_by_animals = Product.objects.filter(animals=1)
        params =  get_cart(request, {'products': products_by_animals})
        return render(request, self.template_name, params)

class DogsView(TemplateView):
    template_name = 'catalog/index.html'
    
    def get(self, request):
        products_by_animals = Product.objects.filter(animals=2)
        params =  get_cart(request, {'products': products_by_animals})
        return render(request, self.template_name, params)

class RodentsView(TemplateView):
    template_name = 'catalog/index.html'
    
    def get(self, request):
        products_by_animals = Product.objects.filter(animals=3)
        params =  get_cart(request, {'products': products_by_animals})
        return render(request, self.template_name, params)

class FishView(TemplateView):
    template_name = 'catalog/index.html'
    
    def get(self, request):
        products_by_animals = Product.objects.filter(animals=4)
        params =  get_cart(request, {'products': products_by_animals})
        return render(request, self.template_name, params)

# class AnimalCategoryView(TemplateView):
#     template_name = 'catalog/index.html'
    
#     def get(self, request, title, name):
#         animal = Animal.objects.get(title=title)
#         category = Сategory.objects.get(name=name)
#         product = Product.objects.filter(animal=animal, name=name)
#         params = {'animal':animal, 'category':category, 'product': product}
#         return render(request, self.template_name, params)
         
class SearchView(TemplateView):
    template_name = 'catalog/index.html'
    
    def post(self, request):
        content = request.POST['content']
        products_by_title = Product.objects.filter(title__icontains=content)
        products_by_description = Product.objects.filter(description__icontains=content)
        result = products_by_title.union(products_by_description, all=False)
        params =  get_cart(request, {'products': result})
        return render(request, self.template_name, params)
