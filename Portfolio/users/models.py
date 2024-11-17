from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=255, choices=[('admin', 'Admin'), ('user', 'User')], default='user')
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

