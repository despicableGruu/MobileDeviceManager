from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from application.models import Application

# Create your views here.
def store(request):
	user = request.user
	application_list = Application.objects.all()
	context = {'user': user, 'application_list': application_list}
	template = 'store/store.html'
	return render(request, template, context)

@login_required
def appPage(request, app_name):
	user = request.user
	try:
		appName = Application.get(name = app_name)
	except App.DoesNotExist:
		raise Http404("App does not exist.")
	context = {'user': user, 'app': appName}
	template = 'mobileApp.html'
	return render(request, template, context)