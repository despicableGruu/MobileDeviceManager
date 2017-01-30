from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View

from device.models import Device
from facility.forms import FacilityForm

from .models import PortalUser
from .forms import UserForm
from .utils import facilities_match



def validate_password(password1, password2):
    """Validates that two passwords are the same."""
    if password1 == password2:
        return True
    else:
        return False

# Create your views here.
@method_decorator(login_required, name='dispatch')
class Users(View):
    """TODO: Docstring"""

    def number_of_devices(self, user):
        """TODO: Docstring"""
        return Device.objects.filter(user=user).count()

    def number_of_devices_offline(self, user):
        """TODO: Docstring"""
        return Device.objects.filter(user=user, heartbeat=False).count()

    def get(self, request):
        """ TODO: Docstring """
        user = request.user
        user_list = []
        if user.is_superuser:
            user_list = PortalUser.objects.all()
        elif user.is_facility_administrator:
            facilities = user.facility.all()
            for one_facility in facilities:
                user_objects = PortalUser.objects.filter(facility=one_facility)
                for user_item in user_objects:
                    user_list.append(user_item)
        for user_item in user_list:
            user_item.number_of_devices = self.number_of_devices(user_item)
            user_item.devices_offline = self.number_of_devices_offline(user_item)
        context = {'user': user, 'user_list': user_list}
        template = 'management/users/users.html'
        return render(request, template, context)

@login_required
def user_configuration(request, username):
    """ TODO: Docstring """
    user = request.user
    requested_user = PortalUser.objects.filter(username=username)[0]
    if facilities_match(user.facility.all(), requested_user.facility.all()) or user.is_superuser:
        context = {'user': user, 'requested_user': requested_user}
        template = 'management/users/configuration.html'
        return render(request, template, context)
    else:
        return redirect('dashboard')


DECORATOR = [login_required, staff_member_required]

@method_decorator(DECORATOR, name='dispatch')
class CreateFacilityAdmin(View):
    """ TODO: Docstring """
    def post(self, request):
        """ TODO: Docstring """
		# Maybe I should refactor this to just have an email and facility input and then behind the scene.
		# I would generate an email with a registration link for the person to create their profile.
        default_form = UserForm(request.POST)
        facility_form = FacilityForm(request.POST)
        if (facility_form.is_valid()
                and default_form.is_valid()
                and validate_password(request.POST['password1'], request.POST['password2'])):
            facility_admin = default_form.save(commit=False)
            facility_admin.email = request.POST['email']
            facility_admin.set_password(request.POST['password1'])
            facility_admin.is_facility_administrator = True
            facility_admin.save()
            facility = facility_form.save()
            facility_admin.facility.add(facility)
            # TODO: send a verification email to the user to create their account.
            return redirect('dashboard')

    def get(self, request):
        """ TODO: Docstring """
        default_form = UserForm()
        facility_form = FacilityForm()
        context = {'defaultForm': default_form, 'facilityForm': facility_form}
        template = 'management/users/create_facility_admin.html'
        return render(request, template, context)

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_superuser or u.is_facility_administrator, redirect_field_name='dashboard'), name='dispatch')
class CreateUser(View):
    """View used to create a new user by a facility administrator"""

    def post(self, request):
        """ TODO: Docstring """
        # Maybe I should refactor this to just have an email and facility input and then behind the
        # scene I would generate an email with a registration link for the person to create
        # their profile.
        user = request.user
        default_form = UserForm(request.POST)
        if (default_form.is_valid() and
                validate_password(request.POST['password1'], request.POST['password2'])):
            facility_user = default_form.save(commit=False)
            facility_user.email = request.POST['email']
            facility_user.set_password(request.POST['password1'])
            facility_user.save()
            creator_facilities = user.facility.all()
            for creator_facility in creator_facilities:
                facility_user.facility.add(creator_facility)
            # TODO: send a verification email to the user to create their account.
            return redirect('dashboard')

    def get(self, request):
        """ TODO: Docstring """
        default_form = UserForm()
        context = {'defaultForm': default_form}
        template = 'management/users/create_user.html'
        return render(request, template, context)
