a = int(input())
count = {}
# list(range(0,10))

for i in range(0, 10):
    i_to_str = str(i)
    count[i_to_str] = 0
# print(count)

compare = str(a)

for i in range(0, len(compare)):
    for j in range(0, 10):
        j_to_str = str(j)
        if compare[i] == j_to_str:
            count[j_to_str] = count[j_to_str] + 1


# 0~ 9 c출력
for i in range(0, 10):
    if i != 9:
        print(i, end=' ')
    elif i == 9:
        print(i)

# dict 에 넣어준 것들 뽑아주기
for i in range(0, 10):
    if i != 9:
        i_to_str = str(i)
        print(count[i_to_str], end=' ')
    elif i == 9:
        print(count[i_to_str])