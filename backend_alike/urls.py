# Import Modules
from django.contrib import admin
from django.urls import path, include
# Import rest_framework routers
from rest_framework import routers

# Import ViewSets
from backend_alike_app.views import UserProfileViewSet, PostViewSet, CommentViewSet, SignupView, LoginView, GrabProfile, AllPost_ViewSet

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
    # signup
    path('signup', SignupView.as_view()),
    # login
    path('login', LoginView.as_view()),
    # grab profile
    path('profile', GrabProfile.as_view()),
    path('posts', AllPost_ViewSet.as_view())
    ]
