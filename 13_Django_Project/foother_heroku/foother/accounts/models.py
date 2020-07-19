from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings


class User(AbstractUser):
    user_phone = models.CharField(max_length=13)
    user_created = models.DateTimeField(auto_now_add=True)
    user_score = models.IntegerField(default=0)
    user_profile_image = ProcessedImageField(
                    upload_to = 'user_profile_image',
                    processors=[ResizeToFill(500, 500)],
                    format='JPEG',
                    options={
                        'quality': 70},
                    default='default.png'
    )
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')

    user_intro = models.CharField(max_length=40)
    # class Meta:
    #     ordering = ['-score']
    