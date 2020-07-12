from django.db import models
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 80}
        )


