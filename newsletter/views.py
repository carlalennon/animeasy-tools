from django.shortcuts import render, redirect
from .models import Subscriber, Newsletter
from .forms import SubscriberForm, NewsletterForm
from django.core.paginator import Paginator




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
    template = 'newsletter/newsletter.html'
    """ Allows a user to create a newsletter """
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newsletter_success')
    context = {
        'form': form,
    }
    return render(request, template, context)
        
        
def newsletter_success(request):
    """
    A view on creation of new newsletter to show the content 
    """
    subscribers = Subscriber.objects.all()
    latest_newsletter = Newsletter.objects.latest('date_created')
    context = {
        'subscribers': subscribers,
        'latest_newsletter': latest_newsletter,
    }
    return render(request, 'newsletter/newsletter_success.html', context)

def newsletter_archive(request):
    """
    A view to show all newsletters that have been created
    """
    newsletters = Newsletter.objects.all()
    context = {
        'newsletters': newsletters,
    }

    return render(request, 'newsletter/newsletter_archive.html', context)




