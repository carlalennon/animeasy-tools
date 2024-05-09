from django.shortcuts import render, redirect
from django.contrib import messages
from newsletter.forms import SubscriberForm

# Create your views here.

def index(request):
    form = SubscriberForm()
    """ Returns index page """
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('/')
        elif form.errors:
            print(form.errors)
            messages.error(request, 'Email already exists')
        else:

            form = SubscriberForm()
    context = {
        'form': form,
    }    
    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html')