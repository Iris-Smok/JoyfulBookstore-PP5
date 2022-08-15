""" profiles app views"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_overview, name='account_overview'),
    path('profile/', views.profile, name='profile'),
    path('order_history/', views.order_history, name='order_history'),
    path('order_confiration/<order_number>',
         views.order_confirmation, name='order_confirmation'),
]
