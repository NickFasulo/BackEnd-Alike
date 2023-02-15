# Import Modules
from django.shortcuts import render
from rest_framework import viewsets

# Import Models and Serializers
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from .models import User, Post, Comment

# User View Set
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Post View Set
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Comment View Set
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer