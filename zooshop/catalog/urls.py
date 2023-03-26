from django.contrib import admin
from django.urls import path, include
from .views import IndexView, ProductView, AnimalView, SearchView
from django.conf import settings
from django.conf.urls.static import static

# '' - "Домашняя страница"
# 'product/' - Список всех товаров
# 'product/<id>' - Детальная информация для отображения товара

urlpatterns = [
    path('', IndexView.as_view(), name='catalog-index'),
    path('catalog/<int:id>/', ProductView.as_view(), name='catalog-product'),
    path('catalog/<int:title>/', AnimalView.as_view(), name='catalog-animal'),
    path('catalog/search/', SearchView.as_view(), name='catalog-search'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)