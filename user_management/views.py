from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .serializers import UserSerializer, UserProfileSerializer
from .permissions import IsSelfOrReadOnly

UserModel = get_user_model()


# Create your views here.
class RegistrationAPIView(APIView):
  """
  Registration View. Accessible to anonymous users.
  Signs in the user after successful signup by manually generating access & refresh tokens.
  """
  serializer_class = UserSerializer
  permission_classes = [permissions.AllowAny, ]
  
  def post(self, request):
    serializer = self.serializer_class(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    
    return Response(data=get_tokens_for_user(user), status=status.HTTP_201_CREATED)


def get_tokens_for_user(user):
  """
  Returns access and refresh token.
  :param user: user for which access tokens generated
  :return: A dictionary of access & refresh tokens
  """
  refresh = RefreshToken.for_user(user)
  
  return {
    'refresh': str(refresh),
    'access': str(refresh.access_token)
  }

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
  """
  View for viewing, updating and deleting user
  in their own rights.
  """
  
  lookup_field = 'username'
  queryset = UserModel.objects.all()
  serializer_class = UserProfileSerializer
  permission_classes = [IsSelfOrReadOnly, ]
  
  @method_decorator(cache_page(60*10))
  def dispatch(self, request, *args, **kwargs):
    return super(UserViewSet, self).dispatch(request, *args, **kwargs)
