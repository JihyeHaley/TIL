from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Review(models.Model):
    # hidden
    lat = models.FloatField()
    lng = models.FloatField()
    restaurant_address = models.CharField(max_length=30)

    # TextInput_readonly
    restaurant_name = models.CharField(max_length=30)

    # TextInput
    food_name = models.CharField(max_length=30)
    
    # Textarea
    food_review = models.CharField(max_length=30)
    
    #손봐야할 거
    food_star = models.IntegerField()

    food_image = ProcessedImageField(
                upload_to='upload_photo',
                processors=[ResizeToFill(200, 200)],
                format='JPEG',
                options={
                    'quality': 80}
    )
    
    visit_date = models.DateField(auto_now_add=False)

    food_kind = models.CharField(max_length=10)

    # ForeignKey
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    
    class Meta:
        ordering = ['-id']


class Comment(models.Model):
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='which_review')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='which_user')

    class Meta:
        ordering = ['-created_at']