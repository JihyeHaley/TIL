# %s '문자열 포맷'
# %c '문자 포맷. 정수를 유니코드 문자로 변환해 출력'
# %d '10진 정수로 출력'
# %o '8진수로 출력'
# %x '16진수로 출력'
# %f '부동소수점 숫자로 출력. 소수점 이하 6자리의 정밀도를 기본값으로 가짐'
# % '% 문자 자체를 출력

print('ㅇㅣ름 :%s' %'지혜')
print('''
c: %c (문자포맷, 정수를 유니코드로)
d: %d (10진수 정수로 출력)
c: %c (8진수로 출력)
x: %x (16진수로 출력)
f: %f (소수점까지 6개 나옴.)
d: %d (3.14를 정수로)
''' %(97, 97, 97, 97, 3.14, 3.14))

# %를 문자열로 쓰고 싶은데 문자열 포맷팅이 있다면 %%로 쓰면된다.
print('%d 점은 상위 %d%%에 속합니다.' %(97,1))

# 문자열 포맷팅이 없을때는 그냥 %만 쓰면 된다.
print('이름 :%', '지혜')

# 문자열 출력의 폭과 정렬 방향 (글자표현 10개)
print('%10s' %'우측정렬') 
print('%-10s' %'좌측정렬')

# 부등소수점 숫자의 출력 폭 지정
print('%f' %3.141592)
print('%0.2f' %3.141592)

# 숫자표현 우측정렬 10칸
print('%10.2f' %3.141592)
# 숫자표현 좌측정렬 10칸
print('%-10.2f' %3.141592)
# 숫자표현 10개, 앞에 공백은 0으로 채워
print('%010.2f' %3.141592)

# str.format()함수 사용해서
print('이름: {0}, 나이: {1}' .format('지혜', 22))

# %안쓰고 :으로 해결
print('{0:c} => {1}' .format(97, 97))
print('{0}, {1}, {2:x}' .format('가', ord('가'), ord('가')))
print('{0:10f} \n{1:10.2f}' .format(3.14, 3.14))
print('{name}, {age}' .format(name='jihye', age='23'))

# format으로 정렬
print('{0:<10}' .format('좌측정렬'))
print('{0:>10}' .format('우측정렬'))


# set은 동일한 변수가 들어갈 수 없으며 index로 접근할 수 없다.
# tuple ()
# list []
# set {}
# dictionary {} collection 자료형 중 하나 key
#  key가 동일하면 저장된 항목 변경, 동일하지 않으면 새로 추가

student = {'a', 'b', 'c', 'a'}
print(student)
# 합집합
student |= {'c', 'd'}
print(student)

dogs = {1: 'a', 2:'b', 3:'c'}
# key로 접근
print(dogs[1])
print(dir(dict))
# key만 다 보여줘
print(dogs.keys())

# value만 다 보여줘 
print(dogs.values())

# dict_items로 다 보여줘 [(key, value)---]
print(type(dogs.items()))

# key값으로 접근해서 보여줘 (없는 key로 접근하면 none이 나온다.)
print(dogs.get(1))
print(dogs.get(5))
# print(dogs[4]) Error

# 변수의 제거
del(dogs)
# print(dogs)

# 객체가 사용한 메모리 공간 자동관리
# 개발자가 메모리 관리를 직접할 필요 없음


print('''
----SWEA기출 python  대빵 쉬운거----
''')
# print(list(range(0, 1)))
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
T = int(input('input a number: '))
result = 0
print('''
Let me show you how to calculation a + aa + aaa + aaaa''')
for tc in range(0, 4):
    for i in range(0, tc+1):
        semi = int(T*10*(10**(i-1)))
        result = result + semi
    print(result)   

# print(5+55+555+5555)

