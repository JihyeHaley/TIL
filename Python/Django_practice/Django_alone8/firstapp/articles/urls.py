from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('index/<str:name>/<int:age>/', views.index, name='index'),
    path('form-practice-a/', views.form_practice_a, name='practice_a'),
    path('form-practice-b/', views.form_practice_b, name='practice_b'),
]