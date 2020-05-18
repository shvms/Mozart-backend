from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from actstream.actions import follow, unfollow
from actstream.models import followers, following, user_stream

from user_management.serializers import UserShortSerializer
from .serializers import ActionSerializer

UserModel = get_user_model()

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def follow_view(request, user_id):
  """
  View to add follow user with id=user_id.
  """
  if user_id == request.user.id:
    return Response({"error": "Can't follow your own self."}, status=status.HTTP_400_BAD_REQUEST)
  
  to_follow = get_object_or_404(UserModel.objects.all(), pk=user_id)
  follow(request.user, to_follow)
  return Response({"message": f"{request.user.username} follows {to_follow.username}"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_view(request, user_id):
  """
    View to unfollow follow user with id=user_id.
  """
  to_unfollow = get_object_or_404(UserModel.objects.all(), pk=user_id)
  unfollow(request.user, to_unfollow)
  return Response({"message": f"{request.user.username} unfollowed {to_unfollow.username}"},
                  status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def followers_view(request):
  """
  View to show a list of followers of the current user.
  """
  f = followers(request.user)
  serializer = UserShortSerializer(instance=f, context={'request': request}, many=True)

  return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def following_view(request):
  """
  View to show a list of users the current user is following.
  """
  f = following(request.user)
  serializer = UserShortSerializer(instance=f, context={'request': request}, many=True)
  
  return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def feed_view(request):
  """
  View to generate feeds for the current user.
  """
  f = user_stream(request.user)
  f = f.filter(verb='posted')
  serializer = ActionSerializer(instance=f, many=True)
  
  return Response(serializer.data)
