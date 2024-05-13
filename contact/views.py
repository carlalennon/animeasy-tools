from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket, TicketReply
from .forms import TicketForm, TicketReplyForm
from profiles.models import UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required  
from django.core.mail import send_mail 


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
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')   
            email = form.cleaned_data.get('email')      
            send_mail(
                title,
                content,
                'contact@animeasy.com',
                [email],
                fail_silently=False,
            )
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
        
        # Filter by unresolved status
        unresolved = request.GET.get('unresolved')
        if unresolved == 'true':
            tickets = tickets.filter(status='pending')

        # Filter by unresolved status
        resolved = request.GET.get('resolved')
        if resolved == 'true':
            tickets = tickets.filter(status='resolved')

        # Sorting by date ascending and descending
        sort_by_date = request.GET.get('sort')
        if sort_by_date == 'asc':
            tickets = tickets.order_by('date_received')
        elif sort_by_date == 'desc':
            tickets = tickets.order_by('-date_received')

        # Sorting by ID number
        sort_by_id = request.GET.get('sort_by_id')
        if sort_by_id == 'asc':
            tickets = tickets.order_by('id')
        elif sort_by_id == 'desc':
            tickets = tickets.order_by('-id')
        
        admin = TicketReply.objects.all()
        context = {
            'tickets': tickets,
            'admin': admin,
        }

        return render(request, 'contact/contact_tickets.html', context)
    else:
        messages.error(request, 'You do not have permission to view this page')
        return redirect('home')
    
    
    
def ticket_detail(request, ticket_id):
    """ Returns page with all ticket information """
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    """
    Allows admin to reply to a ticket 
    """
    template = 'contact/ticket_detail.html'
    email = ticket.email
    reply = None
    if request.user.is_superuser:  
        if request.method == 'POST':
            form = TicketReplyForm(request.POST)
            if form.is_valid():
                reply = TicketReply()
                reply.ticket = ticket
                reply.reply = form.cleaned_data.get('reply')  
                email_body = reply.reply
                reply.admin = UserProfile.objects.get(user=request.user)
                reply.save()
                title = ticket.title   
                send_mail(
                    title,
                    email_body,  # Use reply.reply instead of reply
                    'support@animeasy.com',
                    [email],
                    fail_silently=False,
                )
                messages.success(request, 'Reply was sent to ' + email )
                ticket.status = 'resolved'
                ticket.save()
                return redirect('contact_tickets')
        else: 
            form = TicketReplyForm()
        return render(request, template, {'form': form, 'ticket': ticket})
    else: 
        messages.error(request, 'You do not have permission to reply to tickets')
        return redirect('home')

def privacy_policy(request):
    template = 'contact/privacy_policy.html'
    return render(request, template)

def terms_and_conditions(request):
    template = 'contact/terms_and_conditions.html'
    return render(request, template)
