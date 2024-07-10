"""
Set up admin panel for store products
"""
from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    """
    Adds products to admin panel
    """
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    """
    Adds product categories to admin panel
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
