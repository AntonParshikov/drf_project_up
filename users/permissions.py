from rest_framework import permissions
from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    message = "Вы не являетесь модератором!"
    def has_permission(self, request, view):
        if request.user.role == UserRoles.moderator:
            return True
        return False


class IsBuyer(BasePermission):
    message = "Вы не являетесь владельцем!"
    def has_object_permission(self, request, view, obj):
        if request.user == obj.buyer:
            return True
        return False
