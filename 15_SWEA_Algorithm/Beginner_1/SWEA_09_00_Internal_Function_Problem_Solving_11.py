str = 'abcdef'
num = list(range(0, 6))

per = dict(zip(str, num))

for num, key in enumerate(per):
    print(f'{key}: {num}')