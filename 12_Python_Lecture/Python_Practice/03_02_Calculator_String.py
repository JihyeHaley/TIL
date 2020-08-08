## String

# 출력할때 '' 혹은 ""을 사용해야한다.
print('spam eggs')
print('\'강조강조 백스페이스 쓴거!\'')

# \ 백스페이스를 날 문자로 쓰고 싶을때 
# ex1. \n은 한줄 띄기라서 enter효과
print('C:\some\name')

# ex2. r'\n'은 생 문자로 쓰기위해서 raw
print(r'C:\some\name')

python1 = 'which is short lanauage'
python2 = ('which is short lanauage')
print(python1)
print(python2)

# 변수들끼리 연결해줄려면 + 기호를 사용해라!
print('-----+를 활용한 변수 연결----')
a = 'an'
b = r'\n angel'
c = a + b
print(c) 

# 변수에서 숫자로 접근하기
word = 'python'
number = '123456'
back = '-6 -5 -4 -3 -2 -1'
print(word+'\n'+number+'\n'+back)
print(word[0])
print(word[1])
print(word[2])
print('음수로도 접근 가능')
print(word[-1])
print(word[-2])
print(word[-3])

### Slicing
print('----slicing----')
print(word[0:2])
print(word[2:5])

# s[:i]+s[i:]는 s가 된다.
print('----s[:i]+s[i:]는 s가 된다.----')
print(word[:2]+word[2:])

# s[a:b]에서 a에 음수가 들어갈 수 있다.
print('----example of a<0----')
print(word[-2:])

### len()
s = 'supadupaabc'
print(len(s))

### formatting &format & f-string 사용법

name = 'Yeon'

#1 . % formatting
print('hello, %s' %name)

#2 . .format()
print('hello, {}' .format(name))

#3 . f-string
print(f'hello, {name}')


