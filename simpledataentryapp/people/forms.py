from django import forms
from .models import Person


class NewPersonForm(forms.ModelForm):
    # name and title are required by default
    name = forms.CharField(
        label='Name',
        max_length=Person._meta.get_field('name').max_length
    )
    title = forms.CharField(
        label='Title',
        max_length=Person._meta.get_field('title').max_length
    )
    age = forms.IntegerField(
        # Not defining min/max values here,
        label='Age',
        required=False
    )
    hometown = forms.CharField(
        label='Hometown',
        max_length=Person._meta.get_field('hometown').max_length,
        required=False
    )

    class Meta:
        model = Person
        fields = ['name', 'title', 'age', 'hometown']
