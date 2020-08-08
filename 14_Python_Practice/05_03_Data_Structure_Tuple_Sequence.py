t = 12345, 54321, 'hello!'
print(t[0])
u = t, (1, 2, 3, 4, 5)
print(u)

print('Tuple is immutable. Otherwise, List is mmutable') # 변경할 수 없다.
# t[0] = 88888 # // error난다.

v = ([1, 2, 3], [3, 2, 1])
print(v)

empty = ()
singleton = 'hello', # <-- note trailing comma
len(empty)

len(singleton)
print(singleton)

x, y, z = t
print(t)
# t에 3개의 튜플 변수가 있으니깐  하나씩 저장된다고 생각하기
print('''
t에 3개의 튜플 변수가 있으니깐  하나씩 저장된다고 생각하기
>>> x, y, z = t
>>> print(x) 
    12345 # t[0]
>>> print(y) 
    54321 # t[1]
>>> print(z) 
    hello! # t[2]
''')
# print(x)
# print(y)
# print(z)

print('''

"Sequence unpacking" 
This is called, appropriately enough, sequence unpacking 
and works for any sequence on the right-hand side. 

Sequence unpacking requires that there are as many variables 
on the left side of the equals sign as codethere are elements in the sequence. 
Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.
''')