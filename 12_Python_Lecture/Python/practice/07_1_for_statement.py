for num in range(1, 101, 1):
    print(num)

result = []

for num in range(1, 31):
    if num %2 == 1:
        result.append(num)
print(result)

print('enumerate')

lunch = ['a', 'b', 'c']
for menu in lunch:
    print(menu)

print('-----enumberate-----')
for index, menu in enumerate(lunch):
    print(index, menu)

print(enumerate(lunch))
print(type(enumerate(lunch)))
print(list(enumerate(lunch)))

print((list(enumerate(lunch))[0]))
print(type(list(enumerate(lunch))[1]))
print(type(list(enumerate(lunch))[2]))