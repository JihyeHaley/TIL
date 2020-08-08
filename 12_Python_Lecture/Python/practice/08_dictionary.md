## 20200802_Dictionary

dictionary 함수 사용해서 출력되는 것들이 다름.

*dictionary는  key로 접근해서 출력한다.*

```python
# dict item 으로 value 출력
print('----dict items----')
for member in classroom.items():
    print(member)
```

* **tuple**로 출력됨.

```python
# dict item 으로 value 출력
print('----dict items----')
for key, value in classroom.items():
    print(key, value)
```

*  **str**로 출력됨.

