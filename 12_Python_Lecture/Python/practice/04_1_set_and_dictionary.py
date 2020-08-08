#1.set 

print('----set----')
set_a = {1, 2, 3}
set_b = {3, 6, 9}

print(set_a - set_b)
print(set_a | set_b)
print(set_a & set_b)

set_c = set()
#set은 class를 통해서 선언을 해주고 사용해야 한다.

#2. dictionary
print('----dictionary----')
dict_a = {1: 1, 2: 2, 3: 3}
print(dict_a)
print(type(dict_a))
print(type(set_c))
dict_b = dict()
print(type(dict_b))

print('\n-----dictionary read----')
phone_book={
    '서울' : '02',
    '경기' : '031',
}

print(phone_book['서울'])
# print(dir(dict))
print(phone_book.values())