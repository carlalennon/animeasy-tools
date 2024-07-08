"""
Congifures the bag app
"""
from django.apps import AppConfig


class BagConfig(AppConfig):
    """
    AppConfig class for the 'bag' app.

    This class represents the configuration for the 'bag' app in the Django project.
    It provides settings and metadata specific to the 'bag' app.

    Attributes:
        default_auto_field (str): The default auto field to use for models in the 'bag' app.
        name (str): The name of the 'bag' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
