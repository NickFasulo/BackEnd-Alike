# Import Modules
from django.shortcuts import render
# Import Django Rest Framework
from rest_framework import viewsets
# Import Models and Serializers
from .serializers import UserProfileSerializer, PostSerializer, CommentSerializer
from .models import UserProfile, Post, Comment

# User View Set
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# Post View Set
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Comment View Set
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer