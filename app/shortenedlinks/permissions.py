from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and
            request.user.is_authenticated and obj.User == request.user
        )
