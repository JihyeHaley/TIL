even = []

for i in range(100, 301):
    compare = str(i)
    # str을 다 쪼개서 보기
    a = int(compare[0])
    b = int(compare[1])
    c = int(compare[2])
    if a%2 == 0 and b%2 == 0 and c%2 == 0:
        even.append(compare)

for j in range(0, len(even)):
    if j != len(even)-1:
        print(even[j], end=',')
    else:
        print(even[j])