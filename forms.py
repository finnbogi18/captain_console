from django.forms import EmailField, CharField

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreationForm(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True,
        help_text=_("Required."))
    first_name = CharField(label=_("First name"), required=True,
        help_text=_("Required."))
    last_name = CharField(label=_("Last name"), required=True,
        help_text=_("Required."))

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.fname = self.cleaned_data["first_name"]
        user.lname = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user