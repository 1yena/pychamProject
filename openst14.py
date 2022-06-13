
import cv2
import matplotlib.pyplot as plt
import numpy as np



# 원 그리기
# cv2.circle(image, center, radian, color, thickness) : 하나의 원을 그리는 함수
#   - center : 원의 중심(2차원)
#   - radian : 반지름

image = np.full((512, 512, 3), 255, np.uint8)

# 중심점 위치는 255/255
# 반지름 30 크기
# 색깔은 레드
image = cv2.circle(image, (255, 255), 30, (255, 0, 0), 3)

plt.imshow(image)
plt.show()















