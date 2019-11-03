from django import forms
from django.forms import ModelForm
from .models import NewFood
from django.utils import timezone


class NewFoodForm(ModelForm):
    class Meta:
        model = NewFood
        fields = ('name', 'rating', 'comments')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Food Name'})
        self.fields['rating'].widget.attrs.update({'class': 'ChoiceField'})
        self.fields['comments'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Comments'})
