from rest_framework.permissions import BasePermission
from .models import Program


class IsOwner(BasePermission):
    """Custom permission class to allow only Program owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the Program owner."""
        if isinstance(obj, Program):
            return obj.owner == request.user
        return obj.owner == request.user