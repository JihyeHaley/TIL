print('1. List(가변)')
print('-----List----')
print('List은 형태가 다른 아이들이 다 모일 수 있다.')
print('List은 순서는 0 부터 시작')
my_list = [10, '문자열', True]
print(my_list)
print(type(my_list))
print(my_list[0])
print(my_list[1])

print('2. Tuple(불변)')
print('-----Tuple----')
print('Tuple is immutable. not availabel to edit only for reading')
print('Tuple도 순서는 0 부터 시작')
my_tuple1 = (1, 2)
print('Tupled은 괄호도 필요없다')
my_tuple1_1 = 4,5
print(my_tuple1)
print(type(my_tuple1))
print(type(my_tuple1_1))
print(my_tuple1[0])
print(my_tuple1[1])
print(my_tuple1_1[0])
print(my_tuple1_1[1])


print('----Tuple example1----')
my_tuple2 = 91, 97
print(my_tuple2)
print(type(my_tuple2))

print('----Tuple example2----')
print('when 특정 변수값을 보장')
x, y = '지혜' , '성진'
print(x)
print(y)

print('----Tuple usages----')
usage_of_tuple = ('hello',)
about_list = ('hello')
print(type(usage_of_tuple))
print(type(about_list))
print('need to check whether i used , or not')



print('3. range()')
print('range는 숫자의 시퀀스를 나타내기 위해서 사용')
print('a = [], b = list()')
print('-----range()----')
print(type(range(1)))
print(range(10))
print('** range(10)을 보면 알 수 있는 거 하나. 0 부터 시작')
print(list(range(10)))
print('** list(range(10))을 보면 알 수 있는 거 하나. 0부터 10개 그래서 0부터 9까지 :)')
print(list(range(9)))
print(list(range(2,30)))
print('첫번째 인자부터 두번째 인자 만큼의 숫자를 더 줘 가 아님!!!')