# Import Modules
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# Import Viewsets
from backend_alike_app.views import UserViewSet, PostViewSet, CommentViewSet

# Register Routers
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)

# Define Url Paths
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]