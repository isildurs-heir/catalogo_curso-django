from django import forms
from catalogo.models import Genre, Author
from django.forms.widgets import NumberInput

class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = ('name',)

class AuthorForm(forms.ModelForm):
    pass