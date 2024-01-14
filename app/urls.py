from django.urls import path
from .views import *

urlpatterns = [
    path('book/', books, name='book_list'),
    path('book/<int:pk>/', books, name='book_detail'),
    path('author/', authors, name='author_list'),
    path('author/<int:pk>/', authors, name='author_detail'),
    path('place-order/', create_order, name='placed_order'),
    path('orders/', customerOrders, name='orders'),
    path('orders/<int:pk>/', customerOrders, name='book_detail'),
]