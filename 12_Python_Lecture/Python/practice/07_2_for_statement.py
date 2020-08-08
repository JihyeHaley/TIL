for num in range(1, 100, 1):
    print(num)


result = []
# print(type(result))

for num in range(1, 31):
    result.append(num)
print(result)

lunch = ['오', '아', '카']
for menu in lunch:
    print(menu)


print('---- enumerate ----')

for idx, menu in enumerate(lunch):
    print(idx, menu)

print(enumerate(lunch))

print(type(enumerate(lunch)))
print(type(list(enumerate(lunch))))
print(list(enumerate(lunch)))

print(list(enumerate(lunch))[0])
print(type(list(enumerate(lunch))[0]))