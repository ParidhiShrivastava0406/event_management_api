from rest_framework import permissions
class IsInvitedOrPublic(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.organizer == request.user:
            return True
        
        if obj.is_public:
            return True

        return obj.rsvp_set.filter(user=request.user).exists()

class IsOrganizerOrReadOnly(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.organizer == request.user
