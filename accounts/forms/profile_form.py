from django.forms import ModelForm, widgets

from accounts.models import Profile
from django.contrib.auth.models import User
from django import forms


class UserForm(ModelForm):

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

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email'
        )
        widgets = {
            'first_name': widgets.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': widgets.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': widgets.TextInput(attrs={
                'class': 'form-control'
            })
        }


class ProfileForm(ModelForm):

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        for i in data:
            if not i.isnumeric():
                raise forms.ValidationError('Invalid phone number!')

        if not len(data) == 8:
            raise forms.ValidationError('Invalid phone number!')

        return data

    class Meta:
        model = Profile
        fields = (
            'profile_image',
            'phone_number'
        )
        widgets = {
            'profile_image': widgets.URLInput(attrs={
                'class': 'form-control'
            }),
            'phone_number': widgets.TextInput(attrs={
                'class': 'form-control'
            })
        }



