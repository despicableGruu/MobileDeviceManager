from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission for reading device lists through the API endpoint.
    """

    def has_object_permission(self, request, view, obj):
        """Confirm that the user has the permission to see the object."""
        return obj.owner == request.user or request.user.is_superuser
