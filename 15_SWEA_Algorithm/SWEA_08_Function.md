# 함수의 유형

* 매개변수 :
  * 함수에 입력 값을 전달해야 하는 결정 요인
* 반환값 :
  * 함수가 수행 결과를 호출한 곳으로 돌려줄 필요가 있는가를 결정하는 요

1. 매개변수와 반환값이 있는 함수
   * `def function_1 (a): return a`
2. 매개변수는 없고 반환 값이 있는 함수
   * `def function_2 (): return a`
3. 매개번수는 있고 반환값이 없는 함수
   * `def function_3(a): pass` 
4. 매개변수와 반환값이 없는 함수
   * `def function_4():pass`



## 🔑⚠️ 언팩 연산자(*)

##### 매개변수의 개수를 가변적으로 사용할 수 있도록 언팩 연산자

##### 매개변수에 적용 시 인자를 *튜플 형식으로 처리*함

* 언팩 연산자를 사용해서 만든 함수

  * ```python
    def cal_sum2(*params):
      total = 0 
      for val in params:
        total += val
      return total
    ```

* 언팩연산자와 그냥 매개변수를 혼합해서 만든 경우 (just 매개변수는 앞으로)

  * ```python
    def calc_sum3(precision, *params):
        if precision == 0 :
            total = 0
        elif 0 < precision < 1:
            total = 0.0
    
        for val in params:
            total += val
    
        return total
    ```

    

## 🔑☢️ 키워드 언팩 연산자(**)

##### 매개변수의 개수를 가변적으로 사용할 수 있도록 / 키워드 인자들을 전달해 *매개변수를 딕셔너리 형식*으로 처리

* 매개변수를 딕셔너리 형식으로
  * 키1 = 값1, 키2 = 값2



# 🔑 Scope📚

##### * 어디서나 접근 가능한 전역 변수 => 전역 스코프

##### * 함수 내에서만 접근 가능한 지역 변수 => 함수 스코프

#### 변수에 접근하는 절차:

##### 1️⃣ 순위 : 함수 스코프 내에서 가장 먼저 변수를 찾음

##### 2️⃣ 순위 : 함수 스포크 내에 변수가 없을 경우,, 전역 스코프에서 변수를 찾음



### 접근하고자 하는 전역변수 앞에 global을 기술한다. 

#### 지역변수와 전역변수 이름이 같을 경우! 전역 변수가 가려저 접근 못할 수 있음





## 🧮 고급함수

### 🍭 중첩함수 

##### : 함수 내에 중첩함수를 선언해 사용가능

1. 중첩함수를 포함하는 함수 내에서만 호출이 가능함
2. 중첩함수를 포함하는 함수의 스코프에도 접근이 가능함 (함수내의 지역변수에 접근 가능하다.)

```python
def calc2(operator_fn, x, y): 
    # 매개변수 operator_fun에 전달된 함수를 실행해 반환된 값을 return 문을 통해반환
    return operator_fn(x, y)

def plus(op1, op2):
    return op1 + op2

def minus(op1, op2):
    return op1 - op2

ret_val = calc2(plus, 10, 5) #calc2 함수에서 operator_fn에 plus를 대입
print(f'calc2(plus, 10, 5)의 결과 값: {ret_val}')
ret_val = calc2(minus, 10, 5) #calc2 함수에서 operator_fn에 minus 대입
print(f'calc2(plus, 10, 5)의 결과 값: {ret_val}')
```



## 람다식

#### 프로그램의 유연성을 높이기 위해 함수를 매개변수로 전달하는 방식 선호!

##### 매번 함수를 선언해 사용한다는 것이 불편할 수 있다. => 편하게 하기 위한것 람다식

`Lambda 매개변수 : 반환값`

1. 변수에 저장해 **재사용이 가능**한 함수처럼 사용
2. 기존의 함수처럼 **매개변수의 인자로 전달**
3. 함수의 **매개변수에 직접 전달 가능**

```python

def calc3(operator_fn, x, y):
    return operator_fn(x, y)

ret_val = calc3(lambda a, b: a + b, 10, 5)
print(f'calc3(lamdba a, b: a + b, 10, 5)의 결과값: {ret_val}')
ret_val = calc3(lambda a, b: a - b, 10, 5)
print(f'calc3(lamdba a, b: a - b, 10, 5)의 결과값: {ret_val}')
```



## 클로저

1. 중첩함수에서 중첩함수를 포함하는 함수의 scope에 접근 가능
2. 중첩함수 자체를 반환값으로 사용한다면?
   1. 정보 은닉 구현 가능
   2. 전역변수 남용 방지
   3. 메서드가 하나밖에 없는 객체를 만드는 것보다 우아한 구현 가능

```python
def outer_func():
    id = 0 # 지역 변수: 함수 내의 코드 또는 중첩 함수내에서만 접근 가능
    def inner_func():
        nonlocal id 
        # 변수id가 중첩함수인 inner_func 함수의 지역변수가 아님
        # 변수id 접근 시 outer_func 함수 스코프에서 찾게 만듦
        id += 1 
        return id
    return inner_func # 함수 호출이 아닌 함수에 대한 참조를 반환
```

##### outer_func()을 부르면 inner_func()이 반환된다는걸 잊지마!

```python
make_id = outer_func() # 이게 함수가 되는 거!!!!!

print(f'make_id() 호출의 결과: {make_id()}')
print(f'make_id() 호출의 결과: {make_id()}')
print(f'make_id() 호출의 결과: {make_id()}')

```

##### 1. 중첩함수(inner_func() 호출) 

##### 2. outer_func()함수의 지역변수 id의 값 1씩 증가

##### 3. 증가된 id 값 반환

##### 4. str.format() 함수의 인자로 전달, 변환 문자열 생성

##### 5. print() 함수를 통해 표준출력으로 출력



```python
def input_r():
    r = float(input('반지름을 입력하세요: '))
    return r
    
def round_size(r):
    return r**2*3.14
def round_side(r): 
    return r*2*3.14
    
r = input_r()
round_size = round_size(r)
round_side= round_side(r)
print(f'원의 면적:{round_size:.2f}, 원의 둘레: {round_side:.2f}')
```

