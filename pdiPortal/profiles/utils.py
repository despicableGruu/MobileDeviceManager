from .models import PortalUser

def facilities_match(user_facilities, requested_user_facilities):
    """TODO: Docstring"""
    for user_facility in user_facilities:
        if user_facility in requested_user_facilities:
            return True
    return False


def validate_password(password1, password2):
    """Validates that two passwords are the same."""
    if password1 == password2:
        return True
    else:
        return False

def get_user_list(user):
    user_list = []
    if user.is_superuser:
            user_list = PortalUser.objects.all()
    elif user.is_facility_administrator:
        facilities = user.facility.all()
        for one_facility in facilities:
            user_objects = PortalUser.objects.filter(facility=one_facility)
            for user_item in user_objects:
                user_list.append(user_item)
    return user_list