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