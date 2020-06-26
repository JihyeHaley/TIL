from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class User(AbstractUser):
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follower')
    
    image = ProcessedImageField(
        upload_to='profile_image',
        processors=[ResizeToFill(500, 500)],
        format='JPEG',
        options={
            'quality': 60},
        default='default.png')
    # user_set이 새로 칼럼 생성되서 이름을 follower로 변화
    # 필수로 넣어두고 작업을 하기 :)