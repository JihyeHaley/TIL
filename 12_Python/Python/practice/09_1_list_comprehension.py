my_list = []

for x in range(10):
    my_list.append(x**2)
print(my_list)


my_newlist = [x**2 for x in range(10)]
my_newlist2 = list(x**2 for x in range(10))
print('----my_newlist----')
print(my_newlist)
print('----my_newlist2----')
print(my_newlist2)


print('\n----list comprehension----')
numbers = list(range(10,100,10))
print(numbers)


my_numbers_1 = []
my_numbers_1 = [number for number in numbers if number % 4 == 0]
print(my_numbers_1)
# my_numbers_1 -> 20, 40, 60, 80 출력될 것 같다.


my_numbers_2 = []
for number in numbers :
    if number >= 50:
        my_numbers_2.append(number + 7)
    else:
        my_numbers_2.append(number + 5)

print(my_numbers_2)


#조건표현식
#true_value <if> 조건식 <else> false_value
print('----조건표현식----')
print('''
true_valule <if> 조건식 <else> false_value
''')
my_numbers_2 = [number + 7 if number >= 50 else number +5 for number in numbers]
print(my_numbers_2)

gugu = []
for a in range(2, 10):
    print(f'----{a}단-----')
    for b in range(1, 10):
        print(a, ' * ', b, ' = ', a*b)
        gugu.append(b*a)

gugu_2 = [a * b for a in range(2, 10) for b in range(1, 10) ]
print(gugu_2)