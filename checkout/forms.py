"""
File which handles the forms in the checkout section of Animeasy
"""
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    """
    Sets the fields to appear in the order form
    """
    class Meta:
        model = Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'street_address1',
            'street_address2',
            'town_or_city',
            'postcode',
            'country',
            'county',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country' : '2 Letter Country Code',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

       # Styles fields
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field in placeholders:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
                self.fields[field].label = False
