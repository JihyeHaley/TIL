# #5 Django__newApp_2 _URLs:computer:



## 🐝 새로운 앱 만들기 (after create new app)

### 	1. URL 로직 분리

​		***why?*** 하나의 url.py에서 모든 path를 관리하기가 어려워짐.

​		before : lotto-catch / **after : articles/lotto-catch**

​		- 기존 url이 바뀌어버려서 지금까지 작성한 모드 url을 다시 손봐줘야 됨...

​		- 그건 어려우니 그냥 url에 이름을 만들자.

### 	

### 	2. URL Name (PATH 이름..?)

​			- 그런데 두 개의 앱의 url 이름이 같다면...?

​			- 어떤 앱의 url  이름인지 app_name을 설정하자

### 	

### 	3. URL NameSpace

​			[django bulit in template](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/)





<hr>

​	 **분명 두번째 app의 index 주소로 요청을 보냈는데, 템플릿을 계속 첫번째 app의 index.html을 보여준다..**

​	CUZ, django는 templates를 한 곳에 모아서 가져가기 때문에

### 	4. Django NameSpace

#### 			app_name/

####  				templates/

#### 					app_name(pages *or* articles...) / <- namespace 분리역할

#### 						index.html

​		- app_name/templates 이후에 app_name폴더를 하나 더 둠으로써 이름 공간을 생성한다.

### 	Django는 기본적으로 templates를 "*app_name/templates*"에서 찾는다.

### 	Django는 기본적으로 static 도 "*app_name/static*"에서 찾는다.

​		**'DIRS': [os.path.join(BASE_DIR, 'firstapp', 'templates')],**

### 	first/templates/ 까지도 찾을 수 있게 됐다.





<hr>

### 		5. Inherient 

​		- 여러 페이지에 동일한 구조를 적용 시키고 싶다.

​		- 템플릿의 재사용성에 초점.

### 	



### 	6. static

#### 		app_name/

#### 			static/

#### 				app_name/ <-namespace 분리역할

#### 					stylesheets/

#### 					images/

* 웹 사이트의 구성 요소 중에서 image, css, js 파일과 같이 해당 내용이 고정되어, 응답을 할 때 별도의 처리 없이 파일 내용을 그대로 보여주는 파일. (정적 파일)
* 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 응답해주면 되는 것.









####  firstapp/firstapp/settings.py 에'pages', 추가

```
python manage.py startapp pages
```

* ```python
  INSTALLED_APPS[
    'articles',
    'pages',
  ]
  ```









#### firstapp/urls.py에서 views.py가 충돌 할 거니깐 URL을 각 앱들의 URL파일을 만들어서 수정해주기

​	admin/은 가져오지 않기*

* ```python
  from django.urls import path
  from . import views
  
  urlpatterns = [
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
      path('lotto-throw/', views.lotto_throw),
      path('lotto-catch/', views.lotto_catch),
      path('artii/', views.artii),
      path('artii-result/', views.artii_result),
  ]
  ```

  
    * ❓이제 html파일을 모두 바꿀 수가 없으니깐 name으로 한다.

      * firstapp/articles/urls.py

        * ```
          urlpatterns = [
              path('artii/', views.artii, name='artii'),
              path('artii-result/', views.artii_result, name='artii_result'),
          ]
          ```

          * name = '이름이름'은 **path 이름**!

  

  * firstapp/articles/templates/artii.html

    * ```html
      <form action="{% url 'artii_result' %}" method="get">
          단어입력: <input type="text" name="word"><br>
      ```

      * action의 url설정에  urls.py에서 설정한 path 이름을 적어준다. 

        **{% url '*[name 적기]*' %}**

        url + tab만 해도 만들어준다.





 #### firstapp/urls.py

* ```python
  from django.contrib import admin
  from django.urls import path, include
  # __init__.py가 app을 package화 해주니깐, from import 사용할 수 있다.
  # 가져올 때는 .py를 빼고 가져온다.
  from articles import views 
  from pages import views 
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
      path('pages/', include('pages.urls')),
  ]
  ```

  * from django.urls import path, ***include***

