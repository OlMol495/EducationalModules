from rest_framework import permissions

from users.models import UserRoles


class IsModerator(permissions.BasePermission):
    message = 'Это действие доступно только модератору'

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsOwner(permissions.BasePermission):
    message = 'Это действие доступно только владельцу'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsAdmin(permissions.BasePermission):
    message = 'Это действие доступно только админу'

    def has_permission(self, request, view):
        return request.user.is_staff
