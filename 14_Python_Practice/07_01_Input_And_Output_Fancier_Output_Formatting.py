import math
print(f'The Value of pi is approximately {math.pi:.3f}.')

table = {'Sjoerd': 4111, 'Jack' : 3111, 'Dcab' : 2111}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')


# if i WOULD LIKE TO EMPHASIZE a word use {!r}
animal = 'eels'
print(f'My hovercraf is full of {animal}.')
print(f'My hovercraf is full of {animal!r}.')

print('12'.zfill(5))
print('3.14'.zfill(7))
print('3.14444444'.zfill(5)) # ????