
import numpy as np

li = [1, 2, 3]
arr = np.array(li)

print(arr)

# 데이터 개수
print(arr.size)

# 어떤 데이터 타입인지 알려줌
print(arr.dtype)

# 2번 자리에 위치한 데이터 출력
print(arr[2])


print('==================')


# 0 ~ 3까지의 배열 만들기
arr1 = np.arange(4)
print(arr1)

# zeros : 모든 수를 '0'으로 초기화
# 4*4 크기의 배열 만듦
# dtype=float : 데이터 타입은 실수형
arr2 = np.zeros((4, 4), dtype=float)
print(arr2)

# ones : '1'로 초기화
# dtype=str : 데이터 타입은 string
arr3 = np.ones((5, 5), dtype=str)
print(arr3)

# 0 ~ 9까지 랜덤하게 초기화된 배열 만들기
arr4 = np.random.randint(0, 10, (3, 3))
print(arr4)


