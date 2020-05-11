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


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            'profile_image',
            'phone_number'
        )



