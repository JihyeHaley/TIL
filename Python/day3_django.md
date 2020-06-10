# #3 Django(장고) :computer:

[장고공식문서](https://www.djangoproject.com/)

**M odel** 

**T emplate ( Views)**

**V iew (Controllers)**

`python manage.py runserver`



## :kissing_smiling_eyes: About Django :)

* 하나의 프로젝트는 여러 앱을 가지게 된다.
* django 프로제그는 app들의 집합이고, 실제 요청을 처리하고 페이지를 보여주고 하는 것들은 이 app들의 역할.
* app은 하나의 역할 및 기능 단위로 쪼개는 것이 일반적
* 작은 규모의 서비스에서는 세부적으로 나누지 않는다.
* app 이름은 ***복수형***으로 하는 것이 권장된다.
  * ![image-20200610102139196](C:\Users\ohhoj\AppData\Roaming\Typora\typora-user-images\image-20200610102139196.png)

## django project 시작하기

```
python manage.py startapp articles
```

(중략...ㅎㅎ)



#### 1. django 프로젝트 생성

#### 2. app 생성

#### 3. 프로젝트에 app 등록 (settings.py)

#### 4. urls.py 작성

#### 5. views.py 작성

#### 6. templates 작성

<hr>

![image-20200610103734101](C:\Users\ohhoj\AppData\Roaming\Typora\typora-user-images\image-20200610103734101.png)



##### app 'articles' 안에 'templates' 폴더를 만들고 그 안에 보여줄 html파일들을 만든다.

![image-20200610104405178](C:\Users\ohhoj\AppData\Roaming\Typora\typora-user-images\image-20200610104405178.png)



## 명령어 정리

### 처음 시작할때만 "django-admin start project"

### 나중에는 python manage.py 



`pip install django==2.1.15`

`django-admin startproject firstapp`

* 쓰면 안되는 이름
  * django, test, class, django-test(하이푼 안됨!)

`cd firstapp`

`python manage.py runserver`

![image-20200610094717673](C:\Users\ohhoj\AppData\Roaming\Typora\typora-user-images\image-20200610094717673.png)



*if you see ROCEKT,*  **장고 프로젝트 시작된다!!!**

![image-20200610101233102](C:\Users\ohhoj\AppData\Roaming\Typora\typora-user-images\image-20200610101233102.png)



[장고 Introduction](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Introduction)![image-20200610101111345](C:\Users\ohhoj\AppData\Roaming\Typora\typora-user-images\image-20200610101111345.png)



