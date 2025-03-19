from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class CustomUser(AbstractUser):
    # username = models.CharField(max_length=100)
    username = None
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile_image = models.ImageField(upload_to="profile")

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

