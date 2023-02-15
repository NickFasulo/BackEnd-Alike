# Import Modules
from django.shortcuts import render
from django.contrib import auth
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from knox.models import AuthToken

# Import Models and Serializers
from .serializers import UserSerializer, UserProfileSerializer, PostSerializer, CommentSerializer
from .models import UserProfile, Post, Comment

# User View Set
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class LoginView(APIView):
  permission_classes = [
    permissions.AllowAny
  ]

  def post(self, request):
    data = self.request.data
    username = data["username"]
    password = data["password"]
    try:
      user = auth.authenticate(username = username, password = password)
      if user is not None:
          auth.login(request, user)
          return Response({"success": "User authenticated",
                            "token": AuthToken.objects.create(user)[1]})
      else:
          return Response({"error": "Error Authenticating"})
    except:
        return Response({"error": "Something went wrong when logging in"})

# Post View Set
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Comment View Set
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer