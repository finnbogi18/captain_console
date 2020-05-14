from django.forms import EmailField, CharField, widgets
from django import forms

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreationForm(UserCreationForm):

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
        model = User
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")
        widgets = {
            'username': widgets.TextInput(attrs={
                'class': 'form-control'
            }),
            'password1': widgets.PasswordInput(attrs={
                'class': 'form-control'
            }),
            'password2': widgets.PasswordInput(attrs={
                'class': 'form-control'
            }),
            'email': widgets.EmailInput(attrs={
                'class': 'form-control'
            }),
            'first_name': widgets.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': widgets.TextInput(attrs={
                'class': 'form-control'
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