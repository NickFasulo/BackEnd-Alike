# Import Modules
from rest_framework import serializers
# Import Models
from .models import UserProfile, Post, Comment

# Serializers let us access data from the specific fields that we want within our models.

# User Serializer
class UserSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "username": instance.username,
            "password": instance.password,
        }

# UserProfile Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

# Post Serializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'