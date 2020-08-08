## 20200802_list_comprehesion

```python
gugu = []
for a in range(2, 10):
    print(f'----{a}단-----')
    for b in range(1, 10):
        print(a, ' * ', b, ' = ', a*b)
        gugu.append(b*a)
```



❓여기서 print는 어떻게 쓸깡?

```python
gugu_2 = [a * b for a in range(2, 10) for b in range(1, 10) ]
print(gugu_2)
```



