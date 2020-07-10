from django.contrib import admin
from .models import User
# Register your models here.
# from django.contrib.auth import get_user_model

# class UserAdmin(admin.ModelAdmin):
#     class Meta:


admin.site.register(User)