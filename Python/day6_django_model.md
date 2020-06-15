# day6_Django_model(장고)

[from django.db import models](https://github.com/django/django/tree/master/django/db/models)

model 이 db를 관리해줄 뿐 !!

<sketch for db>

| ?    | id   | title | content | created_at | updated_at |
| ---- | ---- | ----- | ------- | ---------- | ---------- |
|      | 1    |       |         |            |            |
|      | 2    |       |         |            |            |
|      | 3    |       |         |            |            |
|      | 4    |       |         |            |            |
|      | 5    |       |         |            |            |
|      | 6    |       |         |            |            |

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



## Model  작성 3단계

#### 	1. models.py 작성

#### 	2. migrations (설계도 작성)

#### 	3. migrate (db 작성, 구축)



### SQL을 Python에서 사용할 때

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



