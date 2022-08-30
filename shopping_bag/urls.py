""" shopping bag app urls"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_bag_view, name='shopping_bag_view'),
    path('add/<item_id>', views.add_to_shopping_bag,
         name='add_to_shopping_bag'),
    path('adjust/<item_id>', views.adjust_shopping_bag,
         name='adjust_shopping_bag'),
    path('delete/<item_id>/', views.delete_from_shopping_bag,
         name='delete_from_shopping_bag'),
]
