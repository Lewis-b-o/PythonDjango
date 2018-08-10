from django.urls import path
from . import views

app_name = 'shopping_cart'

urlpatterns = [
    path('add/<int:product_id>/', views._adding_cart, name='_adding_cart'),
    path('', views.Itemcartdetails, name='Itemcartdetails'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove_all_items/<int:product_id>/', views.remove_all_items, name='remove_all_items'),
]
