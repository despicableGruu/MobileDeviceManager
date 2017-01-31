from django.forms import ModelForm

from .models import Facility

class FacilityForm(ModelForm):
    """Form that defines facility creation """

    class Meta:
        model = Facility
        fields = '__all__'



