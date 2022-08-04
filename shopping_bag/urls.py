""" shopping bag app views"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_bag_view, name='shopping_bag'),
    path('add/<book_id>', views.add_to_shopping_bag, name='add_to_shopping_bag'),
]
