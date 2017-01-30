from django.forms import ModelForm
from django.contrib.auth.models import Group

from .models import Facility

class FacilityForm(ModelForm):
    """Form that defines facility creation """

    class Meta:
        model = Facility
        fields = '__all__'

class GroupForm(ModelForm):
    """Form that allows users to create a new group"""

    class Meta:
        model = Group
        fields = "__all__"


