from rest_framework import permissions
from .models import *


class PermitAdminAccess(permissions.BasePermission):
    edit_methods = ('PUT','POST','DELETE')
    
    def has_permission(self, request, view):
       
        return request.user.is_superuser
      
    # def has_object_permission(self, request, view, obj):
    #     if request.user.SignUp_as == 'A':
    #         return True
       
        
        
#         if request.user and request.method in self.edit_methods:
            
#             return True
#         return False
      
# class PermitSuperuser(permissions.BasePermission):
    
#     def has_permission(self, request, view):
#         if request.user.is_authenticated:
#           return True
      
#     def IsAdminUser(self, request, view, obj):
#         if request.user.is_superuser:
#             return True
#         return False
        
    
