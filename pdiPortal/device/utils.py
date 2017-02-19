from .models import Device


def get_device_list(user):
    """This function takes a user object as an input and returns a list of the
     devices associated with that user"""
    device_list = []
    if user.is_superuser:
        device_list = Device.objects.all().order_by("androidId").order_by("heartbeat")
    elif user.is_facility_administrator:
        facilities = user.facility.all()
        for one_facility in facilities:
            device_objects = Device.objects.filter(
                facility=one_facility
                ).order_by("androidId").order_by("heartbeat")
            for single_device in device_objects:
                device_list.append(single_device)
    else:
        device_list = Device.objects.filter(user=user).order_by("androidId").order_by("heartbeat")

    return device_list

