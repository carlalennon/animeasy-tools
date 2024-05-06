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