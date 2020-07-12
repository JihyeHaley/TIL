from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    title_en = models.CharField(max_length=50)
    audience = models.IntegerField()
    open_date = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Movie, on_delete=models.CASCADE)