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
                'label': 'Credit Card'
            }),
            'cardholder_name': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cardholder name'
            }),
            'cvv': widgets.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'cvv'
            }),
            'expiry_month': widgets.Select(attrs={
                'class':'custom-select'
            }),
            'expiry_year': widgets.Select(attrs={
                'class': 'custom-select'
            })
        }

