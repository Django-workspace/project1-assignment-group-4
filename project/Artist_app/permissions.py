from rest_framework.permissions import BasePermission, SAFE_METHODS

class is_Fan_Permission(BasePermission):
    messa='permission for the Fan only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
       