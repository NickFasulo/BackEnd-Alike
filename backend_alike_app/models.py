# import modules
from django.db import models

# User model
class User(models.Model):
    # Datafields
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
    image = models.URLField()
    github_link = models.URLField()
    project_name = models.CharField(max_length = 30)
    likes = models.IntegerField(default = 0)
    # Links to User model
    username = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posts')

    # Return project name
    def __str__(self):
        return f'{self.project_name}'

# Comment model
class Comment(models.Model):
    # Datafields
    username = models.CharField(max_length = 30)
    comment = models.CharField(max_length = 255)
    likes = models.IntegerField(default = 0)
    # Links to Post model
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')

    # Return username
    def __str__(self):
        return f'{self.username}'

