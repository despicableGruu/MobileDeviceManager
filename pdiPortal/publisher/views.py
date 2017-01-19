from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CreateApplicationForm

# Create your views here.
@login_required
def publisher(request):
	user = request.user
	context = {'user': user}
	template = 'publisher/publisher.html'
	if user.is_publisher or user.is_superuser:
		return render(request, template, context)
	else:
		return redirect('dashboard')

@login_required
def create_application(request):
	user = request.user
	if user.is_publisher or user.is_superuser:
		app_form = CreateApplicationForm()
		context = {'user': user, 'appForm': app_form}
		template = 'publisher/create_application.html'
		return render(request, template, context)
	else:
		return redirect('dashboard')
