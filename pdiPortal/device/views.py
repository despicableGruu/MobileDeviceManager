from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.http import Http404
from .models import Device
from profiles.models import PortalUser

# Create your views here.
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

@login_required
def device(request):
	user = request.user
	device = request.deviceId
	context = {
		'user': user,
		'device': device
	}
	template = 'management/devices/device.html'
	return render(request, template, context)
	
class register_device(View):
	def post(self, request):
		# TODO: Convert JSON data to dictionary
		# TODO: Confirm account.
		# TODO: Clean form.
		# TODO: If form is valid, store the device in the db and return a 200
		user = request.user