import random

numbers = range(1, 10)

result = random.choice(numbers)
print(result)


pick = random.choice(range(10))
print(pick)

n = random.sample(range(20), 3)
print(n)


print(list(dir(random)))