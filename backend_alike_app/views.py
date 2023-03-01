# Import Modules
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.response import Response
from rest_framework import permissions
from knox.models import AuthToken

# Import Models and Serializers
from .serializers import UserSerializer, UserProfileSerializer, PostSerializer, CommentSerializer
from .models import UserProfile, Post, Comment

class SignupView(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self,request):
        result = User.objects.all()
        all_users = UserSerializer(result,many=True)
        return Response(all_users.data)
    def post(self,request):
        data = self.request.data
        username = data["username"]
        email = data["email"]
        password = data["password"]
        re_password = data["re_password"]
        try:
            if password == re_password:
                if User.objects.filter(username=username).exists():
                    return Response({"error": "Username already exists"})
                else:
                    user = User.objects.create_user(
                        username=username, password=password)
                    UserProfile.objects.create(user=user,email=email,username=username)
                    return Response({
                        "success": "User created successfully",
                        "token": AuthToken.objects.create(user)[1]
                    })
            else:
                return Response({"error": "Passwords do not match"})
        except:
            return Response({"error": "Something went wrong signing up"})


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