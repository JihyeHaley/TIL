# more on list

a = ['jihye', 'yeon', 'yule', 'haley']

# list.append(x) // append는 바로 출력 안해준다.
a.append('hyeon')
print(a)

# list.extend(iterable)
# list.insert(i, x)
# list.remove(x)
# list.index(x[, start[, end]])
# list.count(x)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print('print(fruits.count(\'apple\'))')
#2
print(fruits.count('apple'))

print('print(fruits.count(\'tangerine\'))')
#0 // boolean이 아닌 것 같다.
print(fruits.count('tangerine'))
print(type(fruits.count('tangerine')))

print('print(fruits.index(\'banana\'))')
#3 // index는 무조건 0부터 시작하니깐
print(fruits.index('banana'))

print('print(fruits.index(\'banana\', 4))')
# 6 // index!!! don't forget what number is beginner :)
# find next banana starting a position 4 and return what is the index of that.
print(fruits.index('banana', 4))




# 함수로 바로 나오는 것
# list.count()
# list.pop()
# list.clear()
# list.reverse()
# list.sort()
# list.copy()


