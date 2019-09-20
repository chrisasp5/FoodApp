from django import forms
from django.forms import ModelForm
from .models import Entry
from .models import NewFood
from django.utils import timezone


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'What\'s on your mind?'})

class NewFoodForm(forms.Form):
    name = forms.CharField(max_length=20,
        widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Food Name'}))
    rating= forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'NumberInput'}))
    comments = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Comments'}))
