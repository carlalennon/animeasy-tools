"""
Calculate the subtotal of the item by multiplying the price by the quantity
"""

from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculate the subtotal of the item by multiplying the price by the quantity
    """
    return price * quantity#
