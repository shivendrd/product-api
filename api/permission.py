from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """_summary_

    Args:
        permissions (_type_): _permission authorized to only owner_
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user