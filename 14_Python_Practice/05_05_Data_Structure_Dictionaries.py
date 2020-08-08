tel = {'jack': 4908, 'sape': 4139}
tel['guido'] = 4127
print(tel) 
print(tel['jack']) # 4908

del tel['sape'] # sape 삭제 // 아마 dict은 indx로 접근 안될거다
print(tel)

tel['irv'] = 4127
print(tel)

list(tel)
print(tel)
print(sorted(tel)) # key값만 sort되어서 return 된다
print(tel) 
print('guido' in tel) # True
print('jack' not in tel) # False

# 이렇게도 할 수 있따~~~~
print(dict([('sape', 4139), ('guido', 1234), ('jack', 4949)]))