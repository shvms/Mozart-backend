from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (follow_view, unfollow_view,
                    followers_view, following_view, feed_view)

urlpatterns = [
  path('follow/<int:user_id>/', follow_view, name='follow-view'),
  path('unfollow/<int:user_id>/', unfollow_view, name='unfollow-view'),
  path('followers/', followers_view, name='followers-view'),
  path('following/', following_view, name='following-view'),
  path('feed/', feed_view, name='feed-view'),
]
