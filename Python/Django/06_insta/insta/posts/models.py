from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

# Create your models here.

class Post(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # image = models.ImageField()
    image = ProcessedImageField(
        upload_to='medai',
        processors=[ResizeToFit(500, 500)],
        format='JPEG',
        options={
            'quality': 60})

    # 좋아요를 누른 사람을 가져올 콜롬을 만들기
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ['-id']