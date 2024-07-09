"""
Sets up the admin view for the contact app
"""

from django.contrib import admin
from .models import Ticket, TicketReply

admin.site.register(Ticket)

class TicketReplyAdmin(admin.ModelAdmin):
    """
    Label replies by ticket in admin view
    """
    def __str__(self):
        return f"Reply to {self.ticket.name}"

admin.site.register(TicketReply, TicketReplyAdmin)
