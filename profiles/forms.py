"""
Forms for user profiles
"""
from django import forms
from django.core.exceptions import ValidationError
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    """
    Users can change their default billing information
    """
    class Meta:
        model =UserProfile
        exclude = ('user', )

    def __init__(self, *args, **kwargs):
        #Add placeholders and classes, remove auto-generated labels and set autofocus on first field
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
            
    def clean_default_country(self):
        country = self.cleaned_data.get('default_country')
        if country and len(country) != 2:
            raise ValidationError('Country code must be 2 letters.')
        return country
