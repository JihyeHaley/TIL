print('hello, world!')

#변수선언
number = 10 
string = '문자열'
bools= True #Boolean

print(number, string, bools)

#숫자형(int, float, complex(복소수))
a = 4
print(type(a)) # type 확인  -> class로 나온다. ('int', 'str', 'bool' etc...)

#bool
print(type(False))
# 0, 0.0, (), [], {}, '', None(값이 없음) - > Flase로 처리된다.

#문자형 (한 프로젝트에서 single, double 로 할지 정하고 고대로만 가기)
greeting = 'Hi,'
name = 'Haley'
print(greeting, name)
print(type(name))

#사용자의 입력을 받는
#age = input( ) # 입력받는 값은 absolutely "스트링 타입"
#print(age)
#print(type(age))

print("""
개행문자 없이
여러줄을
그대로 출력 가능합니다.
""")

print(3*'hey '+'yo!') # 사칙연산 순사대로 출력이 된다.

######################################################
# 이제 중요한거 나온다!
#***String interpolation 
######################################################

name = 'Jihye'
#1. % formatting
print('hello, %s' %name)

#2. .format()
print('hello, {}' .format(name))

#3. f-string (Literal String Interpolation) (3.6+ ver 부터 나온 것)
print(f'hello, {name}')

pi = 3.141592
print(f'원주율은 {pi:.4}. 반지름이 2일 때 원의 넓이는 {2*2*pi}')
