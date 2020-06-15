from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    #auto_now_add = 최초 생성 일자
    updated_at = models.DateTimeField(auto_now=True)

