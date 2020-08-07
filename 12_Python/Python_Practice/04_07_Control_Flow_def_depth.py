## Keyword인자
print('''
[----function with keywords-----]
parrot(10000)
''')
def parrot(voltage, state='a staff', action='voom', type='Norwegian Blue'):
    print('--this parrot would\'t', action, end='\n')
    print('--if you put', voltage, 'volts through it.')
    print('--lovely plumage, the', type)
    print('--it\'s', state, '!')
parrot(1000)

print('''
[----function with keywords-----]
parrot(voltage=1000)
''')
parrot(voltage=1000)

print('''
[----function with keywords-----]
parrot(voltage=1000000, action='VOOOOOOM')
''')
parrot(voltage=1000000, action='VOOOOOOM')


print('''
[----function with keywords-----]
parrot('a million', 'before a life', 'jump')
''')
parrot('a million', 'before a life', 'jump')

print('''
[----function with keywords-----]
parrot('a thousand', state='pushing up the daisies')
''')
parrot('a thousand', state='pushing up the daisies')


# 4.7.2 Keyword Arguments
# 아래의 것들 에러났었음. 왜냐하면 *을 빼뜨렸었어서
# 인자에 있는 값들을 넣어서 사용해야한다.
print('''
----4.7.2 Keyword Arguments----
''')
print('''
*가 오타나 강조 표시가 아니라 함수에서 쓰이는 거니깐, 오타라고 생각하지 않기
*argument, **keywords를 
**keywords 
keywords[kw]는 dictionary처럼 접근 (key값으로)
''')
def cheeseshop(kind, *arguments, **keywords):
    print('-- Do you have any', kind, '?')
    print('-- I\'m sorry, we\'re all out of', kind)
    for arg in arguments:
        print(arg)
    print('-' * 40)
    for kw in keywords:
        print(kw, ':', keywords[kw])

cheeseshop('Limburger', 'It\'s very runny, sir.', 'It\'s really very, VERY runny, sir.', shopkeeper='Michael Palin', client='John Cleese', sketch='Cheese Shop Sketch')


# 4.7.3 Arbitrary Argument Lists
print('''
----4.7.3 Arbitrary Argument Lists----
''')

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def concat(*args, sep='/'):
    return sep.join(args)

print(concat('earth', 'mars', 'venus'))

print(concat('earth', 'mars', 'venus', sep='.'))


# 4.7.4 Unpacking Argument Lists
print('''
-----4.7.4 Unpacking Argument Lists-----
''')
# normal call with seperate arguments
list(range(3, 6))
# =>[3, 4, 5]

# call with arguments unpacked from a list
args = [3, 6]
print(list(range(*args)))
# =>[3, 4, 5]

# 4.7.5 Lamda Expressions
print('''
-----4.7.5 Lamda Expressions-----
''')

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print('''
f = make_incrementor(42)''')
print('f(0)->', f(0))
print('f(1)->', f(1))

paris = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
paris.sort(key=lambda pair: pair[1])
paris