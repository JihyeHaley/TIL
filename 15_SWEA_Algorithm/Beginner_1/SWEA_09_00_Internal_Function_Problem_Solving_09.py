some = list(range(1, 11))
answer = list(filter(lambda x: x%2 == 0, some))
answer2 = list(map(lambda x: x**2, answer))
print(answer2)