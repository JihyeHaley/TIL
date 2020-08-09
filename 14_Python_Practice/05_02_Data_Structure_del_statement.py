# del() Statement

a = [-1, 1, 66.25, 333, 333, 1234.5]
print('{:0.3f}' .format(a[2]))

del a[0]
print(a)

del a[2:4]
print(a) # 333, 333 만 사라짐
 
del a[:] # same with del a
print(a) # 전체삭제
