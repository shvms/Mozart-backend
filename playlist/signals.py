from django.db.models.signals import post_save
from django.dispatch import receiver
from actstream import action

from playlist.models import Song

@receiver(post_save, sender=Song)
def push_to_feed(sender, instance, created, **kwargs):
  action.send(instance.user, verb='posted', action_object=instance)   # for pushing song addition actions
