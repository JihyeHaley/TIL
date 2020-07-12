# day8_Django_form_new_logic

##### no more using form tag in html

공식문서는 꼭 확인하기 :)     

[django form](https://docs.djangoproject.com/en/3.0/ref/forms/fields/#charfield) 

[django widget](https://docs.djangoproject.com/en/3.0/ref/forms/widgets/)

```html
  <input type="text" name="title"><br>
  <textarea name="content"></textarea><br>
```

를 form 클래스가 변화시켜준다. 

```html
{{ form }}
```



### Meta데이터

사진 (데이터)

사진에 대한 메타 데이터

* 어떤 카메랄 찍었는지
* 화소는 몇인지
* 사진이 찍힌 장소는 어딘지





## 🔮 Django *Form*

##### 🧷  form  내 field들, field배치, widget, label 유효한 값 등을 정의하고 비유효한 field에 관련된 에러메시지를 결정한다.



##### 🧷  우리가 직접 form태그를 작성하는 것보다 유효한 데이터에 요구되는 여러 동작을 '올바르게' 하기 위해서 제공하는 기능

```python
def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect ('articles:detail', article.pk)
    else: #아직받아온 것이 없어서 꼭 else를 먼저 만들기
        form = ArticleForm(instance=article)
    
    
    context  = {
        'form' : form,
    }

    return render(request, 'articles/update.html', context)
```



## 🧲 Django *ModelForm*

##### 🧷 jango가 해당하는 모델에서 양식에 필요한 모든 정보를이미 정의한다.



##### 🧷 모델의 Meta 정보를 통해 어떤 모델을 정의하는지 이미 알고 있기 때문에 *검증이 끝나면*, 바로 save가 가능하다.



##### 🧷 어차피 모델에 있던 것들을 Form에넣을 거니깐



## 🎨 Bootstrap4

[BOOTSTRAP  참고](https://django-bootstrap4.readthedocs.io/en/latest/templatetags.html)























## 🌈☘️CRUD_로직☘️🌈



📍*R*EAD

##### urls.py

```

```



##### views.py

```

```



##### 0000.html

```

```



### 📍*C*REATE

##### urls.py

```

```



##### views.py

```

```



##### 0000.html

```

```



### 📍*D*ELETE

##### urls.py

```

```



##### views.py

```

```



##### 0000.html

```

```



### 📍*U*PDATE

##### urls.py

```

```



##### views.py

```

```



##### 0000.html

```

```

### admin 작성순서

#### 	1. python manage.py createsuperuser

#### 	2. admin.py 작성