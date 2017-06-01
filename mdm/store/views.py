from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from publisher.models import Application

# Create your views here.
def store(request):
    """TODO: Docstring"""
    user = request.user
    application_list = Application.objects.all()
    context = {'user': user, 'application_list': application_list}
    template = 'store/store_home.html'
    return render(request, template, context)

def app_page(request, app_id):
    """TODO: Docstring"""
    user = request.user
    try:
        app = Application.get(_id=app_id)
    except Application.DoesNotExist:
        raise Http404("App does not exist.")
    context = {'user': user, 'app': app}
    template = 'mobileApp.html'
    return render(request, template, context)

def app_list(request):
    """TODO: Docstring"""
    user = request.user
    application_list = Application.objects.all()
    context = {'user': user, 'application_list': application_list}
    template = 'store/application_list.html'
    return render(request, template, context)
