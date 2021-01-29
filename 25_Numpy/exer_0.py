import numpy as np

# 1차원
array1 = np.array([1, 2, 3])
print(array1)
# print('array1 type:', type(array1))
# print('array1 array 형태:', array1.shape)
print('array1 array 차원:', array1.ndim)

# 2차원
array2 = np.array([[1, 2, 3], [2, 3, 4]]) 3
# print(array2)
# print('array2 type:', type(array2))
print('array2 array 차원:', array2.ndim)

# 2차원
array3 = np.array([[1, 2, 3]])
# print(array3)
# print(f'array3 type: {type(array3)}')
print(f'array3 array 차원: {array3.ndim}')