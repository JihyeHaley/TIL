## List
print('''
- String은 불변(immutable)
- List는 가변(mutable)
''')
squares = [1, 4, 9, 16, 25]
print(squares)

# squares[:]은 전체가 다 나온다.
print(squares[:])

# square도 덧셈이 된다.
squares_added = squares + [36, 49, 64, 81, 100]
print(squares_added)

# 리스트는 가변이기 때문에 내용을 변경할 수 있다.
cubes = [1, 8, 27, 65, 125, 216]
print(cubes)
#...? 4*4*4는 64인데...?
# 바꿔보자
print('''cubes = [1, 8, 27, 65, 125, 216]가 틀림.
>>> cubes[3] = 64
>>> print(cubes)''')
cubes[3] = 64
print(cubes)

# append 사용하기
cubes.append(7**3)
print('''>>> cubes.append(216)
>>> cubes.append(7**3) #(똑같은 말)
>>> print(cubes)''')

print(cubes)

# 불변이니깐 변경도 가능 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 부분 변경하기 (다른 문자열로)
letters[2:5] = ['C', 'D', 'F']
print(letters)

# 부분 변경하기 (없애기)
letters[2:5] = []
print(letters)

# 부분 변경하기 (다 없애기)
letters[:] = []
print(letters)

# list는 R처럼... list안에 여러가지의 형태의 variable이 들어갈 수 있다.
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
z = [a, n, x]
print(z)
print(z[2][1][0])

a, b = 0, 1
print('a =', a)
print('b =', b)

while a < 100:
    print(a, end=',')
    a, b = b, a+b
    #print('a =', a, 'b =', b, 'a+b =', a+b)


