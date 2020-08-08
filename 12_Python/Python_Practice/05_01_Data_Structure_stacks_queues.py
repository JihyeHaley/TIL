print('\n\n')
for i in range(0, 40):
    if i <=37:
        print('-', end='')
    elif i==38:
        print('''
Stacks is "Last In First Out" ...... LIKE 계산기
Queues is "First In First Out"''')
    else:
        for j in range(0,38):
            print('-', end='')
            if j ==37:
                print('-')
                print('----Stack----')
                print('\"Last In First Out\"(LIFO)')
                for k in range(0,38):
                    print('-', end='')
                    if k ==37:
                        print('-')

print('\n\n')
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print('\n\n')

# Queues
for i in range(0,38):
    print('-', end='')
    if i == 37:
        print('-')
        print('----Queues----')
        print('\"First In First Out\"(FIFO)')
        for j in range(0,38):
            print('-', end='')
            if j ==37:
                print('\n')

from collections import deque
# in order to use Queues .... need to use library :)

# .leftpop()
print('----.leftpop()----')
queue1 = deque(['Eric', 'John', 'Michael'])
queue1.append('Terry') # Terry Arrives
queue1.append('Graham') # Graham Arrives
queue1.popleft() # Eric Out, The First to arrives now leaves
queue1.popleft() # John Out, The Second to arrives now leaves
print(queue1) # ['Terry', 'Graham', 'Michael']
print('\n\n')
# .popright()는 없다.. ㅎㅎ
# print('----.rightpop()----')
# queue2 = deque(['Eric', 'John', 'Michael'])
# queue2.insert(0, 'Terry')
# queue2.insert(1, 'Graham')
# queue2.popright() # Graham Out
# queue2.popright() # Terry Out
# print(queue2) # ['Eirc', 'John', 'Michael']

# List Comprehension
for i in range(0,38):
    print('-', end='')
    if i == 37:
        print('-')
        print('----List Comprehension----')
        for j in range(0,38):
            print('-', end='')
            if j ==37:
                print('\n')

squares = []
for x in range(10):
    squares.append(x**2)
    print(squares)

# 람다를 활용해서
squares = list(map(lambda x:x**2, range(10)))
print(squares)

# loop comprehension
# which is more concise and readable.
squares = [x**2 for x in range(10)]
print(squares)


print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

print([(x, y) for x in [1, 2, 3] for y in [2, 3, 4] if x == y])

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)

vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec]) # [-8, -4, 0, 4, 8]
print([x for x in vec if x >= 0]) # [0, 2, 4]
print([abs(x) for x in vec]) # [4, 2, 0, 2, 4]// abs() <- 이 함수는 음수를양수로 변환하는건가..? 


passionfruits = ['    bannana', '    loganberry', 'passion fruit  ']
print([weapon.split() for weapon in passionfruits])
print([weapon.strip() for weapon in passionfruits])

# tuple in comprehension
# tuple should be parenthesized
print([(x, x**2) for x in range(6)])
# otherwise error ... let's see
print('''
Let's what happened without parenthesize

>>> [x, x**2 for x in range(6)]
File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax
...... no way!!! don't forget what kind of type I'm using :)
''')

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]
print([num for elem in vec for num in elem])
for elem in vec:
    for num in elem:
        print(num)
        print('\t')

from math import pi

# round(a, b)는 소수점 b 자리까지 반올림
print([str(round(pi, i)) for i in range(1,6)])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)


# 자.. 똑같은 얘기를 계속 해볼거에요... :)
print([row[i] for row in matrix for i in range(4)])
print([[row[i] for row in matrix] for i in range(4)])
for i in range(4):
    for row in matrix:
        print(row[i], end=' ')
    print('\t')


transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)


transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i]) 
        # 1, 5, 9 / 2, 6, 10 / 3, 7, 11 / 4, 8, 12
    transposed.append(transposed_row)
print(transposed)


print('''

In the real world, 
you should prefer built-in functions to complex flow statements. 
The zip() function would do a great job for this use case:

>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]


zip은 좀 어렵네요..
''')