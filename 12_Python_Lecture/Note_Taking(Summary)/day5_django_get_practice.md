# #5 Django_Get_practice :computer:



## :exclamation: < pre > tag 

* **HTML `<pre>` 요소**는 미리 서식을 지정한 텍스트를 나타내며, HTML에 작성한 내용 그대로 표현합니다. 텍스트는 보통 고정폭 글꼴을 사용해 렌더링하고, 요소 내 공백문자를 그대로 유지합니다.

* 실습에서 ascii artii를 그려보는 연습을 했다.
* '#'으로 글자가 계속 나와서 <pre>태그를 사용해서 글자를 보여줄 수 있다.



### urls.py

```python
urlpatterns = [
    path('artii/', views.artii),
    path('artii-result/', views.artii_result),
]
```



### views.py

1. **Get 방식이기 때문에 숫자들을 입력받는 함수**

   ```python
   def artii(request):
     #1. font URL
     font_URL = 'http://artii.herokuapp.com/fonts_list'
   
     # 2. ARTII api fontlist로 요청을 보내 폰트 정보를 받는다.
     font_response = requests.get(font_URL).text
     #print(type(font_response))
   
     # 3. 문자열 데이터를 리스트로 변환한다.
     fonts_list = font_response.split('\n')
     print(fonts_list)
   
     context = {
         'fonts_list' : fonts_list,
     }
     return render(request, 'artii.html', context)
   ```



2. **입력받고 결과를 내오는 창**

   ```python
   def artii_result(request):
       # 1. form에서 넘어온 데이터를 받는다. (word, font를 artii에서 받아야 한다.)
       word = request.GET.get('word')
       font = request.GET.get('font')
   
       # 2. 선택해서 보여주기
       ARTII_URL = f'http://artii.herokuapp.com/make?text={word}+art&font={font}'
       
       print('word :' + word)
       print('font :' + font)
       # 3. artii api주소로 우리가 만든 데이터와 함께 요청을 보낸다.
       result = requests.get(ARTII_URL).text
       context = {
           'result' : result,
       }
   
       return render(request, 'artii_result.html', context)
   ```

   

### templates

#### 		1) artii 

```html
<h1>나만의 ascii artii</h1>
<form action="/artii-result/" method="get">
    단어입력: <input type="text" name="word"><br>
    <label for="font">폰트선택:</label>
    <select name="font" id="font">
        <option  value="" selected>선택해주세요</option>
```

DTL을 사용해서 **views** ***artii함수***에서 만든 **fonts_list**(는 list type)를 for문을 활용해서 계속 넣어준다.

`<select> ` 의 **name**이 꼭 일치해야한다. with URL에 들어갈 값

```html
        {% for font_select in fonts_list %}
            <option value="{{ font_select }}">{{ font_select }}</option>
        {% endfor %}
    </select><br>
    <input type="submit" value="만들기">
</form>
```

![image-20200613131330591](/Users/haley/Library/Application Support/typora-user-images/image-20200613131330591.png)



#### 	2) artii_result

**view** ***artii_result***함수에서  result를 보여주며 된다.

```html
<h1>result</h1>
```

**HTML `<pre>` 요소**는 미리 서식을 지정한 텍스트를 나타내며, HTML에 작성한 내용 그대로 표현합니다. 텍스트는 보통 고정폭 글꼴을 사용해 렌더링하고, 요소 내 공백문자를 그대로 유지합니다. 

위에서 참고 해주기 🙃

```html
<pre>{{ result }}</pre>
```

![image-20200613131412850](/Users/haley/Library/Application Support/typora-user-images/image-20200613131412850.png)





