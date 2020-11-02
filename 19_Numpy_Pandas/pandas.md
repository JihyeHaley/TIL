# Pandas 
* 판다스는 데이터 과학을 위해 꼭 필요한 파이썬 라이브러리 중 하나다. 
`pip install pandas` 로 설치한다.
실행할 파일 안에서 `import pandas`도 잊지말자

#### 판다스 데이터 구조
| 시리즈       | Series     | 1차원 |
| ------------ | ---------- | ----- |
| 데이터프레임 | Data Frame | 2차원 |
| 패털         | Panel      | 3차원 |

## 1차원 데이터 - 시리즈(Series) 만들기
`pandas.Series(data, index, dtype, copy)`

```python
a = pandas.Series([1, 3, 5, 7, 10])
print(a)

하면 
# 0     1
# 1     3
# 2     5
# 3     7
# 4     10
# dtype : int 64
```



#### Test1

```python
import codecademylib

import pandas as pd



df1 = pd.DataFrame({

  'Product ID': [1, 2, 3, 4],

  'Product Name' : ['t-shirt', 't-shirt', 'skirt', 'skirt'],

  'Color' : ['blue', 'green', 'red', 'black'],

  #  add Product Name and Color here

})



print(df1)
```



#### test2

```python
import codecademylib
import pandas as pd

df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115],
  # Fill in rows 3 and 4
],
  columns=['Store ID', 'Location', 'Number of Employees'
    #add column names here
  ])

print(df2)
```



##### CSV writing

do not have any spaces in the csv information

s

##### Inspect a Data Frame

do not have any spaces in the csv information





##### Test 7

```python
import codecademylib
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north = df['clinic_north']
print(type(clinic_north))
```





##### test8

```python
import codecademylib
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)


clinic_north_south = df[['clinic_north', 'clinic_south']]
print(type(clinic_north_south))
```





##### test 9

```python
import codecademylib
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])


march = df.iloc[2]
```

