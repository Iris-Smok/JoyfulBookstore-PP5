""" book app views"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='books'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('edit_category/<int:category_id>/',
         views.edit_category, name='edit_category'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('delete_category/<int:category_id>/',
         views.delete_category, name='delete_category'),

]
