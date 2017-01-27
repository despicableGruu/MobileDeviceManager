from django.forms import ModelForm
from .models import facility
from django.contrib.auth.models import Group

class FacilityForm(ModelForm):
	"""Form that defines facility creation """

	class Meta:
		model = facility
		fields = '__all__'

class GroupForm(ModelForm):
	"""Form that allows users to create a new group"""

	class Meta:
		model = Group
		fields = "__all__"


