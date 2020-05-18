from rest_framework import permissions
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class IsSelfOrReadOnly(permissions.BasePermission):
  """
  Allows SAFE methods to be bypassed without authentication.
  Mainly used to let only account user to update or delete profile.
  """
  def has_permission(self, request, view):
    if request.method in permissions.SAFE_METHODS:
      return True

    user = UserModel.objects.get(username=view.kwargs['username'])
    return user == request.user
