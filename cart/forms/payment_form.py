from django.forms import ModelForm, widgets
from cart.models import OrderPaymentInfo


class PaymentInformationForm(ModelForm):
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

