times_3 = []
for i in range(1, 101):
    if i % 3 == 0:
        times_3.append(i)

times_3_sum = 0
for i in range(0, len(times_3)):
    times_3_sum = times_3_sum + times_3[i]

print(f'1부터 100사이의 숫자 중 3의 배수의 총합: {times_3_sum}')