from django.forms import ModelForm, widgets
from cart.models import OrderPaymentInfo
from django import forms


class PaymentInformationForm(ModelForm):

    def clean_cardholder_name(self):
        data = self.cleaned_data['cardholder_name']
        for i in data:
            if not i.isalpha() and not i.isspace():
                raise forms.ValidationError('Invalid name!')

        return data

    def clean_card_number(self):
        data = self.cleaned_data['card_number']
        # The lowest possible credit-card number is a MAESTRO UK which is
        if len(data) < 12:
            raise forms.ValidationError('Invalid credit card!')

        return data

    def clean_cvc(self):
        data = self.cleaned_data['cvc']
        if len(data) != 3:
            raise forms.ValidationError('Invalid CVC!')

        return data

    class Meta:
        model = OrderPaymentInfo
        exclude = ('order',)
        widgets = {
            'card_number': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Credit Card',
                'type':'number',
                'min_length':'15'
            }),
            'cardholder_name': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cardholder name',
                'type':'text'
            }),
            'cvc': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CVC',
                'type':'number'
            }),
            'expiry_month': widgets.Select(attrs={
                'class':'custom-select'
            }),
            'expiry_year': widgets.Select(attrs={
                'class': 'custom-select'
            })
        }


