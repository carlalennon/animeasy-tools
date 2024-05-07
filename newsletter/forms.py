from django import forms
from .models import Subscriber, Newsletter

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email',
            'autocomplete': 'off',
            'class' : 'form-control',
        })
        self.fields['email'].label = False
        
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['title', 'content', ]
        
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
            'class' : 'form-control',
        })
        self.fields['content'].label = False