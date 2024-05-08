from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from .forms import TicketForm
# from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame
from django.contrib.auth.decorators import login_required   


def contact(request):
    """
    User can submit a ticket 
    """
    form = TicketForm()
    template = 'contact/contact_form.html'
    email = Ticket.email
    df = read_frame(email, fieldnames=['email'])
    reply_mail = df['email'].values.tolist()
    """ Allows a user to create a ticket """ 
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')   
            email = form.cleaned_data.get('email')      
            send_mail(
                title,
                content,
                'contact@animeasy.com',
                reply_mail,
                fail_silently=False,
            )
            messages.success(request, 'Your ticket has been submitted')
            return redirect('contact_success')
        else: 
            form = TicketForm()

    context = {
        'form': form,
    }
    return render(request, template, context)

   
def contact_success(request):
    """
    Users are redirected here when a ticket is sent 
    """
    ticket_id = Ticket.id
    ticket = get_object_or_404(Ticket, ticket_number=ticket_id)
    
    """
    Could attach tickets to account later 
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        #Attach user to order 
        order.user_profile = profile
        order.save()
    """    
        
    template = 'contact/contact_success.html'
    context = {
        'ticket': ticket,
    }
    
    return render(request, template, context)

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




