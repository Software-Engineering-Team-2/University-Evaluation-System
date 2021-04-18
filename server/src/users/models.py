# models.py in the users Django app
from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPES = [('S', 'Student'), ('I', 'Instructor')]

class CustomUser(AbstractUser):
    # We don't need to define the email attribute because is inherited from AbstractUser
    usertype = models.CharField(max_length=20, choices=USER_TYPES, default='S')
    verified = models.BooleanField(default=False)