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
        params = {'products': products, 'numb': numb, 'category': category, 'animals': animals}
        return render(request, self.template_name, params)


# class CatsView(TemplateView):
#     template_name = 'catalog/cats.html'
    
#     def get(self, request):
#         authors = Author.objects.all()
#         params = get_cart(request, {'authors': authors})
#         return render(request, self.template_name, params)

class ProductView(TemplateView):
    template_name = 'catalog/product.html'
    
    def get(self, request, id):
        product = Product.objects.get(id=id)
        params = {
            'product': product
            }
        return render(request, self.template_name, params)
    

class AnimalView(TemplateView):
    template_name = 'catalog/index.html'
    
    def get(self, request, title):
        animal = Animal.objects.get(title=title)
        products = Product.objects.filter(animal=animal)
        params = {'animal': animal, 'products': products}
        return render(request, self.template_name, params)

class AnimalCategoryView(TemplateView):
    template_name = 'catalog/index.html'
    
    def get(self, request, title, name):
        animal = Animal.objects.get(title=title)
        category = Сategory.objects.get(name=name)
        product = Product.objects.filter(animal=animal, name=name)
        params = {'animal':animal, 'category':category, 'product': product}
        return render(request, self.template_name, params)
         
class SearchView(TemplateView):
    template_name = 'catalog/index.html'
    
    def post(self, request):
        content = request.POST['content']
        products_by_title = Product.objects.filter(title__icontains=content)
        products_by_description = Product.objects.filter(description__icontains=content)
        result = products_by_title.union(products_by_description, all=False)
        params = {
            'products': result
        }
        return render(request, self.template_name, params)
