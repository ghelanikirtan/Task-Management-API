from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permissions(self, req, view):
        return req.method in permissions.SAFE_METHODS
    