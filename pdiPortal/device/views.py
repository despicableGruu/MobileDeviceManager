from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
