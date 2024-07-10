"""
Sets up the admin interface for the newsletter app.
"""

from django.contrib import admin
from .models import Subscriber, Newsletter

admin.site.register(Subscriber)
admin.site.register(Newsletter)
