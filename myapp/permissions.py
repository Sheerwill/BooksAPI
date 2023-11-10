from rest_framework import permissions

class IsStorekeeper(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Check if the user is in the 'shopkeepers' group        
        return request.user.groups.filter(name='storekeepers').exists()
    
class IsShopkeeper(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Check if the user is in the 'shopkeepers' group        
        return request.user.groups.filter(name='storekeepers').exists()
    
class IsLibrarian(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Check if the user is in the 'shopkeepers' group        
        return request.user.groups.filter(name='librarians').exists()