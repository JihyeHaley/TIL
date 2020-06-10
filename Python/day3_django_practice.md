# #3 Django_실습:video_game:



## 실습 1.

### 1)자개소개, 2) 곱셉결과

#### :game_die: 1. 자기소개 페이지 (이름, 나이)

**urls.py**

```python
urlpatterns = [
    path('hello/<str:name>/', views.hello),
    # str 타입 명시는 생략 가능
    # paht('hello/<name>/, view.hello),
   
]
```

**views.py**

```python
def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'hello.html', context)

```

**introMe.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test - Introduction to Me :)</title>
</head>
<body>
    <h1>This is introduction to {{ name }}. Call me Haley, I'm {{ age }} ;)</h1>
</body>
</html>
```





#### :game_die: 2. 수  2개를 받아서 곱셈 결과를 보여주는 페이지

**urls.py**

```python
urlpatterns = [
    path('calculation/<int:num1>/<int:num2>/', views.calculation),

]
```

**views.py**

```python
def calculation(request, num1, num2) :
    result = num1 * num2 
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : result,
    }
    return render(request, 'calculation.html', context)
```

**calculation.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test - calculation</title>
</head>
<body>
    <h1>{{ num1 }}X{{ num2 }}={{ result }} </h1>
</body>
</html>
```





## 실습 2.

### DTL (Django Template Language)

* 주석처리, 날짜, for, if 등... 내가 느끼기에 JavaScript에서 할 만한 것들을 쉽게 사용해서 html에서 처리해주는 방법을 배웠다!

  

#### :game_die: 실습

**urls.py**

```python
urlpatterns = [
   path('dtl-practice/', views.dtl_practice),
]
```



**views.py**

```python
def dtl_practice(request):
    foods = ['타코', '브리또', '오뎅', '딤섬']
    empty_list = []
    messages = 'Life is hosrt, you need Python...'
    datetime_now = datetime.now()
    context = {
        'foods' : foods,
        'empty_ist' : empty_list,
        'messages' : messages,
        'datetime_now' : datetime_now,
    }
    return render(request, 'dtl_practice.html', context)

```



**dtl_practice.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test - dtl_practice</title>
</head>
<body>
    <h1>1. 반복문</h1>
    {% for food in foods %} 
        <p>{{ food }}</p>
    {% endfor %}
    <!-- for같은 것들은 열리면 닫혀야한다.-->


    <!-- forloop.counter or forloop.count0 은 python에서 enumerate같은 함수-->
    {% for food in foods %}
        <p>{{ forloop.counter }} {{ food }}</p> 
    {% endfor %}

    {% for element in empty_list %}
        <p>{{ element }}</p>
    {% empty %}
        <p>지금은 아무것도 없네요...</p>
    {% endfor %}
    <hr>


    <h3>2번. 조건문 </h3>
    {% if '짜장면' in foods %}
        <p>짜장면은 역시 또자강!</p>
    {% else %}
        <p>너 다이어트 중이지? 그만 먹어.... 제발... 바지 작잖아...ㅠㅠ 반성하자 ㅠㅠ </p>
    {% endif %}
    <hr>
    {% for food in foods %}
        {% if forloop.first %}
            <p>샐러드는 no dressing이지 !</p>
        {% else %}
            <p>{{ food }}</p>
        {% endif %}
    {% endfor %}
    <hr>


    <h3>3번. Length Filter </h3> <!-- pipe line 뒤쪽에 사용하는 것들-->
    {% for food in foods %}
        {% if food|length > 2 %}
            <p>메뉴이름이 너무 길어요</p>
        {% else %}
            <p>{{ food }}, {{ food|length }}</p>
        {% endif %}
    {% endfor %}
    <hr>


    <h3>4번. Lorem ipsum </h3> <!-- pipe line 뒤쪽에 사용하는 것들-->
    <p>{% lorem %}</p> <!-- 이미 정의된 변수 호출이라서 퍼센트로-->
    <hr>
    <p>{% lorem 3 w %}</p>
    <hr>
    <p>{% lorem random %}</p>
    <hr>


    <h3>5. 글자수 제한</h3>
    <p>{{ messages|truncatewords:3 }}</p>
    <p>{{ messages|truncatechars:5 }}</p> <!-- ...은 무조건 나오니깐 그거 계산해서 숫자 쓰기-->
    <p>{{ messages|truncatechars:10 }}</p>
    <hr>


    <h3>6. 글자 관련 필터</h3>
    <p>{{ 'ABC'|lower }}</p>
    <p>{{ messages|title }}</p>
    <p>{{ messages|capfirst }}</p>
    <p>{{ foods|random }}</p>
    <hr>

    <h3>7. 연산</h3>
    <p>{{ 4|add:6 }}</p> <!-- 애초의 목적이 다르기 때문에 -->
    <hr>

    <h3>8. 날짜처리</h3>
    <p>{{ datetime_now }}</p>
    <p>{% now "DATE_FORMAT" %}</p>
    <p>{% now "DATETIME_FORMAT" %}</p>
    <p>{% now "SHORT_DATE_FORMAT" %}</p>
    <p>{% now "SHORT_DATETIME_FORMAT" %}</p>
</body>
</html>
```





## 실습 3.

### 회문검사

* 이건 알고리즘 문제같다고 느꼇고, 알고리즘으로 하는 것도 있찌만 오늘은 slicing 이용해서 간단하게 출력만 하는 :)

  

#### :game_die: 

**urls.py**

```python
path('rotator/<word>/', views.rotator),
```



**views.py**

```python
def rotator(request, word):
    if word == word[::-1]:
        result = True
    else:
        result = False
    context = {
        'word' : word,
        'result' : result,
    }
    return render(request, 'rotator.html', context)
```



**rotate.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test - 회문실습</title>
</head>
<body>
    <h1>회문연습</h1>
    {{ word }}는
    {% if result%}
        <p> 회문입니다.</p>
    {% else %}
        <p>회문이 아닙니다.</p>
    {% endif %}
</body>
</html>
```



