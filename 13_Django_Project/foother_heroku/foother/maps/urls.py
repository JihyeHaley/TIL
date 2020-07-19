from django.urls import path
from . import views


app_name = 'maps'


urlpatterns = [
    path('all/', views.review_all, name='review-all'),
    path('create/', views.review_create, name='review-create'),
    path('<str:username>/<int:review_pk>/', views.review_detail, name='review-detail'),
    path('<int:review_pk>/update/', views.review_update, name='review-update'),
    path('<int:review_pk>/like/', views.like, name='like'),
    path('<str:comment_user_pk>/<int:review_pk>/comment/create/', views.comment_create, name='comment-create'),
    path('<str:comment_username>/<int:review_pk>/comment/complete/', views.comment_complete, name='comment-complete'),
]