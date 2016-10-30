from django.forms import ModelForm, PasswordInput
from .models import facility, user
from django.contrib.auth.models import User

class DefaultFacilityAdminForm(ModelForm):
	"""Form that creates the default django user parts of a facility admin"""

	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password']
		widgets = {
			'password': PasswordInput()
		}

class CustomFacilityAdminForm(ModelForm):
	"""Form that create the custom user fields for this application"""

	class Meta:
		model = user
		fields = ['is_facility_administrator', 'is_publisher']

class FacilityForm(ModelForm):
	"""Form that defines facility creation """

	class Meta:
		model = facility
		fields = '__all__'

