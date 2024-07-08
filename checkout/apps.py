"""
Configuration class for the 'checkout' app.

This class defines the configuration for the 'checkout' app in Animeasy.
It registers the 'checkout.signals' module to be imported when the app is ready.
"""

from django.apps import AppConfig

class CheckoutConfig(AppConfig):
    """
    Configuration for the 'checkout' app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
