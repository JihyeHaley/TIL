################################

# 1. 리스트 (List) - 가변
print('----Tuple----')
my_list = [10, '문자열', True]
print(my_list)
print(type(my_list))
print(my_list[1])

# 2. 튜플 (Tuple) - 불변
#튜플은 수정 불가능 (불변, immutable), 읽을 수 밖에 없다.
#직접 사용하지 보다는 파이썬 내부에서 사용하고 있다.
print('----Tuple----')
my_tuple1 = (1, 2)
print(my_tuple1) 
print(type(my_tuple1))


# 어떻게 내부에서 사용하고 있을까?
print('----Tuple ex1 ----')
my_tuple2 = 1,2
print(my_tuple2)
print(type(my_tuple2))

print('----Tuple ex2-1 ----') # 값을 넣어줄 때 x가 1일 거라는 보장을 해주는 거다.
x, y = 1, 2
print(x)
print(y)

print('----Tuple ex2-2 ----')
x, y = y, x
print(x)
print(y)

#하나의 요소로 구성된 튜플은 값 뒤에 쉼표를 붙여서 만든다.
print('---요소가 하나인 튜플 표현하기---')
single_tuple= ('hello',)
print(type(single_tuple))



# 3. range() 
# range는 숫자의 시퀀스를 나타내기 위해 사용
#a= [], b = list()
print('----range()----')
print(type(range(1))) 
print(range(10))
print(list(range(10)))

