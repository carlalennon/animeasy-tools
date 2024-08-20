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
    list_display = ('ticket', 'reply', 'date_reply')
    list_filter = ('ticket', 'date_reply')
    search_fields = ('ticket__name', 'reply')
    date_hierarchy = 'date_reply'

admin.site.register(TicketReply, TicketReplyAdmin)
