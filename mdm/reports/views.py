from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def reports(request):
    """ Reports Docstring """
    user = request.user
    context = {'user': user}
    template = 'management/reports.html'
    return render(request, template, context)
