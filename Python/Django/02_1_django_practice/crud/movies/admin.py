from django.contrib import admin
from .models import Movie
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_en', 'audience', 'open_date', 'genre', 'watch_grade', 'score', 'poster_url', 'description']
    # 소괄호를 쓴 이유는 수정할 없어서서 
    
admin.site.register(Movie, MovieAdmin)
