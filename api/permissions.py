from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permissions(self, req, view, obj):
        if req.method in permissions.SAFE_METHODS:
            return True
        
        return obj.admin == req.user