from django.shortcuts import render, redirect
from .models import Subscriber, Newsletter
from .forms import SubscriberForm, NewsletterForm




def newsletter_unsubscribe(request):
    context = {
        
    }
    return render(request, 'newsletter/newsletter_unsubscribe.html', context)  

def newsletter_unsubscribe_success(request):
    context = {
        
    }
    return render(request, 'newsletter/newsletter_unsubscribe_success.html', context)

def newsletter_create(request):
    form = NewsletterForm()
    template = 'newsletter/newsletter_create.html'
    """ Allows a user to create a newsletter """
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newsletter_success')
        
        
def newsletter_success(request):
    """
    A view on creation of new nesletter to show the content 
    """
    context = {
        
    }
    return render(request, 'newsletter/newsletter_success.html', context)




