print('hello, world!')

number = 10
string = '環じ'
bools = True #boolean

print(number, string, bools)

a=4
print(type(a))

print(type(False))

greeting = 'Hi,'
name = 'Jihye'
print(greeting, name)

print(type(name))

print("""
아하아하
이거 신기한데?
""")

print(3*'hey '+'yo!')

name = 'Jihye'
print('1. formatting')
print('hello, %s' %name)

print('2. format()')
print('hello, {}' .format(name))

print('3. f-string (Literal String Interpolation)')
print(f'hello, {name}')
name2='seongjin'
print(f'hello, {name2}')

pi = 3.141592
print(f'원주율은 {pi:.4}. 반지름이 2일 때 원의 넓이는 {2*2*pi}')
