"""
Handles the views for the home app, newlstter form, about, install guide and FAQ pages
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from newsletter.forms import SubscriberForm

# Create your views here.

def index(request):
    """
    View and forms on the home page, newsletter subscriber box
    """
    form = SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('/')
        if form.errors:
            print(form.errors)
            messages.error(request, 'Email already exists')
        form = SubscriberForm()
    context = {
        'form': form,
    }
    return render(request, 'home/index.html', context)

def about(request):
    """
    View for the about page
    """
    return render(request, 'home/about.html')


def install_guide(request):
    """
    View for the install guide page
    """
    return render(request, 'home/install_guide.html')

def faq(request):
    """
    View for the frequently asked questions page
    """
    return render(request, 'home/faq.html')
