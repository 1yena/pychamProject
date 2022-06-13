
import cv2
import numpy as np
import matplotlib.pyplot as plt


# 이미지 위치 이동
# cv2.warpAffine(image, M, dsize) : 이미지 위치 변경
#   - M : 변환 행렬
#   - dsize : manual size


image = cv2.imread('cat2.jpg')

# 행과 열 정보만 저장
# image.shape는 행, 열과 각 픽셀의 정보를 가져오지만 현재는 행과 열 정보만 가져옴
height, width = image.shape[:2]

M = np.float32([[1, 0, 50], [0, 1, 10]])
dst = cv2.warpAffine(image, M, (width, height))

plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()



