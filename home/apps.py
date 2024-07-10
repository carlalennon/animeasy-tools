"""
Sets up the forms for the home page newsletter box
"""
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Sets up the newsletter subscribe box
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
