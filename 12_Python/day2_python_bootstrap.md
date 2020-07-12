# #2 Python :computer:

# 모듈 / 함수 / 라이브러리 (공적마스크 api)

**random 공식문서 url**

https://docs.python.org/ko/3.7/library/random.html



## Functions for sequences

- `random.choice`(*seq*)

  Return a random element from the non-empty sequence *seq*. If *seq* is empty, raises [`IndexError`](https://docs.python.org/ko/3.7/library/exceptions.html#IndexError).

- `random.``sample`(*population*, *k*)

  Return a *k* length list of unique elements chosen from the population sequence or set. Used for random sampling without replacement.

  Returns a new list containing elements from the population while leaving the original population unchanged. The resulting list is in selection order so that all sub-slices will also be valid random samples. This allows raffle winners (the sample) to be partitioned into grand prize and second place winners (the subslices).

  Members of the population need not be [hashable](https://docs.python.org/ko/3.7/glossary.html#term-hashable) or unique. If the population contains repeats, then each occurrence is a possible selection in the sample.

  To choose a sample from a range of integers, use a [`range()`](https://docs.python.org/ko/3.7/library/stdtypes.html#range) object as an argument. This is especially fast and space efficient for sampling from a large population: `sample(range(10000000), k=60)`.

  If the sample size is larger than the population size, a [`ValueError`](https://docs.python.org/ko/3.7/library/exceptions.html#ValueError) is raised.

- `random.``randrange`(*stop*)

  `random.``randrange`(*start*, *stop*[, *step*])

  Return a randomly selected element from `range(start, stop, step)`. This is equivalent to `choice(range(start, stop, step))`, but doesn’t actually build a range object.

  The positional argument pattern matches that of [`range()`](https://docs.python.org/ko/3.7/library/stdtypes.html#range). Keyword arguments should not be used because the function may use them in unexpected ways.

  *버전 3.2에서 변경:* [`randrange()`](https://docs.python.org/ko/3.7/library/random.html#random.randrange) is more sophisticated about producing equally distributed values. Formerly it used a style like `int(random()*n)` which could produce slightly uneven distributions.

요청, 응답




# HTML

#### CSS 보는 방법 



1. 키워드
2. 크기단위 
   * Pixel 
   * %
   * em
   * rem
   * viewpoint



### 선택자

1. 전체
2. ID
3. Class
4. (Tag)



a - > 클릭하고나면 색상이 바뀐다.

poeima



1. !important (우선)
2. HTML 에 직접
3. #id 
4. .class
5. 태그 이름 



# Box model

#### => 사각형

**차곡차곡 쌓아진다.**



1. Content (실제 내용)
2. Border (테두리)
3. Padding ( border contents 사이)
4. Margin (frame, frame 간의 거리)



기본적으로 모든 **html 코드는 한 줄**을 모두 차지한다.

박스를 쌓을 때마다 위에서부터 하나씩 차곡차곡 쌓여간다.



## 2. display 속성

1. block

   항상 새로운 라인에서 

   가로폭 다 차지 (width:100%)

   margin-left, margin-right 하면은 중앙으로 온다.

   * div, h1~~~~~~, p, a 

2. inline

   새로운 라인에서 시작하지 않으며 문장의 중간에 들어갈 수 있다.

   content의 너비만큼 박스의 크기만큼

   태그 끝나고 바로 붙어버리는 속성들

   상, 하 여백은 line-height로 지정한다.

   * span, a, strong, img, br, input,

3. inline-block

4. none

display: none (존재하지 않음)

visiblility : hidden (잠시 숨겨놓음)





## 3. Position 위치

1. static
2. relative
3. sdf
4. fixed(고정위치)



## 4. flex

* **justify-content**

  * `flex-start`: 요소들을 컨테이너의 왼쪽으로 정렬합니다.
  * `flex-end`: 요소들을 컨테이너의 오른쪽으로 정렬합니다.
  * `center`: 요소들을 컨테이너의 가운데로 정렬합니다.
  * `space-between`: 요소들 사이에 동일한 간격을 둡니다.
  * `space-around`: 요소들 주위에 동일한 간격을 둡니다.

  ![image-20200609170500961](C:\Users\ohhoj\AppData\Roaming\Typora\typora-user-images\image-20200609170500961.png)

* **align-items**

  * `flex-start`: 요소들을 컨테이너의 꼭대기로 정렬합니다.
  * `flex-end`: 요소들을 컨테이너의 바닥으로 정렬합니다.
  * `center`: 요소들을 컨테이너의 세로선 상의 가운데로 정렬합니다.
  * `baseline`: 요소들을 컨테이너의 시작 위치에 정렬합니다.
  * `stretch`: 요소들을 컨테이너에 맞도록 늘립니다.

  

* **flex-direction**

  * `row`: 요소들을 텍스트의 방향과 동일하게 정렬합니다.
  * `row-reverse`: 요소들을 텍스트의 반대 방향으로 정렬합니다.
  * `column`: 요소들을 위에서 아래로 정렬합니다.
  * `column-reverse`: 요소들을 아래에서 위로 정렬합니다.

  

* **align-self**는 개별 요소에 적용할 수 있는 또 다른 속성



* **flex-wrap**

  * `nowrap`: 모든 요소들을 한 줄에 정렬합니다.
  * `wrap`: 요소들을 여러 줄에 걸쳐 정렬합니다.
  * `wrap-reverse`: 요소들을 여러 줄에 걸쳐 반대로 정렬합니다.

  

* **flex-direction**과 **flex-wrap**이 자주 같이 사용되기 때문에, **flex-flow**가 이를 대신할 수 있습니다.





## Grid

* col

  * ![image-20200609171904825](C:\Users\ohhoj\AppData\Roaming\Typora\typora-user-images\image-20200609171904825.png)

  

* container / row

  * ![image-20200609172423276](C:\Users\ohhoj\AppData\Roaming\Typora\typora-user-images\image-20200609172423276.png)



* .offset
  * 몇칸 띄우고 해