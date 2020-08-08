# if Statement
x = int(input('enter a integer: '))

if x < 0 :
    x = 0
    print('Negative changed to zero')
elif x == 0 :
    print('It\'s zero')
elif x == 1 :
    print('Single')
else : 
    print('Over than 1')