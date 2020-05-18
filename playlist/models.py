from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from enum import Enum

UserModel = get_user_model()

class Platform(Enum):
  SPOTIFY = 1
  SOUNDCLOUD = 2


PLATFORM_CHOICES = [
  (Platform.SPOTIFY.value, 'Spotify'),
  (Platform.SOUNDCLOUD.value, 'SoundCloud')
]

class Song(models.Model):
  """
  Song model to store the uri and platform of different tracks in the main playlist.
  """
  uri = models.CharField(max_length=50, db_index=True, null=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='songs')
  platform = models.PositiveSmallIntegerField(choices=PLATFORM_CHOICES)
  added_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"{self.id}: {self.platform}"
  
  class Meta:
    ordering = ['-added_at']
