import logging

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from allauth.account.views import PasswordChangeView
from device.models import Device


# Create your views here.
@login_required
def dashboard(request):
    """ Dashboard Docstring """
    user = request.user
    logging.error("Test Log")
    device_list = []
    if user.is_superuser:
        logging.debug("Inside of the if statement.")
        device_list = Device.objects.all().order_by("android_id").order_by("heartbeat")
    elif user.is_facility_administrator:
        facilities = user.facility.all()
        for one_facility in facilities:
            device_objects = Device.objects.filter(facility=one_facility).order_by("android_id").order_by("heartbeat")
            for device in device_objects:
                device_list.append(device)
    else:
        device_list = Device.objects.filter(user=user).order_by("android_id").order_by("heartbeat")
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
