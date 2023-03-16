from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Animal, Сategory, Age, Product
# from cart.cart import get_cart


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    
    def get(self, request):
        product = Product.objects.all()
        numb = product.count()
        # params = get_cart(request, {'product': product, 'numb': numb})
        return render(request, self.template_name, {'product': product, 'numb': numb})


# class AuthorsView(TemplateView):
#     template_name = 'catalog/authors.html'
    
#     def get(self, request):
#         authors = Author.objects.all()
#         params = get_cart(request, {'authors': authors})
#         return render(request, self.template_name, params)

# class BookView(TemplateView):
#     template_name = 'catalog/book.html'
    
#     def get(self, request, id):
#         book = Book.objects.get(id=id)
#         params = get_cart(request, {'book': book})
#         return render(request, self.template_name, params)
    

# class AuthorView(TemplateView):
#     template_name = 'catalog/index.html'
    
#     def get(self, request, first_name, last_name):
#         author = Author.objects.get(first_name=first_name, last_name=last_name)
#         books = Book.objects.filter(author=author)
#         params = get_cart(request, {'author':author, 'books': books})
#         return render(request, self.template_name, params)
         
        
# class GenresView(TemplateView):
#     template_name = 'catalog/genres.html'
    
#     def get(self, request):
#         genres = Genre.objects.all()
#         params = get_cart(request, {'genres':genres})
#         return render(request, self.template_name, params)        
    
# class GenreView(TemplateView):
#     template_name = 'catalog/index.html'
    
#     def get(self, request, name):
#         genre = Genre.objects.get(name=name)
#         books = Book.objects.filter(genre=genre)
#         params = get_cart(request, {'genre':genre, 'books':books})
#         return render(request, self.template_name, params)    
    
# class SearchView(TemplateView):
#     template_name = 'catalog/index.html'
    
#     def post(self, request):
#         content = request.POST['content']
        
#         #books_by_author = Book.objects.filter(author=content)
#         books_by_title = Book.objects.filter(title__icontains=content)
#         books_by_summary = Book.objects.filter(summary__icontains=content)
#         #books_by_author= Book.objects.filter(author=search_author)
#         result = books_by_title.union(books_by_summary, all=False)
#         params = get_cart(request, {'books': result})
#         return render(request, self.template_name, params)
