from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:question_pk>/', views.detail, name='detail'),
    path('<int:question_pk>/answers/create', views.answer_create, name='answer_create'),

]
