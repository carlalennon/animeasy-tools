"""
Creates models for tickets and their replies
"""
from django.db import models
from profiles.models import UserProfile
status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('resolved', 'Resolved')])

class Ticket(models.Model):
    """
    Model for ticket (send email to admin)
    """
    email = models.EmailField(null=True, max_length=254)
    date_received = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    status = models.CharField(max_length=10, choices=[
            ('pending', 'Pending'),
            ('resolved', 'Resolved')
        ],
        default='pending'
    )

    def __str__(self):
        return self.title

class TicketReply(models.Model):
    """
    Model for reply (from admin to user)
    """
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    admin = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    reply = models.TextField(null=True)
    date_reply = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'date_reply'

    def __str__(self):
        return f'Reply to: {self.ticket.title}'
