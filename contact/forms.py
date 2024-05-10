from django import forms
from .models import Ticket, TicketReply
from django.core.exceptions import ValidationError

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'content', 'email', ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Subject',
            'autocomplete': 'off',
            'class' : 'form-control my-1',
        })
        self.fields['email'].label = False 
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email Address',
            'autocomplete': 'off',
            'class' : 'form-control my-1',
        })
        self.fields['title'].label = False
        self.fields['content'].widget.attrs.update({
            'placeholder': 'What can we help you with?',
            'autocomplete': 'off',
            'class' : 'form-control my-1',
        })
        self.fields['content'].label = False
        
class TicketReplyForm(forms.ModelForm):
    class Meta:
        model = TicketReply
        fields = [ 'reply', 'admin',]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reply'].widget.attrs.update({
            'placeholder': 'Reply',
            'autocomplete': 'off',
            'class' : 'form-control m',
        })
        self.fields['reply'].label = False
        
