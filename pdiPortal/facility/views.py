from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from  django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import DefaultFacilityAdminForm, CustomFacilityAdminForm, FacilityForm

# Create your views here.
@login_required
def create(request):
	if request.method == "POST":
		defaultForm = DefaultFacilityAdminForm(request.POST)
		customForm = CustomFacilityAdminForm(request.POST)
		facilityForm = FacilityForm(request.POST)
		if facilityForm.is_valid() and defaultForm.is_valid() and customForm.is_valid():
			facility = facilityForm.save()
			default_user = defaultForm.save()
			facility_admin = customForm.save(commit=False)
			facility_admin.user=default_user
			facility_admin.facility = facility
			facility_admin.save()
			return redirect('dashboard')
	
	default_form = DefaultFacilityAdminForm()
	custom_form = CustomFacilityAdminForm()
	facility_form = FacilityForm()
	context = {'defaultForm': default_form, 'customForm': custom_form, 'facilityForm': facility_form}
	template = 'management/create_facility_admin.html'
	return render(request, template, context)

