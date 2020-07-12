from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'content', 'created_at', 'updated_at', 'test']
    list_editable = ['title']
admin.site.register(Article, ArticleAdmin)
# admin site에 등록(register)하겠다.