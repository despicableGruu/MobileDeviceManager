from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
	template = 'device.html'
	return render(request, template, context)
	
@login_required
def register_device(request):
	if request.method == "POST":
		# TODO: Check for authentication.
		# TODO: If authenticated, verify form values.
		# TODO: If form is valid, store the device in the db and return a 200
		user = request.user


	else:
		# TODO: Throw an error and return a 404
		raise Http404("Not a valid request.")