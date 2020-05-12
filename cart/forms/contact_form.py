from django.forms import ModelForm, widgets
from cart.models import OrderContactInfo, Order


class ContactInformationForm(ModelForm):
    class Meta:
        model = OrderContactInfo
        exclude = ('order', 'house_number')
        widgets = {
            'first_name': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            'last_name': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Last Name'
            }),
            'street_name': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Address'
            }),
            'city': widgets.TextInput(attrs={
                'class':'form-control',
                'placeholder':'City'
            }),
            'country': widgets.Select(attrs={
                'class': 'custom-select',
            }),
            'postal_code':widgets.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Postal code'
            })
        }

