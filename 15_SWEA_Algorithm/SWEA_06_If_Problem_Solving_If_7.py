result = []
for i in range(1, 201):
    if i % 7 == 0:
        result.append(i) 

output = []
for j in range(0, len(result)):
    if result[j] % 5 != 0:
        output.append(result[j])

for k in range(0, len(output)):
    if k != len(output)-1:
        print(output[k], end=',')
    elif k == len(output)-1:
        print(output[k])