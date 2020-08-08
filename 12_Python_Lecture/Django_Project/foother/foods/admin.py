from django.contrib import admin
from .models import FoodCategory, FoodChoice

# Register your models here.
admin.site.register(FoodCategory)
admin.site.register(FoodChoice)