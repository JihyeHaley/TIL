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



#### ⚠️ map()

##### 			 두번째 인자로 반복 가능한 자료형을 전달 받아 자료형의 각 항목에 대해 첫 번째 인자로 전달 받은 함수를 적용한 결과를 맵 객체로 반환하느 함수

* ```python
  data_list = list('abcdef')
  
  result = list(map(lambda x: x.upper(), data_list))
  print(f'List(map(lambda x: x.upper(), {data_list})) \n => {type(result)} {result}')
  ```





#### ⚠️ max() /min()

##### 			반복 가능한 자료형을 인자로 전달받아 항목 중 가장 큰 값 반환

##### 반복 가능한 자료형 인자로 전달받아 항목 중 가장 작은 값 반환



#### ⚠️ range(a, b ,c) 

a, b, c : 시퀀스형 객체를 생성하는 함수 

##### a: 첫 번째 인자로 전달된 시작 값

##### b: 두 번째 인자로 전달된 종료 값

##### c: 세 번째 인자로 전달된 증감치



#### ⚠️ sorted() 

##### 반복 가능한 자료형을 인자로 전달받아 항목들로부터 *정렬된 리스트를 생성해 반환*하는 함수

* `reversed()` : 내림차순
* `sorted()` : 오름차순



#### ⚠️ zip() 

##### 둘 이상의 반복 가능한 자료형 인자로 전달받아

#####  *동일 위치의 항목을 묶어 튜플을 항목으로 구성하는 zip객체를 생성*하는 함수

*인자로 전달된 객체는 동일 자료형이면서, **항목의 개수가 같아야** 한다*

* dict	

  * ```python
    print(f'dict(zip({data_list1},  {data_list3})) \n-> {dict(zip(data_list1, data_list3))} ')
    print(f'dict(zip({data_list3},  {data_list1})) \n-> {dict(zip(data_list3, data_list1))} ')
    ```

    > {1: 'a', 2: 'b', 3: 'c'} 
    >
    > {'a': 1, 'b': 2, 'c': 3} 





### 3️⃣ 변환함수

![image](https://user-images.githubusercontent.com/58539681/90327930-41028880-dfd3-11ea-9c18-5326ac99f3a3.png)



#### ⚠️ chr() 

##### : 정수 형태의 유니코드 값을 인자로 전달받아 해당 코드의 문자를 반환하는 함수 

* ```python
  val = 65
  print(f'chr({val}) => {chr(val)}')
  ```

  * A

* ```python
  val = 97
  print(f'chr({val}) => {chr(val)}')
  ```

  * a

* ```python
  val_korean = 0xac00
  print(f'chr(ac00) => {chr(val_korean)}')
  ```

  * 가
    * 16진수  0xac00 에 해당하는 ***유니코드 값***의 문자열 '가' 반환





#### ⚠️ ord() 

##### : 문자를 인자로 전달받아 유니코드 값(10진 전수)을 반환하는 함수

* ```python
  val = 'A'
  print(f'ord({val}) -> {ord(val)}')
  
  ```

  * 65

* ```python
  val = 'a'
  print(f'ord({val}) -> {ord(val)}')
  ```

  * 97

* ```python
  val = '가'
  print(f'ord({val}) -> {ord(val)}')
  ```

  * 44032
    * 문자열 '가'에 해당하는 유니코드 값 44032 반환



#### ⚠️ hex() 

##### : 10진 정수 값을 인자로 전달 받아 16진수로 변환된 값을 반환하는 함수

* ```python
  val = '가'
  print(f'ord({val}) -> {hex(ord(val))}')
  ```

  * 0xac00
    * 16진수 값 0xac00반환





#### 🧮 int(a) / int(a, b)

##### 인자로 전달된 <u>*숫자 형식의 문자열, 부동소수점 숫자*</u>를 *<u>정수로 변환</u>*하는 값을 반환하는 함수

* ```
  a를 b로 반환 여기서 b는 몇 진수로 반환할지 고르는 부분!
  ```

* 



#### 🧮 float()

##### 인자로 전달된 <u>*숫자 형식의 문자열, 정수*</u>를 <u>*부동소수점 숫자*</u>로 변환한 값을 반환하는 함수

* ```
  
  ```





#### 🧮 str()

##### 인자로 전달된 객체에 대한 <u>*문자열 변환 값*</u>을 반환하는 함수

* ```
  
  ```



### 4️⃣ 객체 조사를 위한 함수

#### 💼 dir()

##### 인자로 전달된 객체가 가지고 있는 변수, 메서드와 같은 *<u>속성 정보를 리스트 객체로 반환</u>*



#### 💼 globals()

##### 현재의 *<u>전역 심볼 테이블</u>*을 보여주는 *<u>딕셔너리를 반환</u>*하는 함수

###### -> 전역변수와 함수, 클래스의 정보 포함



#### 💼 locals()

##### 현재의 *<u>지역 심볼 테이블</u>*을 보여주는 *<u>딕셔너리를 반환</u>*하는 함수

###### -> 매개변수를 포함한 지역변수와 중첩함수의 정보 포함