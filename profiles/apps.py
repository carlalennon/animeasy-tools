"""
Set up apps for user profiles
"""
from django.apps import AppConfig

class ProfilesConfig(AppConfig):
    """
    App configuration for profiles
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
