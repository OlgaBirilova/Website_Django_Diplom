from django.contrib import admin

from .models import Animal, Сategory, Age, Product


admin.site.register(Animal)
    
@admin.register(Сategory)
class СategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'animals')

@admin.register(Age)
class СategoryAdmin(admin.ModelAdmin):
    list_display = ('age', 'animals')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'animals', 'category', 'display_ageanimal', 'price', 'amount')