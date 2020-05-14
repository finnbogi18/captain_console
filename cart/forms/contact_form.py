from django.forms import ModelForm, widgets
from cart.models import OrderContactInfo
from django import forms


class ContactInformationForm(ModelForm):

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        for i in data:
            if not i.isalpha():
                raise forms.ValidationError('Invalid first name!')

        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        for i in data:
            if not i.isalpha():
                raise forms.ValidationError('Invalid last name!')

        return data

    class Meta:
        model = OrderContactInfo
        exclude = ('order',)
        widgets = {
            'first_name': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            'last_name': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'address': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address'
            }),
            'city': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City'
            }),
            'country': widgets.Select(attrs={
                'class': 'custom-select',
            }),
            'postal_code': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Postal code'
            })
        }
