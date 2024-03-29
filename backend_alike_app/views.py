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


# Signup View Set
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
        
# Login View Set
class LoginView(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self,request):
        data = self.request.data
        username = data["username"]
        password = data["password"]
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return Response({"success": "User authenticated",
                                    "token": AuthToken.objects.create(user)[1]})
            else:
                return Response({"error": "Error Authenticating"})
        except:
            return Response({"error": "Something went wrong when logging in"})

# Grab Profile View Set
class GrabProfile(APIView):
    def get(self, request):
        try:
            user = self.request.user
            profile = UserProfile.objects.get(user=user)
            profile_json = UserProfileSerializer(profile)
            return Response({"profile": profile_json.data})
        except:
            return Response({"error": "User profile not found"})


# User View Set
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# Post View Set
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AllPost_ViewSet(APIView):
    permission_classes = [
        permissions.AllowAny
    ]
    def post(self,request):
        try:
            user = self.request.user
            isAuthenticated = user.is_authenticated
            if isAuthenticated:
                image = request.data['image']
                github_link = request.data['github_link']
                project_name = request.data['project_name']
                username = UserProfile.objects.get(user=user)
                Post.objects.create(username=username, image=image, github_link=github_link, project_name=project_name)
                return Response({'message': "Post Successfully Created"})
            else:
                return Response({'error': "Not authenticated to create post; include an authentication token"})
        except Exception as e:
            print("Error", e)
            return Response({'error': "Error: Invalid body"})
    def get(self, request): 
        try:
            results = Post.objects.all()
            all_post = PostSerializer(results, many=True)
            return Response(all_post.data)
        except:
            return Response({"error": "Something went wrong"})
  
class OnePost_ViewSet(APIView):
    permission_classes = [
        permissions.AllowAny
    ]
    def get(self, request,id):
        try:
            post_results = Post.objects.get(id=id)
            post = PostSerializer(post_results)
            comments_results = Comment.objects.filter(post=id)
            comments = CommentSerializer(comments_results, many=True)
            
            return Response({"post": post.data, "comments": comments.data})
        except Exception as e:  
            print("Error getting One Post:", e)
            return Response({"error": "Something went wrong"})
                
    def put(self, request, id):
        try:
            user = self.request.user
            # postId = self.request.id
            isAuthenticated = True
            if isAuthenticated:
                image = request.data['image']
                github_link = request.data['github_link']
                project_name = request.data['project_name']
                heartQty = request.data['heartQty']
                userProfile = UserProfile.objects.get(user=user)
                post = Post.objects.get(id=id)
                userId = userProfile.id
                userPost = post.username
                if str(userPost) == str(userPost):
                    post.image = image
                    post.github_link = github_link
                    post.project_name = project_name
                    post.heartQty = heartQty
                    post.save()
                    res = f'Post {id} successfully updated'
                    return Response({'message': res})
                
                else:
                    res2 = f'userId: {userId}, userPost: {userPost}, You are not authorized to update this post'
                    return Response({'message': res2})
            else:
                return Response({'error': "Not Authenticated make sure you include a token"})
        except:
            return Response({'error': "Error: Invalid Body"})
        
    def delete(self, request, id):
        try:
            user = self.request.user
            isAuthenticated = user.is_authenticated
            if isAuthenticated:
                userProfile = UserProfile.objects.get(user=user)
                Posts = Post.objects.get(id=id)
                userId = userProfile.id
                userPost = Posts.username
                if str(userId) == str(userPost):
                    Posts.delete()
                    return Response({'message': "Post Successfully Deleted!!"})
                else:
                    res = f'userId: {userId}, userPost: {userPost}, userProfile: {userProfile}, Posts: {Posts} You are not authorized to delete this post'
                    return Response({'message': res})
            else:
                return Response({'error': "Not Authenticated make sure you include a token"})
        except:
            return Response({'error': "Error: Invalid Body"})


# Comment View Set
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

