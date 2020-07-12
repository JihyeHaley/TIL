from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # 생성, 아직 까지 iD값이 필요 없다 
    path('create/', views.create, name='create'),  
    
    # ~을 update, delete, detail이라서 "목적어"가 꼭  필요
    path('<int:pk>/', views.detail, name='detail'), 
    path('<int:pk>/update/', views.update, name='update'), 
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    # article/3/comemnts/create
]
