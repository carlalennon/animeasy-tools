from django.shortcuts import render
from .models import Subscriber, Newsletter
from .forms import SubscriberForm

def newsletter(request):
    context = {
        
    }
    return render(request, 'newsletter/newsletter.html', context)
# Handled in home/views.py
#def newsletter_subscribe(request):
#    form = SubscriberForm()
#    context = {
#        'form': form,
#    }
#    return render(request, 'index.html', context)

def newsletter_success(request):
    context = {
        
    }
    return render(request, 'newsletter/newsletter_success.html', context)

def newsletter_unsubscribe(request):
    context = {
        
    }
    return render(request, 'newsletter/newsletter_unsubscribe.html', context)  

def newsletter_unsubscribe_success(request):
    context = {
        
    }
    return render(request, 'newsletter/newsletter_unsubscribe_success.html', context)




