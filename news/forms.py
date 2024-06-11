from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text']

    widgets = {
        "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name staties',
        }),
        "anons": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Anons staties',
        }),
        "date": DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Date',
        }),
    }
