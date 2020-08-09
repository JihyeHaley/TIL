odd = []
for i in range(1, 101):
    if i % 2 == 1:
        odd.append(i)

for i in range(0, len(odd)):
    if i != len(odd)-1:
        print(odd[i], end=', ')
    else:
        print(odd[i])