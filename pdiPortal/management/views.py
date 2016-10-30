from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from allauth.account.views import PasswordChangeView
from device.models import Device
from django.contrib.auth.admin import User

# Create your views here.
def home(request):
	context = {}
	template = 'home.html'
	return render(request, template, context)

@login_required
def dashboard(request):
	user = User.objects.filter(username=request.user)[0]
	device_list = Device.objects.filter(user=user).order_by("androidId").order_by("heartbeat")
	if user.is_superuser:
		device_list = Device.objects.all().order_by("androidId").order_by("heartbeat")
	elif user.user.is_facility_administrator:
		device_list = Device.objects.filter(facility = user.user.facility).order_by("androidId").order_by("heartbeat")
	context = {'user': user, 'device_list': device_list[:10]}
	template = 'management/dashboard.html'
	return render(request, template, context)

@login_required
def devices(request):
	user = User.objects.filter(username=request.user)[0]
	device_list = Device.objects.filter(user=user).order_by("androidId").order_by("heartbeat")
	if user.is_superuser:
		device_list = Device.objects.all().order_by("androidId").order_by("heartbeat")
	elif user.user.is_facility_administrator:
		device_list = Device.objects.filter(facility = user.user.facility).order_by("androidId").order_by("heartbeat")
	context = {'user': user, 'device_list': device_list}
	template = 'management/device_list.html'
	return render(request, template, context)

@login_required
def users(request):
	user = request.user
	user_list = User.objects.all()
	context = {'user': user, 'user_list': user_list}
	template = 'management/users.html'
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
	template = 'management/policies.html'
	return render(request, template, context)

class custom_password_change(PasswordChangeView):
	"""docstring for custom_password_change"""
	@property
	def success_url(self):
		return reverse_lazy('dashboard')

dashboard_after_password_change = login_required(custom_password_change.as_view())