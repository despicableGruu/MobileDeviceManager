from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def publisher(request):
	user = request.user
	context = {'user': user}
	template = 'publisher/publisher.html'
	if user.user.is_publisher or user.is_superuser:
		return render(request, template, context)
	else:
		return redirect('/dashboard')

