"""
Set up product configuration app for store products
"""
from django.apps import AppConfig

class ProductsConfig(AppConfig):
    """
    PRODUCT CONFIGURATION
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
