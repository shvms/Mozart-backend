from rest_framework import serializers
from actstream.models import Action
from django.contrib.auth import get_user_model

from user_management.serializers import UserProfileSerializer
from playlist.serializers import SongSerializer
from playlist.models import Song

UserModel = get_user_model()

class GenericRelatedField(serializers.Field):
  def to_representation(self, value):
    if isinstance(value, UserModel):
      return UserProfileSerializer(value, context={'request':None}).data
    if isinstance(value, Song):
      return SongSerializer(value).data
    return str(value)

class ActionSerializer(serializers.ModelSerializer):
  """
  Action Serializer for serializing action models for user feeds.
  """
  
  actor = GenericRelatedField(read_only=True)
  target = GenericRelatedField(read_only=True)
  action_object = GenericRelatedField(read_only=True)
  
  class Meta:
    model = Action
    fields = '__all__'
