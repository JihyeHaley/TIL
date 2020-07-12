from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'), # GET(new) / POST(create)
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'), # GET(edit) / POST(update)
    path('<int:pk>/delete/', views.delete, name='delete')
]
