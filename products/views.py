from django.shortcuts import render
from .models import Product
# Create your views here.

def all_products(request):
    """ Returns all products page """
    
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)