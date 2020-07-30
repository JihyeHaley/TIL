print('slicing은 공간을 자르는거')

print('----slicing----')
sample_list = list(range(0,31))
print(list(range(0,31)))
print(sample_list)
print(sample_list[1:3])
print(sample_list[1:4])
print(sample_list[1:5])

# 거꾸로
print(sample_list[10:-1]) 
# a:b:c 는!! range(a:b)에서 slicing 3씩
print('# a:b:c 는!! range(a:b)에서 slicing c씩 slicing')
print(sample_list[0:len(sample_list):3])
print('# a::b 는!! lengh만큼 b씩 slicing')
print(sample_list[1::3])
print(sample_list[0::3])
print('# ::a (a>0) 는!! range(x,y) a씩 slicing')
print(sample_list[::3])
print('# ::a (a<0) 는!! range(x,y) 거꾸로 a씩 slicing')
print(sample_list[::-1])
print('if sample no single output')
print(sample_list[1:1])

