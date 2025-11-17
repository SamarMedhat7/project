from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
    )
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=10)