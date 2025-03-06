# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    class Meta:
      ordering = ['id']
    def __str__(self):
        return f"{ self.first_name } { self.last_name }"
