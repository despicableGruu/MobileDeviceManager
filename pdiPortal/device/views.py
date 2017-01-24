from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.http import Http404

# Create your views here.
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