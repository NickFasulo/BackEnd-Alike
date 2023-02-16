# import modules
from django.db import models
# imports Django native User model
from django.contrib.auth.models import User

# UserProfile model
class UserProfile(models.Model):
    # Datafields
    # Linking our UserProfile model to Django's native User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    username = models.CharField(
      max_length = 30,
      unique = True
    )

    email = models.EmailField(
      max_length = 40,
      unique = True
      )

    # Return username
    def __str__(self):
        return f'{self.username}'

# Post model
class Post(models.Model):
    # Datafields
    image = models.URLField(max_length = 500)
    github_link = models.URLField(max_length = 500)
    project_name = models.CharField(max_length = 30)
    heartQty = models.IntegerField(default = 0)
    # Links to User model
    username = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name = 'posts')

    # Return project name
    def __str__(self):
        return f'{self.project_name}'

# Comment model - Built out for future implementation
class Comment(models.Model):
    # Datafields
    username = models.CharField(max_length = 30)
    comment = models.CharField(max_length = 255)
    heartQty = models.IntegerField(default = 0)
    # Links to Post model
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')

    # Return username
    def __str__(self):
        return f'{self.username}'

