from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from django.utils.decorators import method_decorator
from allauth.account.views import PasswordChangeView
from device.models import Device
from profiles.models import PortalUser
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def facilities_match(user_facilities, requested_user_facilities):
	for user_facility in user_facilities:
		if(user_facility in requested_user_facilities):
			return True
	return False

# Create your views here.
@login_required
def dashboard(request):
	user = request.user
	if user.is_superuser:
  		device_list = Device.objects.all().order_by("androidId").order_by("heartbeat")
	elif user.is_facility_administrator:
		facilities = user.facility.all()
		device_list = []
		for oneFacility in facilities:
			deviceObjects = Device.objects.filter(facility = oneFacility).order_by("androidId").order_by("heartbeat")
			for device in deviceObjects:
				device_list.append(device)
	else:
		device_list = Device.objects.filter(user=user).order_by("androidId").order_by("heartbeat")
	context = {'user': user, 'device_list': device_list[:10]}
	template = 'management/dashboard.html'
	return render(request, template, context)

@login_required
def reports(request):
	user = request.user
	context = {'user': user}
	template = 'management/reports.html'
	return render(request, template, context)

@login_required
def policies():
	user = request.user
	context = {'user': user}
	template = 'management/users/policies.html'
	return render(request, template, context)

class custom_password_change(PasswordChangeView):
	"""docstring for custom_password_change"""
	@property
	def success_url(self):
		return reverse_lazy('dashboard')

dashboard_after_password_change = login_required(custom_password_change.as_view())