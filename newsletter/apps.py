"""
Sets up the app for the newsletter app
"""
from django.apps import AppConfig


class NewsletterConfig(AppConfig):
    """
    Create big auto field
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsletter'
