# API (Application Programming Interface)
# 내장함수!
#   수치형 데이터 조작을 위한 함수
#   집합과 원소 사이의 관계를 다루는 함수
#   각종 변환 함수

# 수칙연산 
# 절대값 // abs()
# 나머지 몫 // divmod()
# 제곱 // pow()
val1, val2 = 9, 5
result_tuple = divmod(val1, val2)

print('divmod({0}, {1}) => 몫: {2} 나머지:{3}' .format(val1, val2, *result_tuple))

data_list = [1, 2, 3, 4, 5]

print('pow({0}, 2) => {1}' .format(data_list[2], pow(data_list[2], 2)))

print('list(map(lambda x: pow(x, 2), {0})) => {1}' .format(data_list, list(map(lambda x: pow(x, 2), data_list))))



# filter

def iseven(num):
    return num % 2 == 0 # 짝수일 경우

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret_val = filter(iseven, numbers)
# ret_val = filter(lambda n: n % 2==0, numbers)
print(type(ret_val))
print(list(ret_val)) # 필터객체를 리스트로 변환 [2, 4, 6, 8, 10]

# list()
# tuple()
# set()
# dict()

data_str = 'hello'

print('''
list()''')
data_list = list(data_str) # 문자 하나하나가 list안에 변수로 전달됨
print(f'list({data_str}) => {type(data_list)} {data_list}')

print('''
tuple()''')
data_tuple = tuple(data_str) # 문자 하나하나가 tuple안에 변수로 전달됨
print(f'tuple({data_str}) => {type(data_tuple)} {data_tuple}')


print('''
set()''')
data_set = set(data_str) # 문자 하나하나가 set안에 변수로 전달됨, 겹치면 빠빠이.. 사라짐
print(f'set({data_str}) => {type(data_set)} {data_set}')

print('''
dict()''')
#data_set
data_dict = dict(enumerate(data_set)) # 문자 하나하나가 0~ n : str 
print(f'set({data_str}) => {type(data_dict)} {data_dict}')
#data_tuple
data_dict = dict(enumerate(data_tuple)) # 문자 하나하나가 0~ n : str
print(f'set({data_str}) => {type(data_dict)} {data_dict}')
# data_str
data_dict = dict(enumerate(data_str)) # 문자 하나하나가 0~ n : str
print(f'set({data_str}) => {type(data_dict)} {data_dict}')




print('''
map''')
data_list = list('abcdef')

result = list(map(lambda x: x.upper(), data_list))
print(f'List(map(lambda x: x.upper(), {data_list})) \n => {type(result)} {result}')



print('''
min() / max()''')

data_list = [1, 2, 3, 4, 5]

print(f'{data_list} => min:{min(data_list)}, max: {max(data_list)}')


print('''
zip()''')

data_list1 = [1, 2, 3]
data_list2 = [4, 5, 6]
data_list3 = ['a', 'b', 'c']


print(f'list(zip({data_list1}, {data_list2})) \n-> {list(zip(data_list1, data_list2))} ')
# [(1,4), (2,5), (3,6)]
print(f'list(zip({data_list1}, {data_list2}, {data_list3})) \n-> {list(zip(data_list1, data_list2, data_list3))} ')
# [(1,4,'a'), (2,5,'b'), (3,6,'c')]

#zip과 dict사용
print('''
dict(zip())''')
print(f'dict(zip({data_list1},  {data_list3})) \n-> {dict(zip(data_list1, data_list3))} ')
print(f'dict(zip({data_list3},  {data_list1})) \n-> {dict(zip(data_list3, data_list1))} ')



# 변환함수
# chr(), ord(), hex()

print('''
chr()''')
# 65 = A
val = 65
print(f'chr({val}) => {chr(val)}')

# 65 = a
val = 97
print(f'chr({val}) => {chr(val)}')


val_korean = 0xac00
print(f'chr(ac00) => {chr(val_korean)}')



print('''
ord()''')

val = 'A'
print(f'ord({val}) -> {ord(val)}')

val = 'a'
print(f'ord({val}) -> {ord(val)}')

val = '가'
print(f'ord({val}) -> {ord(val)}')

val = '가'
print(f'ord({val}) -> {hex(ord(val))}')



x = '10'
y = '3C'
z = 4.5

#2진수 -> 10진수
print(f'2진수 표현인 문자열\'{x}\'은(는) 10진수 {int(x, 2)}로 변환됩니다. ')
#16진수 -> 10진수
print(f'16진수 표현인 문자열\'{y}\'은(는) 10진수 {int(y, 16)}로 변환됩니다. ')
# 
print(f'int({z})은 {type(z)} {type(int(z))}을 {type(int(z))} {int(z)}로 변환됩니다.')
print(f'int({x})은 {type(x)} {type(int(x))}을 {type(float(x))} {float(x)}로 변환됩니다.')
print(f'str({z})은 {type(z)} {type(int(z))}을 {type(str(z))} \'{str(z)}\'로 변환됩니다.')
