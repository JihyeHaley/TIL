from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


# post_set = FK => (어떤 유저가 작성한 글들)
# post_set = M2M => (어떤 유저가 좋아요 버튼을 누른 글들)
# related_name을 통해서 like_posts로 바꿔서 
# 두개의 이름이 똑가아서 충돌
 
class Post(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField()
    image = ProcessedImageField(
        processors=[ResizeToFit(500, 500)],
        format='JPEG',
        options={
            'quality': 60})
            

    # user.like_posts -> 이 유저가 좋아유를 누른 "포스트들"
    # post.like_users -> 이 포스트를 좋아하는 "유저들"

    # user = 작성한 사람을 저장하기 위한
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 좋아요를 누른 사람을 가져올 콜롬을 만들기
    # like_user = 좋아요 버튼을 누른사람들을 저장
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')

    class Meta:
        ordering = ['-id']