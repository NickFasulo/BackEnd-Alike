from django.db import models

class User(models.Model):
    username = models.CharField(
      max_length = 30,
      unique = True
      )
    email = models.EmailField(
      max_length = 40,
      unique = True
      )

    def __str__(self):
        return f'{self.username}'

class Post(models.Model):
    image = models.URLField()
    github_link = models.URLField()
    project_name = models.CharField(max_length = 30)
    likes = models.IntegerField()
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f'{self.project_name}'

class Comments(models.Model):

    def __str__(self):
        return f'{self.project_name}'

