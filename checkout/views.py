from django.shortcuts import render, redirect, reverse 
from django.contrib import messages 

from .forms import OrderForm

def checkout(request):
    bag = request.soession.get('bag', {})
    if not bag: 
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    return render(request, 'checkout/checkout.html')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    } 
    
    return render(request, template, context)