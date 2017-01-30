def facilities_match(user_facilities, requested_user_facilities):
    """TODO: Docstring"""
    for user_facility in user_facilities:
        if user_facility in requested_user_facilities:
            return True
    return False
