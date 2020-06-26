from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# from django.contrib.auth import get_user_model
# Create your models here.


class User(AbstractUser):
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follower')
    pass
    # user_set이 새로 칼럼 생성되서 이름을 follower로 변화
    # 필수로 넣어두고 작업을 하기 :)