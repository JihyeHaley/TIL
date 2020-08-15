# 내장함수



### ▶︎수칙연산 

#### 	⚠️ abs(a)

##### 		인자로 숫자를 전달하면 그 숫자의 *절대값*을 반환하는 함수



#### 	⚠️ divmod(a, b)

##### 		첫 번째 인자를 두 번째 인자로 나눴을 때의 몫과 나머지를 튜플 객체로 반환하는 함수

```python
val1, val2 = 9, 5
result_tuple = divmod(val1, val2)

print('divmod({0}, {1}) => 몫: {2} 나머지:{3}' .format(val1, val2, *result_tuple))

# divmod(9, 5) => 몫: 1 나머지:4
```



#### 	⚠️ pow(a, b)

##### 		첫 번째로 전달된 인자 값에 대해 두번째로 전달된 인자 값으로 제곱한 결과를 반화하는 함수

```python
data_list = [1, 2, 3, 4, 5]

print('pow({0}, 2) => {1}' .format(data_list[2], pow(data_list[2], 2)))

print('list(map(lambda x: pow(x, 2), {0})) => {1}' .format(data_list, list(map(lambda x: pow(x, 2), data_list))))

# pow(3, 2) => 9
# list(map(lambda x: pow(x, 2), [1, 2, 3, 4, 5])) => [1, 4, 9, 16, 25]
```





### ▶︎시퀀스형 / 반복 가능한 자료형을 다루는 함수 

#### 	⚠️ all(group) (Like And)

##### 			반복 가능한 자료형인 List, Tuple, Set, Dictionary, 문자열 등을 인자로 받고 항목 모두가 True로 평가되면 True를 반환하고 Flase로 평가되는 항목이 하나라도 있으면 False를 반환

```python
val1 = [True, True, True]
print(f'all({val1}) = > {all(val1)}')
# all([True True True]) = > True

val2 = [10, 20, 30]
print(f'all({val2}) = > {all(val2)}')
# all([10, 20, 30]) = > True

val3 = [10, 20, 0]
print(f'all({val3}) = > {all(val3)}')
# all([10, 20, 0]) = > False
```



```python
val4 = [10, 20, ""]
print(f'all({val4}) = > {all(val4)}')
# all([10, 20, ""]) = > False

val5 = [10, 20, False]
print(f'all({val5}) = > {all(val5)}')
# all([10, 20, False]) = > False

val6 = [10, 20, None]
print(f'all({val6}) = > {all(val6)}')
# all([10, 20, None]) = > False
```



#### ⚠️ any(group) (Like Or)

##### 			반복 가능한 자료형인 List, Tuple, Set, Dictionary, 문자열 등을 인자로 전달하여  항목 모두가 False로 평가되면 False로 반환하고, True로 평가되는 항목이 하나라도 있으면 True를 반환



#### ⚠️ enumerate(group)

##### 			List, Tuple, Dictionary, 문자열 같은 시퀀스형을 입력받아 인덱스를 포함하는 튜플 객체를 항목으로 구성하는 enumerate 객체를 반환하는 함수

*  언팩연사자를 활용해서 보자.

  * ```python
    data_list = [10, 20, 30, 40, 50]
    for obj in enumerate(data_list):
      print('{0}: {1}, {2}' .format(type(obj) *obj))
      # 변수 obj : 투플객체로 인덱스와 값 출력
    ```



#### ⚠️ filter(group)

##### 			조건에 맞는 항목을 걸러내는 함수

* ![image](https://user-images.githubusercontent.com/58539681/89861160-0fa74880-dbe0-11ea-8b2e-7f401638fe0f.png)





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

