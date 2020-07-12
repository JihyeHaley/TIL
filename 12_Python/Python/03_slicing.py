######################## slicing ########################
#slicing은 공간을 자른 것

print('----slicing-----')
sample_list = list(range(0,31))
print(sample_list)
print(sample_list[1:4])
print(sample_list[10:-1])
print(sample_list[0:len(sample_list):3])
print('----- slicing 중간 생략 -----')
print(sample_list[0::3]) 
print('----- slicing처음 중간 생략 -----')
print(sample_list[::3]) 
print('----slicing 역순-----')
print(sample_list[::-1]) 
print('----- slicing 암것도 안나옴 -----')
print(sample_list[1:1])