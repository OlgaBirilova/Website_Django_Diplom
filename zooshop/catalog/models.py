from django.db import models
from django.urls import reverse

class Animal(models.Model):
    title = models.CharField(max_length=100)
    #photo = models.ImageField(upload_to="animals/", blank=True, default="photo-placeholder.png")
        
    def __str__(self):
        return self.title
    
    # def get_animal_url(self):
    #     return reverse('catalog-animal', args=[self.title])

class Сategory(models.Model):
    name = models.CharField(max_length=50)
    animals = models.ForeignKey(Animal, on_delete=models.PROTECT)
    #image = models.ImageField(upload_to="categories/", blank=True, default="image-placeholder.jpeg")
        
    def __str__(self):
        return self.name
    
    # def get_genre_url(self):
    #     return reverse('catalog-сategory', args=[self.name])

class Age(models.Model):
    age = models.CharField(max_length=10)
    animals = models.ForeignKey(Animal, on_delete=models.PROTECT)

    def __str__(self):
        return self.age

class Product(models.Model):
    title = models.CharField(max_length=100)
    animals = models.ForeignKey(Animal, on_delete=models.PROTECT)
    category = models.ForeignKey(Сategory, on_delete=models.PROTECT)
    ageanimal = models.ManyToManyField(Age)
    description = models.TextField(max_length=500, help_text='Enter a description of the product')
    ingredients = models.TextField(max_length=500, help_text='Enter the composition of the product')
    price = models.FloatField()
    amount = models.IntegerField(default=0)
    #image = models.ImageField(upload_to="books/", blank=True, default="book-placeholder.jpeg")

    def __str__(self):
        return self.title

    def display_ageanimal(self):
        return ', '.join([ageanimal.age for ageanimal in self.ageanimal.all()])
    
    # def get_book_url(self):
    #     return reverse('catalog-book', args=[self.id])
    
    # def add_to_cart(self):
    #     return reverse('cart-add', args=[self.id])
    
    # def del_to_cart(self):
    #     return reverse('cart-del', args=[self.id])
    
    # display_genre.short_description = 'Genre'