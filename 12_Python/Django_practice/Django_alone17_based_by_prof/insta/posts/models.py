from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, ResizeToFill

# Create your models here.
# class User:
    # post_set = FK => 어떤유저가 작성한 글들 
    # like_posts = M2M => 어떤유저가 좋아요 버튼 누른 글들


class Post(models.Model):
    # 좋아요 버튼을 누른사람들을 저장
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    content = models.CharField(max_length=200)
    # 작성한 사람을 저장
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField()
    image = ProcessedImageField(upload_to='media',
                                processors=[ResizeToFill(500, 500)],
                                format='JPEG',
                                options={'quality': 60})
    class Meta:
        ordering = ['-id']
