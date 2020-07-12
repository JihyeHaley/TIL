from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('dinner/', views.dinner),
    path('randomImg/', views.randomImg),
    path('hello/<str:name>/', views.hello),
    # str 타입 명시는 생략 가능
    # paht('hello/<name>/, view.hello),
    path('introMe/<str:name>/<int:age>/', views.introMe),
    path('calculation/<int:num1>/<int:num2>/', views.calculation),
    path('dtl-practice/', views.dtl_practice),
    path('rotator/<word>/', views.rotator),
    path('throw/',views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('lotto-throw/', views.lotto_throw, name='lotto'),
    path('lotto-catch/', views.lotto_catch, name='lotto_catch'),
    path('artii/', views.artii, name='artii'),
    path('artii-result/', views.artii_result, name='artii_result'),
]
