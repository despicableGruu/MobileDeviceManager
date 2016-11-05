from django.forms import ModelForm
from application.models import Application

class CreateApplicationForm(ModelForm):
  """Form to create a new application that will 
  be hosted on our site."""

  class Meta:
    model = Application
    fields = '__all__'