import math

print(f'math.randian(90) = {math.radians(90)}') # 각도를 인자로 전달하면 라디안 변화 값 반환
print(f'math.ceil(3.2) = {math.ceil(3.2)}') # 올림 => 4
print(f'math.floor(3.2) = {math.floor(3.2)}')  #버림 => 3

print(f'math.pi = {math.pi}') # 3.14~~~~~~~


# import ~ as ~
# 별칭을 사용하면 편리하게 코딩할 수 있다.

import math as m
print('m.radians(90)')

# from ~ import ~

# from math import radians, ceil, floor, pi
# from math import * # 전체 다 가져와라


# sys 모듈
import sys 
# sys.argv : 리스트 타입, 명령행에서 python명령에 전달된 인자들의 정보를 담고 있음
print(f'sys.argv => {type(sys.argv)} {sys.argv}')


# edit -> run configuration -> parameter(1 2 3 ) // 꼭 공백을 유지하후
for i, val in enumerate(sys.argv):
    print(f'sys.argv[{i}] => {val}')

# random 모듈 // 난수발생
import random
from random import random, uniform, randrange, choice, choices, sample, shuffle
# random 함수는 0.0 <= N < 1.0 범위의 부동소수점 난수 N 반환
# uniform 함수는 지정된 범위 내의 부동소수점 난수 N 반환
# randrange 함수는 정수형 난수 N 생성
print('random()=> {0}' .format(random()))
print('uniform({0}, {1}) => {2}' .format(1.0, 10.0, uniform(1.0, 10.0)))

start, stop, step = 1, 45, 2
print('randrange({0}, {1}) => {2}' .format(start, stop, randrange(1, 45)))
print('randrange({0}) => {1}' .format(start, randrange(stop)))
print(f'randranage({start} , {stop}, {step}) => {randrange(start, stop, step)}')


# choice(data_list) // List에서 1개 반환
# choice(data_list, k=2) // List에서 무엇을 몇개 반환 (1개 뽑고도 그 숫자를 또 뽑을 수 있다.)


# sample() // 인자로 전달된 시퀀스 객체, 혹은 set 객체 항목 중 임의의 k개 반환, 비복원추출 기능을 가진 시뮬레이션 함수

# shuffle() // 인자로 전달된 시퀀스 객체의 항목을 뒤섞는 함수, 반환값은 없고 원본 객체의 항목의 순서를 뒤섞음


# datetime() // 날짜와 시간 정보를 확인하고 조작하는 클래스, 모듈

from datetime import datetime, timezone, timedelta

# datetime()
# datetime.now()
now = datetime.now()
print(f'{now.year}-{now.month}-{now.day}  {now.hour}:{now.minute}:{now.second}')
print(f'{now.year}-{now.month:02}-{now.day:02}  {now.hour:02}:{now.minute:02}:{now.second:02}')

# datetime.now.strftime()
fmt = '%Y{0} %m{1} %d{2} %H{3} %M{4} %S{5}'
print(now.strftime(fmt).format(*'년월일시분초')) # 인자 언팩 연산자 적용