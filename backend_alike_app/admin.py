# Import django's admin 
from django.contrib import admin

# Import User, Post, Comment models
from .models import User, Post, Comment

# Registers our models for use on the backend panel (/user, /post, /comment, /admin)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
