from django.contrib import admin
from django.urls import path, include
from .views import IndexView, ProductView, CatsView, SearchView, DogsView, RodentsView, FishView
from django.conf import settings
from django.conf.urls.static import static

# '' - "Домашняя страница"
# 'product/' - Список всех товаров
# 'product/<id>' - Детальная информация для отображения товара

urlpatterns = [
    path('', IndexView.as_view(), name='catalog-index'),
    path('catalog/<int:id>/', ProductView.as_view(), name='catalog-product'),
    path('catalog/search/', SearchView.as_view(), name='catalog-search'),
    path('catalog/cats/', CatsView.as_view(), name='catalog-cats'),
    path('catalog/dogs/', DogsView.as_view(), name='catalog-dogs'),
    path('catalog/rodents/', RodentsView.as_view(), name='catalog-rodents'),
    path('catalog/fish/', FishView.as_view(), name='catalog-fish'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)