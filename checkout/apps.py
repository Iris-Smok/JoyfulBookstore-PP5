"""App config for checkout app"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """App config for checkout app"""
    name = 'checkout'

    def ready(self):
        """checkout signals"""
        import checkout.signals
