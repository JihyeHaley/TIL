# -*- coding: utf-8 -*-
##### for
for num in range(1,100,1):
    print(num)


result = []

for num in range(1, 31):
    if num % 2 == 1:
        result.append(num)
print(result)

# enumerate

lunch =['a', 'b', 'c']
for menu in lunch:
    print(menu)

print('---- enumerate ----')
lunch =['짜장면', 'b', 'c']
for idx, menu in enumerate(lunch):
    print(idx, menu)


print(enumerate(lunch))

print(type(enumerate(lunch)))
print(list(enumerate(lunch))) #<- tuples and list

print(type(list(enumerate(lunch))[0]))
print(type(list(enumerate(lunch))[1]))
print(type(list(enumerate(lunch))[2]))

