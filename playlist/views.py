from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import Song
from .serializers import SongSerializer


class SongCreateAPIView(APIView):
  """
  Creates a new song post.
  """
  permission_classes = (IsAuthenticated,)
  serializer_class = SongSerializer
  queryset = Song.objects.all()

  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(user=request.user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


class SongListAPIView(APIView):
  """
  Lists down the songs in the playlist of the user. Anonymous view is permitted.
  """
  permission_classes = [AllowAny, ]
  serializer_class = SongSerializer
  queryset = Song.objects.all()
  
  def get(self, request, username):
    songs = Song.objects.filter(user__username=username)
    serializer = self.serializer_class(songs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  @method_decorator(cache_page(60*2))
  def dispatch(self, request, *args, **kwargs):
    return super(SongListAPIView, self).dispatch(request, *args, **kwargs)

class SongDestroyAPIView(DestroyAPIView):
  permission_classes = [IsAuthenticated, ]
  serializer_class = SongSerializer
  queryset = Song.objects.all()
