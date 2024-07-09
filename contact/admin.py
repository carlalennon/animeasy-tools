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
    list_display = ('ticket', 'reply_text', 'created_at')
    list_filter = ('ticket', 'created_at')
    search_fields = ('ticket__name', 'reply_text')
    date_hierarchy = 'created_at'

admin.site.register(TicketReply, TicketReplyAdmin)
