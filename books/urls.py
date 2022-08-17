""" book app views"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='books'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
]
