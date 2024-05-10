from django import forms
from .models import Ticket
from django.core.exceptions import ValidationError

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'content', 'email', ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Title',
            'autocomplete': 'off',
            'class' : 'form-control',
        })
        self.fields['title'].label = False
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Content',
            'autocomplete': 'off',
            'class' : 'form-control m',
        })
        self.fields['content'].label = False
        
class TicketReplyForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [ 'content',]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Content',
            'autocomplete': 'off',
            'class' : 'form-control m',
        })
        self.fields['content'].label = False
        
