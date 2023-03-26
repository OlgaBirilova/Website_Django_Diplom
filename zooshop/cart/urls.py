from django.urls import path, include
from .views import CartAddView, CartDelView, CartDelAllView


urlpatterns = [
    path('add/<int:id>/', CartAddView.as_view(), name='cart-add'),
    path('del/<int:id>/', CartDelView.as_view(), name='cart-del'),
    path('del_all/', CartDelAllView.as_view(), name='cart-del_all'),
]