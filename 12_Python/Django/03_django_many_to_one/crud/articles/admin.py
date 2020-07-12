from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'content', 'created_at',]
    list_editable = ['title']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
# admin site에 등록(register) 하겠다.