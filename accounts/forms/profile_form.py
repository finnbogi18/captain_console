from django.forms import ModelForm, widgets

from accounts.models import Profile
from django.contrib.auth.models import User


class UserForm(ModelForm):
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
    class Meta:
        model = Profile
        fields = (
            'profile_image',
            'phone_number'
        )
        widgets = {
            'profile_image': widgets.TextInput(attrs={
                'class': 'form-control'
            }),
            'phone_number': widgets.TextInput(attrs={
                'class': 'form-control'
            })
        }



