from django.forms import EmailField, CharField, widgets

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreationForm(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True),
    first_name = CharField(label=_("First name"), required=True),
    last_name = CharField(label=_("Last name"), required=True)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")
        widgets = {
            'username': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'password1': widgets.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            'password2': widgets.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password confirmation'
            }),
            'email': widgets.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'first_name': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            'last_name': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            })
        }

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.fname = self.cleaned_data["first_name"]
        user.lname = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user