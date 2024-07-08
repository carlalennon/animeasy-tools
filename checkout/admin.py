"""
Sets up the admin panel for orders in the checkout app
"""
from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    """
    Shows the line items in the admin panel
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    """
    Order admin panel
    """
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = (
        'order_number',
        'date',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',
        )

    fields = (
        'order_number',
        'user_profile',
        'date', 'full_name',
        'email',
        'phone_number',
        'country',
        'postcode',
        'town_or_city',
        'street_address1',
        'street_address2',
        'county',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',
        )

    list_display = (
        'order_number',
        'date',
        'full_name',
        'order_total',
        'grand_total',
        'country',
    )

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
