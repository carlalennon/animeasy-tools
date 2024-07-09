"""
A file with listeners that will update the order total when a line
item is created, updated or deleted.
"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(_sender, instance, _created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(_sender, instance, created, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
