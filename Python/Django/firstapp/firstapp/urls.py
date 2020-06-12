"""firstapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# __init__.py가 app을 package화 해주니깐, from import 사용할 수 있다.
# 가져올 때는 .py를 빼고 가져온다.
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('dinner/', views.dinner),
    path('randomImg/', views.randomImg),
    path('hello/<str:name>/', views.hello),
    # str 타입 명시는 생략 가능
    # paht('hello/<name>/, view.hello),
    path('introMe/<str:name>/<int:age>/', views.introMe),
    path('calculation/<int:num1>/<int:num2>/', views.calculation),
    path('dtl-practice/', views.dtl_practice),
    path('rotator/<word>/', views.rotator),
    path('throw/',views.throw),
    path('catch/', views.catch),
]
