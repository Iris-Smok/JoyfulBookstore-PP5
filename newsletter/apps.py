""" app config newsletter app"""
from django.apps import AppConfig


class NewsletterConfig(AppConfig):
    """newsletter config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsletter'
