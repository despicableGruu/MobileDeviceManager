from django.forms import ModelForm, ClearableFileInput, ImageField
from .models import Application


class CreateApplicationForm(ModelForm):
    """Form to create a new application that will
    be hosted on our site."""

    screenshot = ImageField(widget=ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Application
        exclude = ['number_of_downloads']
