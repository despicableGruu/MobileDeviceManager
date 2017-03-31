from .models import Device, DeviceModel


def get_device_list(user):
    """This function takes a user object as an input and returns a list of the
     devices associated with that user"""
    device_list = []
    if user.is_superuser:
        device_list = Device.objects.all().order_by("androidId").order_by("heartbeat")
    elif user.is_facility_administrator:
        device_list = Device.objects.filter(
            facility=user.facility
            ).order_by("androidId").order_by("heartbeat")
    else:
        device_list = Device.objects.filter(user=user).order_by("androidId").order_by("heartbeat")

    return device_list

def check_device_model_exists(model):
    """
    This function checks to see if the device's model
    exists in the DeviceModel table, and if not creates it.
    """
    DeviceModel.objects.get_or_create(device_model=model)

