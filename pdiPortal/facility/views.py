from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from  django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, HttpResponseServerError
from .forms import FacilityForm, UserForm
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def validate_password(password1, password2):
	logger.error('Validating Passwords.')
	if(password1 == password2):
		return True
	else:
		return False

# Create your views here.
decorator = [login_required, staff_member_required]

@method_decorator(decorator, name='dispatch')
class create_facility_admin(View):
	def post(self, request):
		# Maybe I should refactor this to just have an email and facility input and then behind the scene.
		# I would generate an email with a registration link for the person to create their profile.
		defaultForm = UserForm(request.POST)
		facilityForm = FacilityForm(request.POST)
		logger.error(facilityForm)
		if facilityForm.is_valid() and defaultForm.is_valid() and validate_password(request.POST['password1'], request.POST['password2']):
					facility_admin = defaultForm.save(commit=False)
					facility_admin.email = request.POST['email']
					facility_admin.set_password(request.POST['password1'])
					facility_admin.is_facility_administrator = True
					facility_admin.save()
					facility = facilityForm.save()
					facility_admin.facility.add(facility)
					# TODO: send a verification email to the user to create their account.
					return redirect('dashboard')

	def get(self, request):
		default_form = UserForm()
		facility_form = FacilityForm()
		context = {'defaultForm': default_form, 'facilityForm': facility_form}
		template = 'management/users/create_facility_admin.html'
		return render(request, template, context)

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_superuser or u.is_facility_administrator, redirect_field_name='dashboard'), name='dispatch')
class create_user(View):
	"""View used to create a new user by a facility administrator"""

	def post(self, request):
		# Maybe I should refactor this to just have an email and facility input and then behind the scene.
		# I would generate an email with a registration link for the person to create their profile.
		user = request.user
		defaultForm = UserForm(request.POST)
		if defaultForm.is_valid() and validate_password(request.POST['password1'], request.POST['password2']):
			facility_user = defaultForm.save(commit=False)
			facility_user.email = request.POST['email']
			facility_user.set_password(request.POST['password1'])
			facility_user.save()
			creator_facilities = user.facility.all()
			for creator_facility in creator_facilities:
				facility_user.facility.add(creator_facility)
			# TODO: send a verification email to the user to create their account.
			return redirect('dashboard')

	
	def get(self, request):
		default_form = UserForm()
		context = {'defaultForm': default_form}
		template = 'management/users/create_user.html'
		return render(request, template, context)
