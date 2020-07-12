from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# 원래 있던 유저에서 새로운 유저로 가는 걸루
class User(AbstractUser):
    phone = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)

