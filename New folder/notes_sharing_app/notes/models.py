

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
