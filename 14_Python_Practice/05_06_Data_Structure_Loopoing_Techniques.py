knights = {'gallahad' : 'the pure', 'robin' : 'the brave'}
print('\n')
for k, v in knights.items():
    print(k, 'is viewed as', v)

print('\n')
for i, v in enumerate(knights):
    print(i, ': ', v)

questions = ['name', 'quest', 'favorite color']
answers = ['jihye', 'the holy let see...', 'purple']
for q, a in zip(questions, answers):
    print('What is your {}? \tIt is {}\n' .format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# set을 하면 겹치는건 merge? 되기 때문에
basket_list = []
for f in sorted(set(basket)):
    basket_list.append(f)
print(basket_list)


import math 
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data= []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

print(float('NaN')) # nan