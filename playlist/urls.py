from django.urls import path

from .views import SongCreateAPIView, SongListAPIView, SongDestroyAPIView

urlpatterns = [
  path('song/', SongCreateAPIView.as_view(), name='song-create'),
  path('song/<int:pk>/', SongDestroyAPIView.as_view(), name='song-destroy'),
  path('user/<str:username>/playlist/', SongListAPIView.as_view(), name='playlist'),
]
