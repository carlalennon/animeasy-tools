from django.shortcuts import render, redirect
from .models import Subscriber, Newsletter
from .forms import NewsletterForm
# from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame
from django.contrib.auth.decorators import login_required   
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired



@login_required
def newsletter_create(request):
    """
    Allows admin to create newsletter
    """
    form = NewsletterForm()
    template = 'newsletter/newsletter.html'
    emails = Subscriber.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    email_list = df['email'].values.tolist()
    print(email_list)
    """ Allows a user to create a newsletter """
    if request.user.is_superuser:  
        if request.method == 'POST':
            form = NewsletterForm(request.POST)
            if form.is_valid():
                form.save()
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')         
                send_mail(
                    title,
                    content,
                    'newsletter@animeasy.com',
                    email_list,
                    fail_silently=False,
                )
                messages.success(request, 'Newsletter created successfully')
                return redirect('newsletter_success')
        else: 
            form = NewsletterForm()
    else: 
        messages.error(request, 'You do not have permission to create a newsletter')
        return redirect('home')
    
    context = {
        'form': form,
    }
    return render(request, template, context)
        
@login_required      
def newsletter_success(request):
    """
    A view on creation of new newsletter to show the content 
    """
    if request.user.is_superuser:
        subscribers = Subscriber.objects.all()
        latest_newsletter = Newsletter.objects.latest('date_created')
        context = {
            'subscribers': subscribers,
            'latest_newsletter': latest_newsletter,
        }
        return render(request, 'newsletter/newsletter_success.html', context)
    else: 
        messages.error(request, 'You do not have permission to view this page')
        return redirect('home')

@login_required
def newsletter_archive(request):
    """
    A view to show all newsletters that have been created
    """
    if request.user.is_superuser:
        newsletters = Newsletter.objects.all()
        context = {
            'newsletters': newsletters,
        }

        return render(request, 'newsletter/newsletter_archive.html', context)
    else:
        messages.error(request, 'You do not have permission to view this page')
        return redirect('home')

def newsletter_unsubscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            subscriber = Subscriber.objects.get(email=email)
            subscriber.delete()
            messages.success(request, 'You have been unsubscribed')
        except Subscriber.DoesNotExist:
            messages.error(request, 'You are not subscribed')
        return redirect('home')
    else: 
        return render(request, 'newsletter/newsletter_unsubscribe.html')



