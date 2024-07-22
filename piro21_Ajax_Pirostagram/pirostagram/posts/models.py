from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()