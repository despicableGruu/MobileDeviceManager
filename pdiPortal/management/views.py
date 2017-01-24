from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from django.utils.decorators import method_decorator
from allauth.account.views import PasswordChangeView
from device.models import Device
from facility.models import PortalUser
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
def devices(request):
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
	context = {'user': user, 'device_list': device_list}
	template = 'management/devices/device_list.html'
	return render(request, template, context)

@method_decorator(login_required, name='dispatch')
class devices_for_user(View):
	
	def get(self, request, username):
		user = request.user
		requested_username = username
		if user.is_superuser:
			if PortalUser.objects.filter(username = requested_username).count() == 0:
				return redirect('device-list')
			requested_user = PortalUser.objects.filter(username = requested_username)[0]
			device_list = Device.objects.filter(user = requested_user).order_by("androidId").order_by("heartbeat")
			if requested_user.first_name:
				requested_username = requested_user.first_name
		elif user.is_facility_administrator:
			if PortalUser.objects.filter(username = requested_username).count() == 0:
				return redirect('device-list')
			requested_user = PortalUser.objects.filter(username = requested_username)[0]
			facilities = user.facility.all()
			device_list = []
			for oneFacility in facilities:
				deviceObjects = Device.objects.filter(facility = oneFacility).order_by("androidId").order_by("heartbeat")
				for device in deviceObjects:
					device_list.append(device)
			if requested_user.first_name:
				requested_username = requested_user.first_name
		else:
			return redirect('dashboard')
		context = {'user': user, 'device_list': device_list, 'requested_username': requested_username}
		template = 'management/devices/device_list_for_user.html'
		return render(request, template, context)

@method_decorator(login_required, name='dispatch')
class users(View):
	
  def number_of_devices(self, user):
    return Device.objects.filter(user = user).count()

  def number_of_devices_offline(self, user):
    return Device.objects.filter(user = user, heartbeat = False).count()

  def get(self, request):
    user = request.user
    user_list = []
    if user.is_superuser:
      user_list = PortalUser.objects.all()
    elif user.is_facility_administrator:
      facilities = user.facility.all()
      for oneFacility in facilities:
        userObjects = PortalUser.objects.filter(facility = oneFacility)
        for userItem in userObjects:
          user_list.append(userItem)
    for user_item in user_list:
      user_item.number_of_devices = self.number_of_devices(user_item)
      user_item.devices_offline = self.number_of_devices_offline(user_item)
    context = {'user': user, 'user_list': user_list}
    template = 'management/users/users.html'
    return render(request, template, context)

@login_required
def user_configuration(request, username):
	user = request.user
	requested_user = PortalUser.objects.filter(username=username)[0]
	if facilities_match(user.facility.all(), requested_user.facility.all()) or user.is_superuser:
		context = {'user': user, 'requested_user': requested_user}
		template = 'management/users/configuration.html'
		return render(request, template, context)
	else:
		return redirect('dashboard')

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