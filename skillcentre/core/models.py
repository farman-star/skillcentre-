
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    interests = models.TextField(blank=True)

class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    views = models.PositiveIntegerField(default=0)
    emotion_tag = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=True)

# Projects
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    views= models.PositiveIntegerField(default =0)
    created_at = models.DateTimeField(auto_now_add=True)

# Sketches
class Sketch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='sketches/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    diary = models.ForeignKey('DiaryEntry', on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True, blank=True)
