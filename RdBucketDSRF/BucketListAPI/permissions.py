from .models import BucketList
from rest_framework.permissions import BasePermission, IsAdminUser


class Owner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, BucketList):
            return obj.owner == request.user
        return obj.owner == request.user


class Admin(IsAdminUser):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser
