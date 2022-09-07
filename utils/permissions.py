from rest_framework import permissions

from apps.users.models import User


class IsSubscriptionActive(permissions.BasePermission):
    def has_permission(self, request, view):
        user: User = request.user
        return user.is_subscription_active
