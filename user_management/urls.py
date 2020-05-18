from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from .views import RegistrationAPIView
from .views import UserViewSet

router = DefaultRouter()
router.register("user", UserViewSet, basename="user")

urlpatterns = [
  path('auth/login/', TokenObtainPairView.as_view(), name='login-token-obtain-pair'),
  path('auth/login/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
  path('auth/register/', RegistrationAPIView.as_view(), name='registration-api-view'),
  path('', include(router.urls)),   # endpoints for accessing/updating/deleting profile with certain restrictions.
]
