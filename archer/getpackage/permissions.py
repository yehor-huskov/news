from rest_framework import permissions
from django.contrib.auth.models import User, Group

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        editor_group = Group.objects.get(name='editor')
        if editor_group in request.user.groups.all():
            return True

        return obj.author == request.user

