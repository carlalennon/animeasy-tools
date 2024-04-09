from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.



def all_products(request):
    """ Returns all products page """
    
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Returns page with detailed information about selected product  """
    
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)