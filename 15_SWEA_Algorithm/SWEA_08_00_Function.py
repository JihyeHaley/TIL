a, b = 2, 3

# interpretor언어이기 때문에 한줄씩 해석하니깐 위치가 엄청 중요하다.
# 함수 선언 
# def 함수명(매개변수):
# return 문

def calc_sum(x, y):
    return x + y

c = calc_sum(a, b) # 반환값(5)이 변수 c에 저장
d = calc_sum(a, c) # 반환값(7)이 변수 d에 저장
print(f'{c}, {d}')


# 언팩 연산자
# 매개변수의 개수를 제한하지 않고 넣어주는 만큼 매개변수로 사용할 수 있도록
def calc_sum2(*params):
    total = 0 
    for val in params:
        total += val 
        # total = total + val
    return total
    # 변수 total값이 calc_sum()함수를 호출한 위치에 반환 값으로 전달


print(calc_sum2(1, 2))
print(calc_sum2(1, 2, 3))

# 언팩 연산자는 반환값을 2개 만들 수 있다.
def calc_sum3(precision, *params):
    if precision == 0 :
        total = 0
    elif 0 < precision < 1:
        total = 0.0

    for val in params:
        total += val

    return total

print(calc_sum3(0, 1, 2, 3))
print(calc_sum3(0.2, 1, 2, 3))



# 언팩 연산자를 사용하는 튜플 형식의 반환값

def calc_sum4(precision1, precision2, *params):
    if precision1 == 0:
        total1 = 0
    elif 0 < precision1 < 1:
        total1 = 0.0

    if precision2 == 0:
        total2 = 0
    elif 0 < precision2 < 1:
        total2 = 0.0

    for val in params:
        total1 += val
        total2 += val

    return total1, total2 # 투플을 반환해서 하나 이상의 값을 반환할 수 있다.



# 키워드 언팩 연산자
def use_keyword_arg_unpacking(**params):
    for k in params.keys():
        print(f'{k}: {params[k]}')

print(use_keyword_arg_unpacking(jihye='no.1', haley='no.2', yeon='no.0'))



# 기본 값 (defaul)을 갖는 매개변수 
# tuple로  리턴된다.
def calc(x, y, operator='+'):
    # 만약에 operator의 값이 생략되면 defaul 값으로 +로 사용되는거
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '/':
        return x//y, '---', x%y 
    elif operator == '*':
        return x*y

print(calc(1, 2)) # 3
print(calc(1, 2, '+')) # 3 
print(calc(1, 2, '-')) # -1
print(calc(4, 3, '/')) # 1 --- 1 // 튜플로 리턴 되는 걸 알 수 있다.
print(calc(4, 3, '*')) # 12


# Scope 변수의 유효 범위
# 어디서나 접근 가능한 전역 변수 => 전역 스코프
# 함수 내에서만 접근 가능한 지역 변수 => 함수 스코프

def test_scope(a):
    result = a + 1 # 지역변수
    print(f'\n\ttest_scope() 안에서의 a의 값: {a}')
    print(f'\ttest_scope() 안에서의 result값: {result}\n')
    return result

x = 5
print(f'test_scope() 호출전의 x 값 {x}')
ret_val = test_scope(x)
print(f'test_scope() 함수가 반환한 값: {ret_val}')
print(f'test_scope() 호출후의 x 값 {x}')


def change_gloabl_var():
    global x # 함수 내에서 x는 전역변수를 가리킴 (밖엥 있는거)
    x += 1 # 변수 x의 값 5가 인자로 전달되고, 1을 더한 결과값 반환

x = 5
change_gloabl_var()
print(f'전역변수 x의 값: {x}') # global x를 통해서 함수 밖에 있는 전역변수값을 바꿔줘서 x가 6이됨


# 중첩함수
def calc2(operator_fn, x, y): 
    # 매개변수 operator_fun에 전달된 함수를 실행해 반환된 값을 return 문을 통해반환
    return operator_fn(x, y)

def plus(op1, op2):
    return op1 + op2

def minus(op1, op2):
    return op1 - op2

ret_val = calc2(plus, 10, 5) #calc2 함수에서 operator_fn에 plus를 대입
print(f'calc2(plus, 10, 5)의 결과 값: {ret_val}')
ret_val = calc2(minus, 10, 5) #calc2 함수에서 operator_fn에 minus 대입
print(f'calc2(plus, 10, 5)의 결과 값: {ret_val}')


# 람다식

def calc3(operator_fn, x, y):
    return operator_fn(x, y)

ret_val = calc3(lambda a, b: a + b, 10, 5)
print(f'calc3(lamdba a, b: a + b, 10, 5)의 결과값: {ret_val}')
ret_val = calc3(lambda a, b: a - b, 10, 5)
print(f'calc3(lamdba a, b: a - b, 10, 5)의 결과값: {ret_val}')

#closure 
def outer_func():
    id = 0 # 지역 변수: 함수 내의 코드 또는 중첩 함수내에서만 접근 가능
    def inner_func():
        nonlocal id 
        # 변수id가 중첩함수인 inner_func 함수의 지역변수가 아님
        # 변수id 접근 시 outer_func 함수 스코프에서 찾게 만듦
        id += 1 
        return id
    return inner_func # 함수 호출이 아닌 함수에 대한 참조를 반환


print('''
outer_func()을 부르면 inner_func()이 반환된다는걸 잊지마!
''')

make_id = outer_func() # 이게 함수가 되는 거!!!!!

print(f'make_id() 호출의 결과: {make_id()}')
print(f'make_id() 호출의 결과: {make_id()}')
print(f'make_id() 호출의 결과: {make_id()}')

print('''
1. 중첩함수(inner_func() 호출)
2. outer_func()함수의 지역변수 id의 값 1씩 증가
3. 증가된 id 값 반환
4. str.format() 함수의 인자로 전달, 변환 문자열 생성
5. print() 함수를 통해 표준출력으로 출력
''')

def input_r():
    r = float(input('반지름을 입력하세요: '))
    return r
    
def round_size(r):
    return r**2*3.14
def round_side(r): 
    return r*2*3.14
    
r = input_r()
round_size = round_size(r)
round_side= round_side(r)
print(f'원의 면적:{round_size:.2f}, 원의 둘레: {round_side:.2f}')

