# Import Modules
from django.contrib import admin
from django.urls import path, include
# Import rest_framework routers
from rest_framework import routers
# Import from Simple JSON Web Token the functions to obtain tokens
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

# Import ViewSets
from backend_alike_app.views import UserProfileViewSet, PostViewSet, CommentViewSet, SignupView, LoginView, GrabProfile

# Register Routers
router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet)
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)

# Define Url Paths
urlpatterns = [
    # API root
    path('', include(router.urls)),
    # admin panel
    path('admin/', admin.site.urls),
    path('signup', SignupView.as_view()),
    path('login', LoginView.as_view()),
    path('profile', GrabProfile.as_view())
    ]
    # # obtain pair view token path
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # # obtain refresh token path
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
