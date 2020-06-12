# #4 Django(장고) :computer:



## :exclamation: Form 

action 속성으로 보낸다.

```html
<form action ="/search">
  <input name="q">
  <input name="a">
  <input name="g">
</form>
```

name="q", name="a", name="g"  는 key 이고 검색할때 값 







## View에서

**2개의 View필요**

1. 사용자로부터 입력받는 form 을 보여주는 view
2. 입력된 데이터를 받아서 처리하는 view



실습 -> throw /  catch

views 함수 두개 만들고 이렇게 해본 후에는... 

객체에 대한 정보단 찍힌 상태

```python
def catch(request):
  print(request)
	return render(request, 'catch.html')
```

​	<WSGIRequest: GET '/catch/?message=hi'>

```python
def catch(request):
  print(request.GET)
	return render(request, 'catch.html')
```

   <QueryDict: {'message': ['HIHIHI']}>









## From 에서 중요한 것

#### 	1. 데이터를 어디로 보낼 것인지 => action

#### 	2. 어떤 방식으로 보낼지 => method

#### 	3. 어떤 데이터를 보낼지 = > input, type [http input type mdn](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input)

#### 	4. 데이터의 이름은 어떻게 붙일지 => name

#### 	5. 제출 => submit









## Form 에서 GET, POST방식이란?

[http method **mdn**](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods)

#### GET 

* HTTP method 중 GET 요청은 서버로부터 정보를 조회하는데 사요된다.
* `GET` 메서드는 특정 리소스의 표시를 요청합니다. `GET`을 사용하는 요청은 오직 데이터를 받기만 합니다
* **서버의 데이터나 상태를 변경시키지 않기 때문에 단순조회(html)할 때 사용.**
* 데이터를 전송할 때 http body가 아니라 **쿼리스트링(? 뒤에 모든 것들)을 통해 전송.**



#### POST

* post : 