from django.contrib import admin
from django.urls import path, include
from .views import IndexView, ProductView, AnimalView
from django.conf import settings
from django.conf.urls.static import static

# '' - "Домашняя страница"
# 'product/' - Список всех товаров
# 'product/<id>' - Детальная информация для отображения товара

urlpatterns = [
    path('', IndexView.as_view(), name='catalog-index'),
    # path('authors/', AuthorsView.as_view(), name='catalog-authors'),
    # path('catalog/genres/', GenresView.as_view(), name='catalog-genres'),
    # path('catalog/<str:first_name>-<str:last_name>/', AuthorView.as_view(), name='catalog-author'),
    path('catalog/<int:id>/', ProductView.as_view(), name='catalog-product'),
    path('catalog/<int:title>/', AnimalView.as_view(), name='catalog-animal'),
    # path('catalog/search/', SearchView.as_view(), name='catalog-search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)