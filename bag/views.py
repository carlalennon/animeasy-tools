from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ Returns user bag """
    return render(request, 'bag/bag.html')