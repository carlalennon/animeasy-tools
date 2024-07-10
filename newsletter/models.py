"""
Models for newsletter and subscribers
"""
from django.db import models

class Subscriber(models.Model):#
    """
    Model for people subscribed to the newsletter
    """
    email = models.EmailField(null=True, max_length=254)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    """
    Model for the newsletter
    """
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
