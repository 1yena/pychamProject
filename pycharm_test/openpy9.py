
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.concatenate([arr1, arr2])

print(arr3)
# 배열의 크기를 나타냄 : 6개의 데이터가 담긴 배열.
print(arr3.shape)

print('=================')

# numpy 배열 형태 바꾸기
# 가로축으로 합치기
arr4 = np.array([1, 2, 3, 4])
arr5 = arr4.reshape((2, 2))

print(arr5)

print('=====================')

# 세로축으로 합치기
arr6 = np.arange(4).reshape(1, 4)
arr7 = np.arange(8).reshape(2, 4)
print(arr6)
print(arr7)

print('**********************')

# 세로축 합치기
arr8 = np.concatenate([arr6, arr7], axis=0)
print(arr8)













