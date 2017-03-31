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
    """This function returns a list of users based on profile."""
    user_list = []
    if user.is_superuser:
        user_list = PortalUser.objects.all()
    elif user.is_facility_administrator:
        user_list = PortalUser.objects.filter(facility=user.facility)
    return user_list
