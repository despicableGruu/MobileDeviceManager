from django.forms import ModelForm, PasswordInput
from .models import facility, user
from django.contrib.auth.models import User, Group

class BasicUserForm(ModelForm):
	"""Form to create a general user."""

	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']

class CustomUserForm(ModelForm):
	"""Form that create the custom user fields for this application"""

	class Meta:
		model = user
		fields = ['is_publisher']

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


