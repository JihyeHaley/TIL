# day6_Django_model(장고)

[from django.db import models](https://github.com/django/django/tree/master/django/db/models)

model 이 db를 관리해줄 뿐 !!

<sketch for db>

| ?    | id   | title  | content | created_at | updated_at |
| ---- | ---- | ------ | ------- | ---------- | ---------- |
|      | 1    | first  | django  |            |            |
|      | 2    | second | django  |            |            |
|      | 3    |        |         |            |            |
|      | 4    |        |         |            |            |
|      | 5    |        |         |            |            |
|      | 6    |        |         |            |            |

![code2](https://user-images.githubusercontent.com/58539681/84613176-a962ba00-aefd-11ea-8ef9-8cdec6ea671c.png)



## 🔠 CharField

* 길이에 제한이 있는 문자열을 넣을 때 사용
* max_length는 필수 인자
* text양이 많을 경우 => **TextField**





## ⏰ DateTimeField

#### - auto_now_add

* 최초 생성 일자
* django ORM이 최소 INSERT시에만 현재날짜와 시간으로 갱신



#### - auto_now

* 최종 수정 일자
* django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신



## 📭Django shell에서 하기 위해서

```python
pip install ipython
```

```python
python manage.py shell
```

```python
pip install django-extensions
```

[django extention](https://django-extensions.readthedocs.io/en/latest/installation_instructions.html)에 들어가서 설치하고 입력해주고

settings.py > INSTALLED_APPS[]에다가 'django_extention'

```python
python manage.py shell_plus
```

​	를 하면 모든걸 import를 자동적으로 해준다.





## 🌈☘️Model  작성 3단계☘️🌈

#### 	1. models.py 작성

#### 	2. migrations (설계도 작성)

##### 	sqlmigrate

​		`python manage.py makemigrations`

​		`python manage.py sqlmigrate app_name migration_number`

#### 	3. migrate (db 작성, 구축)

​		`python manage.py migrate`

해당 migrations가 어떻게 SQL구문으로 해석될 수 있는지



## ⚒SQL을 Python에서 사용할 때 (Abstract)⚒

![code2](https://user-images.githubusercontent.com/58539681/84613176-a962ba00-aefd-11ea-8ef9-8cdec6ea671c.png)

```python
python manage.py makeimgrations
```

* migrations/0001_initial.py 생성됨

```python
python manage.py sqlmigrate  articles 0001
```

```
BEGIN;
--
-- Create model Article
--
CREATE TABLE "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(20) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
COMMIT;
```

![code](https://user-images.githubusercontent.com/58539681/84613149-98b24400-aefd-11ea-8abb-420b618173f5.png)

* table 생성

```python
python manage.py migrate
```





## CRUD

### 🧪 READ

``` python
# 모든 객체 조회
Article.objects.all()

# 특정 객체 조회(get)
Article.objects.get(pk=n)

# 특정 조건 객체 조회(filter) -> 무조건 쿼리셋 리턴, 없으면 빈 쿼리가 나온다.
Article.objects.filter(pk=n)
Article.objects.filter(title='first', content='django!')

# 내림차순
Article.objects.order_by('-pk')

# LIKE역할
Article.objects.filter(title__contains='fi')
Article.objects.filter(title__icontains='fi')
Article.objects.filter(title__startswith='fi')
Article.objects.filter(title__endswith='!')
```

* get()을 사용할 때 해당 객체가 없으면 ***DoesNotExist*** 에러가 발생
* 여러개일 경우에 ***MultipleObjectReturned*** 에러가 발생.
* 이와 같은 특징 때문에 unique한 속성을 가지고 있는 데이터에 사용해야 한다.(pk)

[quries](https://docs.djangoproject.com/en/3.0/topics/db/queries/)

[queryset](https://docs.djangoproject.com/en/3.0/ref/models/querysets/)

* field look up 은 __ 의 유무 이다.



### 🧪 Create (3 ways to use)

```python
#1
article = Article()
article.title = 'first'
article.content = 'django!'
article.save()
```



```python
#2 
article = Article(title='second', content='django!!')
article.save()
```

`article.save()` 를 안하는 경우가 있으니 주의하자



```python
#3
Article.objects.create(title='third', content='django!!!')
```



### 🧪 Update

```python
article = Article.objects.get(pk=1)
article.title = 'edit title'
article.save()
```



### 🧪 Delete 

```python
article = Article.objects.get(pk=1)
article.delete()
```



<hr>

<hr>



#### 💊obejects

<hr>

* models.py에 작성한 클래스(테이블)을 불러와서 사용할 때 DB와의 인터페이스 역할을 하는 manager
  * Python class(python) --------- objects --------- DB (SQL)







#### 💊QuerySet

<hr>

* objects 매니저를 사용하여 복수의 데이터를 가져오는 함수를 사용할 때 반환되는 객체 타입
* 단일 객체는 Query(class의 인스턴스)

![image-20200615133931831](/Users/haley/Library/Application Support/typora-user-images/image-20200615133931831.png)

* query(질문)를 DB에게 보내서 글을 조회하거나 생성, 수정, 삭제
* qeury를 보내는 언어를 활용해서 DB에게 데이터에 대한 조작을 실행







<hr>

### 계정 또한 데이터이기 때문에 반드시 migrate 작업 후에 관리자 계정을 생성해야 한다.



### admin 작성순서

#### 	1. python manage.py createsuperuser

#### 	2. admin.py 작성