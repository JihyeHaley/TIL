  
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class FoodCategory(models.Model):
    food_ctg = models.CharField(max_length=100)

    food_ctg_image = ProcessedImageField(
                upload_to='food_ctg_photo',
                processors=[ResizeToFill(200, 200)],
                format='JPEG',
                options={
                    'quality': 80},
                default='/img/ctg/chicken.png'
    )
    # selectbox로 설정
    # img = models.ImageField()
    # food_set 자동생김    


class FoodChoice(models.Model):
    food_name = models.CharField(max_length=100)
    food_ctgs = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    # food_by_emotion
    status = models.CharField(max_length=50,default="일반")