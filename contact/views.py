from django.shortcuts import render, redirect, get_object_or_404

from .models import Ticket
from .forms import TicketForm
# from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required   


def contact(request):
    """
    User can submit a ticket 
    """
    form = TicketForm()
    template = 'contact/contact_form.html'
    email = Ticket.email

    """ Allows a user to create a ticket """ 
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            """
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')   
            email = form.cleaned_data.get('email')      
            send_mail(
                title,
                content,
                'contact@animeasy.com',
                email,
                fail_silently=False,
            )
            """
            messages.success(request, 'Your ticket has been submitted')
            ticket_id = ticket.id 
            return redirect('contact_success', ticket_id=ticket.id)
        else: 
            form = TicketForm()

    context = {
        'form': form,
        
    }
    return render(request, template, context)

   
def contact_success(request, ticket_id):
    """
    Users are redirected here when a ticket is sent 
    """
    ticket = get_object_or_404(Ticket, pk=ticket_id)
 
    """
    Could attach tickets to account later 
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        #Attach user to order 
        order.user_profile = profile
        order.save()
    """        
    context = {
        'ticket': ticket,
    }  
    return render(request, "contact/contact_success.html", context)

@login_required
def contact_tickets(request):
    """
    A view to show all tickets 
    """
    if request.user.is_superuser:
        tickets = Ticket.objects.all()
        context = {
            'tickets': tickets,
        }

        return render(request, 'contact/contact_archive.html', context)
    else:
        messages.error(request, 'You do not have permission to view this page')
        return redirect('home')
    
    
    
def ticket_detail(request, ticket_id):
    """ Returns page with all ticket information """
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    context = {
        'ticket': ticket,
    }
    return render(request, 'contact/contact_detail.html', context)




