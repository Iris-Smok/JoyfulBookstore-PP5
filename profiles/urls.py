""" profiles app views"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_overview, name='account_overview'),
    path('profile/', views.profile, name='profile'),
]
