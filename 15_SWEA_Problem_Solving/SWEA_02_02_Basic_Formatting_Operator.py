a = int(input('input a cm: '))
inch = 2.54
print('{:.2f} inch => {:.2f} cm' .format(a, a*inch))


kg = int(input('input a kg: '))
p = 2.2046
print('{0:.2f} kg =>  {1:.2f} lb' .format(kg, p*kg))

c = int(input('input a C: '))
print('{0:.2f} ℃ =>  {1:.2f} ℉' .format(c, 32+1.8*c))


print('혼합된 소금물의 농도: {0:.2f}%%' .format(20/300*100))