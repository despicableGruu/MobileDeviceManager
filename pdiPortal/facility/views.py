from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from  django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import BasicUserForm, CustomUserForm, FacilityForm

# Create your views here.
@login_required
def create_facility_admin(request):
  	
	# Maybe I should refactor this to just have an email and facility input and then behind the sceens
	# I would generate an email with a registration link for the person to create their profile. 
	if request.method == "POST":
		defaultForm = BasicUserForm(request.POST)
		customForm = CustomUserForm(request.POST)
		facilityForm = FacilityForm(request.POST)
		if facilityForm.is_valid() and defaultForm.is_valid() and customForm.is_valid():
			facility = facilityForm.save()
			default_user = defaultForm.save(commit=False)
			# TODO: create a random password and save it.
			default_user.save()
			facility_admin = customForm.save(commit=False)
			facility_admin.user = default_user
			facility_admin.facility = facility
			facility_admin.is_facility_administrator = True
			facility_admin.save()
			# TODO: send a verification email to the user to create their account.
			return redirect('dashboard')
	
	default_form = BasicUserForm()
	custom_form = CustomUserForm()
	facility_form = FacilityForm()
	context = {'defaultForm': default_form, 'customForm': custom_form, 'facilityForm': facility_form}
	template = 'management/create_facility_admin.html'
	return render(request, template, context)

@login_required
def create_user(request):
	"""View used to create a new user by a facility administrator"""
	user = request.user
	if request.method == "POST":
		basicForm = BasicUserForm(request.POST)
		customForm = CustomUserForm(request.POST)
		if basicForm.is_valid() and customForm.is_valid():
  			django_user = basicForm.save(commit=False)

