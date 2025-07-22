from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Allows all users to read only.
    Only admins can write (POST, PUT, DELETE, PATCH).
    """

    def has_permission(self, request, view):
        return (
                request.method in SAFE_METHODS
                or request.user and request.user.is_staff
        )
