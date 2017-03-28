from .models import Device, DeviceModel, DeviceFacilityList


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

def check_device_model_exists(model):
    """
    This function checks to see if the device's model
    exists in the DeviceModel table, and if not creates it.
    """
    DeviceModel.objects.get_or_create(device_model=model)

def create_device_facility_records(device, user):
    """This function will create the initial entries in the DeviceFacilityList"""
    for single_facility in user.facility.all():
        DeviceFacilityList.objects.create(device=device, facility=single_facility)

def update_device_facility_records(device, user):
    """
    This function will remove all the rows associated with
    the device and update them to the latest user.
    """
    DeviceFacilityList.objects.filter(device=device).delete()
    create_device_facility_records(device, user)
