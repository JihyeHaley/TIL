ordinary = [1, 2, 3, 4, 3, 2, 1]
changed = set(ordinary)
output = []
again = []
print(ordinary)

for i in range(0, len(changed)):
    output.append(changed.pop())

for i in range(0, len(output)):
    again.append(output.pop()) 

print(again)