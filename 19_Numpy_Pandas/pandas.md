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

