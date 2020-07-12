from django.contrib import admin
from django.urls import path
from . import views

app_name = 'foods'

urlpatterns = [
    path('result/<str:food_ctg>/', views.result, name='result'),
    path('result/', views.hangover, name='hangover'),
    path('select/<str:food_name>/', views.select, name='select'),
]