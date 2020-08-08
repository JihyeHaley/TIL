## range()
print('''
for i in range(5):
    print(i)''')
for i in range(5):
    print(i)

print('''
for i in range(5, 10):
    print(i)''')
for i in range(5, 10):
    print(i)

print('''
for i in range(0, 10, 3):
    print(i)''')
for i in range(0, 10, 3):
    print(i)

print('''
for i in range(-10, -100, -30):
    print(i)''')
for i in range(-10, -100, -30):
    print(i)

# len()사용해서 해보기
a = ['Mary', 'had', 'a', 'litte', 'pet']
print('''
for i in range(len(a)):
    print(i, a[i])''')
for i in range(len(a)):
    print(i, a[i])

# enumerate()사용해서 해보기
a = ['Mary', 'had', 'a', 'litte', 'pet']
print('''
for idx, i in enumerate(a):
    print(idx, i)''')
for idx, i in enumerate(a):
    print(idx, i)

print('''
>>> print(range(5))
range(0, 5) 
로 리턴이 된다.. 

>>> print(list(range(5)))
[0, 1, 2, 3, 4]
로 해야지 "리스트 형태"로 리턴된다.
''')

print(list(range(5)))

