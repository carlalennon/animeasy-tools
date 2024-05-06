from django.shortcuts import render
from newsletter.forms import SubscriberForm

# Create your views here.

def index(request):
    """ Returns index page """
    form = SubscriberForm()
    context = {
        'form': form,
    }    
    return render(request, 'home/index.html', context)