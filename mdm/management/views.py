"""
This is the general dashboard view.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from allauth.account.views import PasswordChangeView
from device.models import Device
from device.utils import get_device_list


# Create your views here.
@login_required
def dashboard(request):
    """ Dashboard Docstring """
    user = request.user
    device_list = get_device_list(user)
    context = {'user': user, 'device_list': device_list[:10]}
    template = 'management/dashboard.html'
    return render(request, template, context)



@method_decorator(login_required, name='dispatch')
class CustomPasswordChange(PasswordChangeView):
    """docstring for custom_password_change"""
    @property
    def success_url(self):
        """ Where to redirect users on a successful password change. """
        return reverse_lazy('dashboard')
