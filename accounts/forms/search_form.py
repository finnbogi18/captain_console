from django.forms import ModelForm, widgets

from accounts.models import SearchHistory


class SearchForm(ModelForm):
    class Meta:
        model = SearchHistory
        exclude = ['id', 'user', 'date']
        widgets = {
            'search': widgets.TextInput(attrs={ 'class': 'form-control mr-sm-2', 'type':'search',
            'placeholder': 'Search', 'aria-label': 'Search'}),

        }
