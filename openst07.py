
import cv2
import numpy as np
import matplotlib.pyplot as plt


# 이미지 회전
# cv2.getRotationMatrix2D(center, angle, scale) : 이미지 회전을 위한 변환 행렬을 생성
# ceeter : 회전 중심
# angle : 회전 각도
# scale : scale factor

image = cv2.imread('cat2.jpg')

# 행과 열 정보만 저장
height, width = image.shape[:2]

# width / 2 : 가로 중앙
# height / 2 : 세로 중앙
# 90 : 90도로 회전
# 0.5 : 이미지 크기는 반으로 줄임

M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5)
# 2*3 변환행렬이 만들어짐
print(M)

dst = cv2.warpAffine(image, M, (width, height))

plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()





