# #3 Django(장고) :computer:

[장고공식문서](https://www.djangoproject.com/)

**M odel** 

**T emplate ( Views)**

**V iew (Controllers)**



## :kissing_smiling_eyes: About Django :)

* 하나의 프로젝트는 여러 앱을 가지게 된다.
* django 프로제그는 app들의 집합이고, 실제 요청을 처리하고 페이지를 보여주고 하는 것들은 이 app들의 역할.
* app은 하나의 역할 및 기능 단위로 쪼개는 것이 일반적
* 작은 규모의 서비스에서는 세부적으로 나누지 않는다.
* app 이름은 ***복수형***으로 하는 것이 권장된다.
  * <img src="C:\Users\ohhoj\AppData\Roaming\Typora\typora-user-images\image-20200610102139196.png" alt="image-20200610102139196" style="zoom:50%;" />



* MTV 모델

  [장고 Introduction](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Introduction)![image-20200610101111345](C:\Users\ohhoj\AppData\Roaming\Typora\typora-user-images\image-20200610101111345.png)







## Django 프로젝트 특징

- app 들의 집합 (한개의 프로젝트에 여러 app들이 존재함)
- 실제 요청을 처리하고 페이지를 보여주고 하는 것들은 이 app들의 역할
- app은 하나의 역할 및 기능 단위로 쪼개는 것이 일반적
- 작은 규모의 서비스에서는 세부적으로 나누지 는 않는다
- app 이름은 복수형으로 하는 것이 권장된다







## Django 설치 및 실행

- 설치 : 

  ```
  pip install django==2.1.15
  ```

- 설치 확인: 

  ```
  pip list
  ```

- 장고 프로젝트 만들기(처음에만 사용) : 

  ```
  django-admin startproject firstapp
  ```

  - 쓰면 안되는 이름
    * django, test, class, django-test(하이푼 안됨!)

- firstapp에 들어가기

  ```
  cd firstapp
  ```

- *서버 작동* : 

  ```
  python manage.py runserver
  ```

- 앱 생성 : 

  ```
  python manage.py startapp [app name]
  ```

- 명령어 기본 : 

  ```
  python manage.py ~~~~~~~
  ```





## django project 시작하기

```
python manage.py startapp articles
```

#### 1. django 프로젝트 생성

#### 2. app 생성

#### 3. 프로젝트에 app 등록 (settings.py)

#### 4. urls.py 작성

#### 5. views.py 작성

#### 6. templates 작성









## 프로젝트 기본 구성 내용

- `__init__.py` : 해당 디렉토리를 패키지화 해주는 파일 (ex. import firstapp 가능)
- `settings.py` : 모든 설정을 관리해주는 파일
- `urls.py` : 요청 url
- `wsgi.py` : 배포할 때 사용
- `admin.py` : 관리자용 페이지를 커스터마이징 하는 파일
- `apps.py` : app 의 정보가 작성된 곳. 절대! 수정하지 않음
- `models.py` : app 에서 database 즉 `model` 을 정의하는 곳
- `test.py` : test code 를 작성하는 곳
- `views.py` : view들이 정의 되는 곳..다양한 함수 작성 (중간 관리자-젤 중요)





<img src="C:\Users\ohhoj\AppData\Roaming\Typora\typora-user-images\image-20200610101233102.png" alt="image-20200610101233102" style="zoom:50%;" />








![image-20200610103734101](C:\Users\ohhoj\AppData\Roaming\Typora\typora-user-images\image-20200610103734101.png)



##### app 'articles' 안에 'templates' 폴더를 만들고 그 안에 보여줄 html파일들을 만든다.

![image-20200610104405178](C:\Users\ohhoj\AppData\Roaming\Typora\typora-user-images\image-20200610104405178.png)


