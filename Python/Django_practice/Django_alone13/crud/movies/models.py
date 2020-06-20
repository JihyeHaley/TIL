from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.CharField(max_length=20)
    audience = models.IntegerField()
    open_date = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=20)
    score = models.IntegerField()
    poster_url = models.CharField(max_length=20)
    description = models.TextField()