## for 과 else의 관계
## try를 쓸 줄 알아야 하겠다.
## if 에서의 braek도 있다.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

print('''
try 문의 else 절은 예외가 발생하지 않을 때 실행되고, 
for 문의 else 절은 break 가 발생하지 않을 때 실행됩니다.
''')
print(list(range(2,2)))
print(list(range(2,3)))
print(list(range(2,4)))
print(list(range(2,5)))


## continue 
for num in range(2, 10):
    if num % 2 == 0:
        print('Found an even number', num)
        continue
    print('Found a number', num)