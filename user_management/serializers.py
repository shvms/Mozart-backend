from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  """
  Used at the time of registration of users.
  """
  first_name = serializers.CharField(required=True)
  last_name = serializers.CharField(required=True)
  email = serializers.EmailField(required=True)
  
  def create(self, validated_data):
    user = UserModel.objects.create_user(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name'],
      password=validated_data['password']
    )
    user.save()
    
    return user
  
  class Meta:
    model = UserModel
    fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
    extra_kwargs = {
      'password': {'write_only': True},
      'id': {'read_only': True},
    }


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
  """
  User profile
  """
  playlist = serializers.HyperlinkedIdentityField(
    view_name='playlist',
    lookup_field='username',
    read_only=True
  )
  
  class Meta:
    model = UserModel
    fields = ['id', 'username', 'first_name', 'last_name', 'playlist']
    extra_kwargs = {
      'id': {'read_only': True},
      'username': {'read_only': True},
    }

class UserShortSerializer(serializers.HyperlinkedModelSerializer):
  """
  Short serialization required for follower/following views.
  """
  
  url = serializers.HyperlinkedIdentityField(
    view_name='user-detail',
    lookup_field='username',
    read_only=True
  )
  
  class Meta:
    model = UserModel
    fields = ['id', 'username', 'url']
    extra_kwargs = {
      'id': {'read_only': True},
      'username': {'read_only': True},
    }
