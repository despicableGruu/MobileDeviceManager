"""
This is the views for the publisher application.
"""

from django.contrib.admin.views.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .forms import CreateApplicationForm

# Create your views here.
@login_required
def publisher(request):
    """This is the home page for the publisher. It shows the """
    user = request.user
    context = {'user': user}
    template = 'publisher/publisher.html'
    if user.is_publisher or user.is_superuser:
        return render(request, template, context)
    else:
        return redirect('dashboard')


class CreateApplication(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        View):
    """Views required for application creation."""
    permission_required = "auth.add_Application"

    def get(self, request):
        """This shows the form for creating a new application"""
        user = request.user
        if user.is_publisher or user.is_superuser:
            app_form = CreateApplicationForm()
            context = {'user': user, 'appForm': app_form}
            template = 'publisher/create_application.html'
            return render(request, template, context)
        else:
            return redirect('dashboard')

    def post(self, request):
        """This will process the form when submitted."""
        application_form = CreateApplicationForm(request.POST)
