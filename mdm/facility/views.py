import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Facility
from .serializers import FacilitySerializer


class FacilityCreateReadView(ListCreateAPIView):
    """ This is part of the Facility API where you can create new devices
    or return all of the devices. """

    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    lookup_field = 'id'


class FacilityReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """This is part of the API where you can Update, Read, or Delete a specific device."""
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    lookup_field = 'id'